%global shortname docker

Name:           devassistant-dap-%{shortname}
Version:        0.10.0dev
Release:        1%{?dist}
Summary:        Docker assistant

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-docker
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args

%description
Runs a Docker container for your project, mounting your source code in.


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
* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-1
Initial package
