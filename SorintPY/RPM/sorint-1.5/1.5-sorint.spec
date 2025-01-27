Name:           sorint
Version:        1.5
Release:        el9
Summary:        Sorint Lab Project by Ibraheem IBRAHEEM & GPT 4
Group:          Sorint France

License:        GPLv2+
URL:            https://github.com/DeyAgrO/Linux101
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
Requires:       python3

%description
Linux 101 Training Lab Commands Exercises
The Number is Nu=SO6ZK9200LFQ82

%prep
%setup -q

%build
# No build steps necessary for this script

%install
install -d %{buildroot}/usr/bin
install -m 755 sorint.py %{buildroot}/usr/bin/sorint

install -d %{buildroot}/usr/lib/sorint
cp -r my_scripts %{buildroot}/usr/lib/sorint/

%files
%doc
/usr/bin/sorint
/usr/lib/sorint/my_scripts

%changelog
* Wed Jan 22 2025 Ibraheem IBRAHEEM <iibraheem@sorint.com> - 1.5
- Initial package
