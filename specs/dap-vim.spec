%global shortname vim

Name:           dap-%{shortname}
Version:        0.10.0dev
Release:        1%{?dist}
Summary:        Vim snippet and assistant

License:        GPLv2+
URL:            https://github.com/devassistant/dap-vim
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args

%description
Installs and configures vim. Works as a mod assistant or a snippet, so you can use it form other assistants.


%prep
%setup -q -n %{shortname}-%{version}

%install
%install_assistant

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/twk/%{shortname}*
%{assistant_path}/snippets/%{shortname}*

%changelog
* Thu Dec 04 2014 tradej <tradej@redhat.com> - 0.10.0dev-1
Initial package
