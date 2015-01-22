%global shortname eclipse

Name:           devassistant-dap-%{shortname}
Version:        0.10.0dev
Release:        2%{?dist}
Summary:        Eclipse snippet and assistant

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-eclipse
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args

Provides:       dap-%{shortname}-%{release} = %{version}-%{release}
Obsoletes:      dap-%{shortname}-%{release} < %{version}-%{release}

%description
Installs and configures eclipse. Works as a mod assistant or a snippet, so you can use it form other assistants.


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
* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-2
Obsoletes: old pkg name

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-1
Initial package
