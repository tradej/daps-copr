%global shortname github

Name:           dap-%{shortname}
Version:        0.10.1
Release:        1%{?dist}
Summary:        GitHub assistant

License:        GPLv2+
URL:            https://github.com/devassistant/dap-github
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-git

%description
Creates GitHub repository (+ local git repository if not already created)
and optionally pushes sources there.
Works even for projects that weren't created by DevAssistant.

Offers --github (push to github) and --gh-fork (fork on github) arguments
to outside assistants


%prep
%setup -q -n %{shortname}-%{version}

%install
%install_assistant

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/assistants/twk/%{shortname}*
%{assistant_path}/snippets/%{shortname}*

%changelog
Thu Dec 04 2014 tradej <tradej@redhat.com> - 0.10.1-1
Initial package
