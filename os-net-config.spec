# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


Name:			os-net-config
Version:		11.5.0
Release:		1%{?dist}
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

Requires:	initscripts
Requires:	iproute
Requires:	ethtool
Requires:	dhclient

BuildArch:	noarch

BuildRequires:	python%{pyver}-setuptools
BuildRequires:	python%{pyver}-devel
BuildRequires:	python%{pyver}-pbr
BuildRequires:	python%{pyver}-sphinx
BuildRequires:	python%{pyver}-openstackdocstheme

Requires:	python%{pyver}-eventlet >= 0.18.2
Requires:	python%{pyver}-oslo-concurrency >= 3.8.0
Requires:	python%{pyver}-oslo-config
Requires:	python%{pyver}-oslo-utils >= 3.20.0
Requires:	python%{pyver}-netaddr >= 0.7.13
Requires:	python%{pyver}-iso8601 >= 0.1.11
Requires:	python%{pyver}-six >= 1.9.0
Requires:	python%{pyver}-pbr >= 2.0.0
Requires:	python%{pyver}-jsonschema >= 2.0.0

%if %{pyver} == 2
Requires:	PyYAML >= 3.10
Requires:	python-anyjson >= 0.3.3
Requires:	python-pyudev >= 0.16.1
%else
Requires:	python%{pyver}-PyYAML >= 3.10
Requires:	python%{pyver}-anyjson >= 0.3.3
Requires:	python%{pyver}-pyudev >= 0.16.1
%endif

%if 0%{?rhel} > 7
# RHEL8 requires a network-scripts package for ifcfg backwards compatibility
Requires:   network-scripts
%endif

%description
Host network configuration tool for OpenStack.

%prep

%setup -q -n %{name}-%{upstream_version}

%build
%{pyver_build}
%{pyver_bin} setup.py build_sphinx

%install
%{pyver_install}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{_bindir}/os-net-config-sriov
%{pyver_sitelib}/os_net_config*

%changelog
* Mon Apr 05 2021 RDO <dev@lists.rdoproject.org> 11.5.0-1
- Update to 11.5.0

* Mon Feb 08 2021 RDO <dev@lists.rdoproject.org> 11.4.0-1
- Update to 11.4.0

* Mon Jan 06 2020 RDO <dev@lists.rdoproject.org> 11.3.1-1
- Update to 11.3.1

* Mon Oct 21 2019 RDO <dev@lists.rdoproject.org> 11.3.0-1
- Update to 11.3.0

