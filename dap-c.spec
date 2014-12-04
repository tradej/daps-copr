%global shortname c

Name:           dap-%{shortname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        C assistants

License:        GPLv2+
URL:            https://github.com/devassistant/dap-c
Source0:        https://dapi.devassistant.org/download/%{name}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-eclipse
Requires:       dap-git
Requires:       dap-github
Requires:       dap-vim

%description
Kickstarts new C project and more C related assistants


%prep
%setup -q -n %{shortname}-%{version}

%install
%install_assistant

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/icons/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*
%{assistant_path}/assistants/twk/%{shortname}*

%changelog
Thu Dec 04 2014 tradej <tradej@redhat.com> - 0.10.0-1
Initial package
