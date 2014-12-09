%global shortname common_args

Name:           dap-%{shortname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Common arguments to be used from other assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-common_args
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui

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

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/snippets/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.10.0-1
Initial package
