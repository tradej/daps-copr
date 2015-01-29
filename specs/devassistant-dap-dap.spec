%global shortname dap

Name:           devassistant-dap-%{shortname}
Version:        0.0.5
Release:        4%{?dist}
Summary:        Assistants for creating DAPs - DevAssistant packages

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-dap
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.%{shortname}

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github

%description
This assistants helps you with creating DAPs - DevAssistant packages.
It lets you create the git repository with the sources and also to package
the assistants as .dap file.


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
* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.0.5-4
Initial package
