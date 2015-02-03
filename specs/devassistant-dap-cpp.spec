%global shortname cpp

Name:           devassistant-dap-%{shortname}
Version:        0.10.0
Release:        5%{?dist}
Summary:        C++ assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-cpp
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-eclipse
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github
Requires:       devassistant-dap-vim

%description
Kickstarts new C++ projects


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
%license %{assistant_path}/doc/%{shortname}/NOTICE

%changelog
* Tue Feb 03 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-5
Marked licensing files as %license

* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-4
Initial package
