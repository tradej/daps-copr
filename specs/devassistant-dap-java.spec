%global shortname java

Name:           devassistant-dap-%{shortname}
Version:        0.10.0
Release:        3%{?dist}
Summary:        Java assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-java
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-eclipse
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github

%description
Kickstarts new Java projects.

Currently supports Maven and JavaServer Faces projects.


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
* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-3
Initial package
