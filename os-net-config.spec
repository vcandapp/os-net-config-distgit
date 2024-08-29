%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x4c29ff0e437f3351fd82bdf47c5a3bc787dc7035
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


Name:			os-net-config
Version:		14.2.0
Release:		1%{?dist}
Summary:		Host network configuration tool

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

Requires:	initscripts
Requires:	iproute
Requires:	ethtool
Requires:	dhclient

BuildArch:	noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

BuildRequires:  git-core
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-pbr
BuildRequires:	python3-sphinx
BuildRequires:	python3-openstackdocstheme
# Needed for downsteam test runs
BuildRequires:  nmstate
BuildRequires:  NetworkManager-ovs
BuildRequires:  python3-libnmstate
BuildRequires:  nmstate-libs
BuildRequires:  mstflint

Requires:	python3-eventlet >= 0.18.2
Requires:	python3-oslo-concurrency >= 3.8.0
Requires:	python3-oslo-config
Requires:	python3-oslo-utils >= 3.20.0
Requires:	python3-netaddr >= 0.7.13
Requires:	python3-iso8601 >= 0.1.11
Requires:	python3-six >= 1.9.0
Requires:	python3-pbr >= 2.0.0
Requires:	python3-jsonschema >= 2.6.0

Requires:	python3-PyYAML >= 3.10
Requires:	python3-anyjson >= 0.3.3
Requires:	python3-pyudev >= 0.16.1
# Needed for NetworkManager support
Requires:	NetworkManager-ovs
Requires:	nmstate
Requires:	nispor
Requires:	python3-libnmstate
Requires:       python3-pyroute2 >= 0.6.6

%if 0%{?rhel} == 8
# RHEL8 requires a network-scripts package for ifcfg backwards compatibility
Requires:   network-scripts
%endif

%description
Host network configuration tool for OpenStack.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif

%autosetup -n %{name}-%{upstream_version} -S git

# pyroute2>=0.7.10 is not available in wallaby
sed -i "s/pyroute2>=.*/pyroute2/" requirements.txt

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
%{_bindir}/os-net-config-dcb
%{_bindir}/os-net-config-sriov
%{_bindir}/os-net-config-sriov-bind
%{python3_sitelib}/os_net_config*

%changelog
* Mon Aug 16 2021 RDO <dev@lists.rdoproject.org> 14.2.0-1
- Update to 14.2.0

* Mon Jul 19 2021 RDO <dev@lists.rdoproject.org> 14.1.1-1
- Update to 14.1.1

* Wed May 05 2021 RDO <dev@lists.rdoproject.org> 14.1.0-1
- Update to 14.1.0

