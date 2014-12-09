%global shortname custom

Name:           dap-%{shortname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Custom prep assistants to develop on an upstream project

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-custom
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-github

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

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/prep/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.10.0-1
Initial package
