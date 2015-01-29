%global shortname vim

Name:           devassistant-dap-%{shortname}
Version:        0.10.0dev
Release:        3%{?dist}
Summary:        Vim snippet and assistant

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-vim
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args

%description
Installs and configures vim. Works as a mod assistant or a snippet, so you can use it form other assistants.


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
Initial package
