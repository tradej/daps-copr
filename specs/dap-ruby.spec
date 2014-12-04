%global shortname ruby

Name:           dap-%{shortname}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Ruby assistants

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

%install
%install_assistant

%files
%doc %{assistant_path}/doc/%{shortname}
%{assistant_path}/icons/%{shortname}
%{assistant_path}/assistants/crt/%{shortname}*

%changelog
* Thu Dec 04 2014 tradej <tradej@redhat.com> - 0.10.0-1
Initial package
