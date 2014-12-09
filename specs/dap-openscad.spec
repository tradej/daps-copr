%global shortname openscad

Name:           dap-%{shortname}
Version:        0.0.2
Release:        1%{?dist}
Summary:        Create 3D printing projects for OpenSCAD

BuildArch:      noarch

License:        GPLv3+ and GPLv2 with exceptions
URL:            https://github.com/3DprintFIT/dap-openscad
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-git
Requires:       dap-github

%description
This assistants helps you to create new OpenSCAD project for 3D printing.
We use it in our 3D printing lab to store our 3D printers on Github.

Projects created with this assistant have a `Makefile` to build the 3D models form OpenSCAD sources.
To do so, run `make`. You can also generate the images by `make images` or print plates with `make arrange`.
Observe the generated `Makefile` to see all available options.


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
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.0.2-1
Initial package
