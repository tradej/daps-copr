%global shortname python

Name:           devassistant-dap-%{shortname}
Version:        0.10.1
Release:        3%{?dist}
Summary:        Python assistants (library, Django, Flask, GTK3)

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/bkabrda/dap-python
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-eclipse
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github
Requires:       devassistant-dap-tito
Requires:       devassistant-dap-vim

%description
Set of crt assistants for Python. Contains assistants that let you
kickstart new Django or Flask web application, pure Python library or GTK3 app.
Supports both Python 2 and 3.


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
