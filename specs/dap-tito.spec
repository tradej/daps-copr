%global shortname tito

Name:           dap-%{shortname}
Version:        0.10.0dev
Release:        1%{?dist}
Summary:        Tito snippet to use in other assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-tito
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui

%description
Snippet that runs tito init in assistants, where you want it


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
%{assistant_path}/snippets/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.10.0dev-1
Initial package
