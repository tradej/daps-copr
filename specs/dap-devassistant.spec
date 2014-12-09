%global shortname devassistant

Name:           dap-%{shortname}
Version:        0.10.1dev
Release:        1%{?dist}
Summary:        DevAssistant prep assistants to develop DevAssistant itself

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-devassistant
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-git
Requires:       dap-github
Requires:       dap-python

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
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/prep/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.10.1dev-1
Initial package
