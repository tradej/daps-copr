%global shortname common_args

Name:           devassistant-dap-%{shortname}
Version:        0.10.0
Release:        3%{?dist}
Summary:        Common arguments to be used from other assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-common_args
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui

Provides:       dap-%{shortname} = %{version}-%{release}
Obsoletes:      dap-%{shortname} < %{version}-%{release}

%description
Common arguments used in most of the assistants.

Provided arguments: name, path, rpm, docker, eclipse

Arguments "github" and "gh_fork" are now provided by the assistant
"github", which you need to specify in your Assistant separately.


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
* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-3
Fixed Provides and Obsoletes

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-2
Obsoletes: old pkg name

* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-1
Initial package
