%global shortname ruby

Name:           devassistant-dap-%{shortname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Ruby assistants

BuildArch:      noarch

License:        GPLv2+
URL:            https://github.com/devassistant/dap-ruby
Source0:        https://dapi.devassistant.org/download/%{shortname}-%{version}.dap

BuildRequires:  devassistant-devel
Requires:       devassistant-ui
Requires:       devassistant-dap-common_args
Requires:       devassistant-dap-git
Requires:       devassistant-dap-github
Requires:       devassistant-dap-vim

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

%files -f dap-files

%changelog
* Wed Jan 21 2015 Tomas Radej <tradej@redhat.com> - 0.10.0-1
Initial package