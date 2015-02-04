%global shortname devassistant

Name:           devassistant-dap-%{shortname}
Version:        0.10.1dev
Release:        6%{?dist}
Summary:        DevAssistant prep assistants to develop DevAssistant itself

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-devassistant
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github
Requires:       devassistant-dap-python

%description
Set up environment for DevAssistant, so you can develop on DevAssistant trough DevAssistant. We have to go deeper.


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
%{assistant_path}/assistants/prep/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Wed Feb 04 2015 Tomas Radej <tradej@redhat.com> - 0.10.1dev-6
Verbose files section

* Tue Feb 03 2015 Tomas Radej <tradej@redhat.com> - 0.10.1dev-5
Marked licensing files with proper macro

* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.1dev-4
Initial package
