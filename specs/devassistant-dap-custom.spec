%global shortname custom

Name:           devassistant-dap-%{shortname}
Version:        0.10.0
Release:        3%{?dist}
Summary:        Custom prep assistants to develop on an upstream project

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-custom
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-github

Provides:       dap-%{shortname} = %{version}-%{release}
Obsoletes:      dap-%{shortname} < %{version}-%{release}

%description
The custom assistant sets up environment for developing custom project
previously created with DevAssistant.

If the project contains a .devassistant file, you may choose to execute it.
However, only do so with projects you trust, since the file can contain
arbitrary custom commands that will run on your machine.


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
Fixed Provides and Obsoletes

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-2
Obsoletes: old pkg name

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-1
Initial package
