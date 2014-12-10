%global shortname python

Name:           dap-%{shortname}
Version:        0.10.1
Release:        1%{?dist}
Summary:        Python assistants (library, Django, Flask, GTK3)

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/bkabrda/dap-python
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-eclipse
Requires:       dap-git
Requires:       dap-github
Requires:       dap-tito
Requires:       dap-vim

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

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*
%{assistant_path}/files/crt/%{shortname}*
%{assistant_path}/icons/crt/%{shortname}*
%{assistant_path}/snippets/%{shortname}*
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Wed Dec 10 2014 Tomas Radej <tradej@redhat.com> - 0.10.1-1
Initial package
