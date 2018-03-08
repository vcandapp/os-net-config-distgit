%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:			os-net-config
Version:		5.2.3
Release:		1%{?dist}
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-sphinx
BuildRequires:	python-oslo-sphinx

Requires:	python-setuptools
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
Requires:	python-pbr

%description
Host network configuration tool for OpenStack.

%prep

%setup -q -n %{name}-%{upstream_version}

%build
%{__python} setup.py build
%{__python} setup.py build_sphinx

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{python_sitelib}/os_net_config*


%changelog
* Thu Mar 08 2018 RDO <dev@lists.rdoproject.org> 5.2.3-1
- Update to 5.2.3

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 5.2.2-1
- Update to 5.2.2

* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 5.2.1-1
- Update to 5.2.1

* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 5.2.0-1
- Update to 5.2.0

* Tue Jan 10 2017 Alfredo Moralejo <amoralej@redhat.com> 5.1.0-1
- Update to 5.1.0

* Thu Nov 17 2016 Jon Schlueter <jschluet@redhat.com> 5.0.0-2
- rebuild with pbr again

* Thu Oct 06 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-1
- Update to 5.0.0

* Fri Sep 30 2016 Alfredo Moralejo <amoralej@redhat.com> 5.0.0-0.2.0rc2
- Update to 5.0.0.0rc2

* Wed Sep 14 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-0.1.0b3
- Update to 5.0.0.0b3

