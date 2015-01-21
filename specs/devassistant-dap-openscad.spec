%global shortname openscad

Name:           devassistant-dap-%{shortname}
Version:        0.0.2
Release:        1%{?dist}
Summary:        Create 3D printing projects for OpenSCAD

BuildArch:      noarch

License:        GPLv3+ and GPLv2 with exceptions
URL:            https://github.com/3DprintFIT/dap-openscad
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github

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

%files -f dap-files

%changelog
* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.0.2-1
Initial package
