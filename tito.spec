%global shortname tito

Name:           dap-%{shortname}
Version:        0.10.0dev
Release:        1%{?dist}
Summary:        Tito snippet to use in other assistants

License:        GPLv2+
URL:            https://github.com/devassistant/dap-tito
Source0:        https://dapi.devassistant.org/download/%{name}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui

%description
Snippet that runs tito init in assistants, where you want it


%prep
%setup -q -n %{shortname}-%{version}

%install
%install_assistant

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/snippets/%{shortname}*

%changelog
Thu Dec 04 2014 tradej <tradej@redhat.com> - 0.10.0dev-1
Initial package
