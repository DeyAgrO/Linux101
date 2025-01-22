Name:           sorint
Version:        1.0
Release:        1%{?dist}
Summary:        Sorint Project by Ibraheem IBRAHEEM ft GPT 4

License:        GPLv2+
URL:            https://github.com/DeyAgrO
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
Requires:       python3

%description
Linux 101 training lab to do commands exercises

%prep
%setup -q

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -m 755 sorint.py %{buildroot}%{_bindir}/sorint

install -d %{buildroot}%{_datadir}/sorint/my_scripts
cp -r my_scripts/* %{buildroot}%{_datadir}/sorint/my_scripts

%files
%{_bindir}/sorint
%{_datadir}/sorint

%changelog
* Fri Jun 28 2024 Ibraheem IBRAHEEM <ibraheem@sorint.com> - 1.0-1
- Initial package
