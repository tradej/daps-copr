%global shortname dap

Name:           dap-%{shortname}
Version:        0.0.5
Release:        1%{?dist}
Summary:        Assistants for creating DAPs - DevAssistant packages

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-dap
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.%{shortname}

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-git
Requires:       dap-github

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

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/icons/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*
%{assistant_path}/assistants/twk/%{shortname}*
%{assistant_path}/snippets/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.0.5-1
Initial package
