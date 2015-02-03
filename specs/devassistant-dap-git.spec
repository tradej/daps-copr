%global shortname git

Name:           devassistant-dap-%{shortname}
Version:        0.10.0dev
Release:        5%{?dist}
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

%files -f dap-files
%license %{assistant_path}/doc/%{shortname}/LICENSE

%changelog
* Tue Feb 03 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-5
Marked licensing files as %license

* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-4
Initial package
