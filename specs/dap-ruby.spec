%global shortname ruby

Name:           dap-%{shortname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Ruby assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-ruby
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       dap-common_args
Requires:       dap-git
Requires:       dap-github
Requires:       dap-vim

%description
Kickstarts new Ruby projects. Currently only supports Ruby on Rails.


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
%{assistant_path}/meta/%{shortname}.yaml

%changelog
* Tue Dec 09 2014 Tomas Radej <tradej@redhat.com> - 0.10.0-1
Initial package
