%global shortname git

Name:           dap-%{shortname}
Version:        0.10.0dev
Release:        1%{?dist}
Summary:        Git snippet to be used from other assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-git
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui

%description
Git snippet, allowing to initialize a git repo and commit everything.


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
