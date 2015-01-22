%global shortname docker

Name:           devassistant-dap-%{shortname}
Version:        0.10.0dev
Release:        3%{?dist}
Summary:        Docker assistant

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-docker
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args

Provides:       dap-%{shortname} = %{version}-%{release}
Obsoletes:      dap-%{shortname} < %{version}-%{release}

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
* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-3
Fixed Provides and Obsoletes

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-2
Obsoletes: old pkg name

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-1
Initial package
