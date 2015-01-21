%global shortname devassistant

Name:           devassistant-dap-%{shortname}
Version:        0.10.1dev
Release:        1%{?dist}
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

%files -f dap-files

%changelog
* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.1dev-1
Initial package
