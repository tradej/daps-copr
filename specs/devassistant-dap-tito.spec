%global shortname tito

Name:           devassistant-dap-%{shortname}
Version:        0.10.0dev
Release:        2%{?dist}
Summary:        Tito snippet to use in other assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-tito
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui

Provides:       dap-%{shortname} = %{version}-%{release}
Obsoletes:      dap-%{shortname} < %{version}-%{release}

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

%files -f dap-files

%changelog
* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-2
Obsoletes old pkg name

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0dev-1
Initial package
