%global shortname nodejs

Name:           devassistant-dap-%{shortname}
Version:        0.10.1
Release:        3%{?dist}
Summary:        Node.js assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-nodejs
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github
Requires:       devassistant-dap-vim

%description
Kickstarts new Node.js projects with or without the Express framework.


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
* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.1-3
Initial package
