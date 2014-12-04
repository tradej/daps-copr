%global shortname git

Name:           dap-%{shortname}
Version:        0.10.0dev
Release:        1%{?dist}
Summary:        Git snippet to be used from other assistants

License:        GPLv2+
URL:            https://github.com/devassistant/dap-git
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui

%description
Git snippet, allowing to initialize a git repo and commit everything.


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
