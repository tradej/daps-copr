%global shortname cpp

Name:           dap-%{shortname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        C++ assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-cpp
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-eclipse
Requires:       dap-git
Requires:       dap-github
Requires:       dap-vim

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

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*
%{assistant_path}/files/crt/%{shortname}*
%{assistant_path}/icons/crt/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Wed Dec 10 2014 Tomas Radej <tradej@redhat.com> - 0.10.0-1
Initial package
