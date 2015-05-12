Name:			os-net-config
Version:		0.1.3
Release:		1%{?dist}
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

#
# patches_base=+1
#

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-sphinx
BuildRequires:	python-oslo-sphinx

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
Requires:	PyYAML

%description
Host network configuration tool for OpenStack.

%prep

%setup -q -n %{name}-%{version}


sed -i '/setuptools_git/d' setup.py
sed -i s/REDHATOSNETCONFIGVERSION/%{version}/ os_net_config/version.py
sed -i s/REDHATOSNETCONFIGRELEASE/%{release}/ os_net_config/version.py

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
* Mon May 11 2015 Mike Burns <mburns@redhat.com> 0.1.3-1
- Update to upstream 0.1.3

* Mon May 11 2015 Mike Burns <mburns@redhat.com> 0.1.2-1
- Update to upstream 0.1.2

* Fri May 08 2015 Mike Burns <mburns@redhat.com> 0.1.3-2
- Update to upstream 0.1.3

* Fri Feb 13 2015 Ben Nemec <bnemec@redhat.com> - 0.1.1-3
- Fix BuildRequires in the srpm

* Fri Feb 06 2015 Ben Nemec <bnemec@redhat.com> - 0.1.1-2
- Cleanups from package review

* Mon Dec 22 2014 Ben Nemec <bnemec@redhat.com> - 0.1.1-1
- Initial Fedora package
