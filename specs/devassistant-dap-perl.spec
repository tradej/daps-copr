%global shortname perl

Name:           devassistant-dap-%{shortname}
Version:        0.10.0
Release:        4%{?dist}
Summary:        Perl assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-perl
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github
Requires:       devassistant-dap-vim

%description
Kickstarts new Perl projects.


%prep
%setup -q -n %{shortname}-%{version}

%build
%repack_assistant

%install
%install_assistant

%check
%check_assistant

%files
%license %{assistant_path}/doc/%{shortname}/LICENSE
%license %{assistant_path}/doc/%{shortname}/NOTICE
%dir %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*
%{assistant_path}/files/crt/%{shortname}*
%{assistant_path}/icons/crt/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Feb 03 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-4
Marked licensing files as %license

* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-3
Initial package
