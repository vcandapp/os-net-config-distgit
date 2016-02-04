Name:			os-net-config
Version:		0.1.5
Release:		4%{?dist}
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-sphinx
BuildRequires:	python-oslo-sphinx

Requires:	python-pbr
Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-anyjson
Requires:	python-babel
Requires:	python-eventlet
Requires:	python-oslo-concurrency
Requires:	python-oslo-config
Requires:	python-oslo-utils
Requires:	python-netaddr
Requires:	python-iso8601
Requires:	python-six >= 1.5.0
Requires:	initscripts
Requires:	PyYAML

%description
Host network configuration tool for OpenStack.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python2} setup.py build
%{__python2} setup.py build_sphinx

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{python2_sitelib}/os_net_config*


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 James Slagle <jslagle@redhat.com> 0.1.5-3
- Add Requires: python-pbr

* Tue Oct 20 2015 James Slagle <jslagle@redhat.com> 0.1.5-1
- Update to upstream 0.1.5

* Fri Feb 13 2015 Ben Nemec <bnemec@redhat.com> - 0.1.1-3
- Fix BuildRequires in the srpm

* Fri Feb 06 2015 Ben Nemec <bnemec@redhat.com> - 0.1.1-2
- Cleanups from package review

* Mon Dec 22 2014 Ben Nemec <bnemec@redhat.com> - 0.1.1-1
- Initial Fedora package
