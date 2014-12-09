%global shortname eclipse

Name:           dap-%{shortname}
Version:        0.10.0dev
Release:        1%{?dist}
Summary:        Eclipse snippet and assistant

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-eclipse
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args

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

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/twk/%{shortname}*
%{assistant_path}/files/snippets/%{shortname}*
%{assistant_path}/snippets/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.10.0dev-1
Initial package
