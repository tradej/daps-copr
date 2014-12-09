%global shortname nodejs

Name:           dap-%{shortname}
Version:        0.10.1
Release:        1%{?dist}
Summary:        Node.js assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-nodejs
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-git
Requires:       dap-github
Requires:       dap-vim

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

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/icons/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*
%{assistant_path}/files/crt/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.10.1-1
Initial package
