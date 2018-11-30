# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pydefault 3
%else
%global pydefault 2
%endif

%global pydefault_bin python%{pydefault}
%global pydefault_sitelib %python%{pydefault}_sitelib
%global pydefault_install %py%{pydefault}_install
%global pydefault_build %py%{pydefault}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


Name:			os-net-config
Version:		XXX
Release:		XXX
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

Requires:	initscripts
Requires:	iproute
Requires:	ethtool
Requires:	dhclient

BuildArch:	noarch

BuildRequires:	python%{pydefault}-setuptools
BuildRequires:	python%{pydefault}-devel
BuildRequires:	python%{pydefault}-pbr
BuildRequires:	python%{pydefault}-sphinx
BuildRequires:	python%{pydefault}-oslo-sphinx

Requires:	python%{pydefault}-eventlet >= 0.18.2
Requires:	python%{pydefault}-oslo-concurrency >= 3.8.0
Requires:	python%{pydefault}-oslo-config
Requires:	python%{pydefault}-oslo-utils >= 3.20.0
Requires:	python%{pydefault}-netaddr >= 0.7.13
Requires:	python%{pydefault}-iso8601 >= 0.1.11
Requires:	python%{pydefault}-six >= 1.9.0
Requires:	python%{pydefault}-pbr >= 2.0.0
Requires:	python%{pydefault}-jsonschema >= 2.0.0

%if %{pydefault} == 2
Requires:	PyYAML >= 3.10
Requires:	python-anyjson >= 0.3.3
Requires:	python-pyudev >= 0.15
%else
Requires:	python%{pydefault}-PyYAML >= 3.10
Requires:	python%{pydefault}-anyjson >= 0.3.3
Requires:	python%{pydefault}-pyudev >= 0.15
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
%{pydefault_build}
%{pydefault_bin} setup.py build_sphinx

%install
%{pydefault_install}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{_bindir}/os-net-config-sriov
%{pydefault_sitelib}/os_net_config*

%changelog
