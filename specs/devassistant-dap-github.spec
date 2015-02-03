%global shortname github

Name:           devassistant-dap-%{shortname}
Version:        0.10.1
Release:        5%{?dist}
Summary:        GitHub assistant

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-github
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-git

%description
Creates GitHub repository (+ local git repository if not already created)
and optionally pushes sources there.
Works even for projects that weren't created by DevAssistant.

Offers --github (push to github) and --gh-fork (fork on github) arguments
to outside assistants


%prep
%setup -q -n %{shortname}-%{version}

%build
%repack_assistant

%install
%install_assistant

%check
%check_assistant

%files -f dap-files
%license %{assistant_path}/doc/%{shortname}/LICENSE

%changelog
* Tue Feb 03 2015 Tomas Radej <tradej@redhat.com> - 0.10.1-5
Marked licensing files as %license

* Thu Jan 22 2015 Tomas Radej <tradej@redhat.com> - 0.10.1-4
Initial package
