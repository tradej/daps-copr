%global shortname vim

Name:           devassistant-dap-%{shortname}
Version:        0.10.0dev
Release:        5%{?dist}
Summary:        Vim snippet and assistant

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-vim
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args

%description
Installs and configures vim. Works as a mod assistant or a snippet, so you can use it form other assistants.


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
%dir %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/twk/%{shortname}*
%{assistant_path}/files/snippets/%{shortname}*
%{assistant_path}/snippets/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Wed Feb 04 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-5
Verbose files section

* Tue Feb 03 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-4
Marked licensing files with proper macro

* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-3
Initial package
