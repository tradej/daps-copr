%global shortname devassistant

Name:           dap-%{shortname}
Version:        0.10.1dev
Release:        1%{?dist}
Summary:        DevAssistant prep assistants to develop DevAssistant itself

License:        GPLv2+
URL:            https://github.com/devassistant/dap-devassistant
Source0:        https://dapi.devassistant.org/download/%{name}-%{version}.dap

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

%install
%install_assistant

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/prep/%{shortname}*

%changelog
Thu Dec 04 2014 tradej <tradej@redhat.com> - 0.10.1dev-1
Initial package
