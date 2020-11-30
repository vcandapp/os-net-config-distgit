%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


Name:			os-net-config
Version:		12.3.2
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

BuildRequires:  git
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-pbr
BuildRequires:	python3-sphinx
BuildRequires:	python3-openstackdocstheme

Requires:	python3-eventlet >= 0.18.2
Requires:	python3-oslo-concurrency >= 3.8.0
Requires:	python3-oslo-config
Requires:	python3-oslo-utils >= 3.20.0
Requires:	python3-netaddr >= 0.7.13
Requires:	python3-iso8601 >= 0.1.11
Requires:	python3-six >= 1.9.0
Requires:	python3-pbr >= 2.0.0
Requires:	python3-jsonschema >= 2.0.0

Requires:	python3-PyYAML >= 3.10
Requires:	python3-anyjson >= 0.3.3
Requires:	python3-pyudev >= 0.16.1

%if 0%{?rhel} > 7
# RHEL8 requires a network-scripts package for ifcfg backwards compatibility
Requires:   network-scripts
%endif

%description
Host network configuration tool for OpenStack.

%prep

%autosetup -n %{name}-%{upstream_version} -S git

%build
%{py3_build}
sphinx-build -W -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%files
%doc README.rst
%doc LICENSE
%doc doc/build/html
%{_bindir}/os-net-config
%{_bindir}/os-net-config-sriov
%{_bindir}/os-net-config-sriov-bind
%{python3_sitelib}/os_net_config*

%changelog
* Mon Oct 05 2020 RDO <dev@lists.rdoproject.org> 12.3.2-1
- Update to 12.3.2

* Tue Jul 28 2020 RDO <dev@lists.rdoproject.org> 12.3.1-1
- Update to 12.3.1

* Tue May 26 2020 RDO <dev@lists.rdoproject.org> 12.3.0-1
- Update to 12.3.0

* Thu May 07 2020 RDO <dev@lists.rdoproject.org> 12.2.0-1
- Update to 12.2.0

