%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order bashate
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%global with_doc 1


Name:			os-net-config
Version:		XXX
Release:		XXX
Summary:		Host network configuration tool

License:		Apache-2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:	noarch
%if 0%{?rhel} || 0%{?centos}
# The mstflint package does not have builds for these architectures
# on RHEL; choose a different arch host when building the noarch
# package.
ExcludeArch:    s390 s390x
%endif

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  git-core
BuildRequires:	python3-devel
BuildRequires:	pyproject-rpm-macros
# Needed for NetworkManager support
BuildRequires:	NetworkManager-ovs
BuildRequires:	iproute
BuildRequires:	ethtool
BuildRequires:	nmstate
%if !(0%{?rhel} < 9)
BuildRequires:  nmstate-libs
%endif
BuildRequires:	python3-libnmstate
BuildRequires:	nispor

Requires:	initscripts
Requires:	iproute
Requires:	ethtool
Requires:	dhclient
Requires: 	mstflint

# Needed for NetworkManager support
Requires:	NetworkManager-ovs
Requires:	nmstate
Requires:	python3-libnmstate
Requires:	nispor

%description
Host network configuration tool for OpenStack.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif

%autosetup -n %{name}-%{upstream_version} -S git

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# (TODO) There is no pyroute2>=0.7.10 in fedora yet.
sed -i 's/pyroute2>=0.7.10/pyroute2>=0.7.3/g' requirements.txt

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif


%build
%pyproject_wheel

%if 0%{?with_doc}
%tox -e docs
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
%tox -e %{default_toxenv}

%files
%doc README.rst
%doc LICENSE
%if 0%{?with_doc}
%doc doc/build/html
%endif

%{_bindir}/os-net-config
%{_bindir}/os-net-config-dcb
%{_bindir}/os-net-config-sriov
%{_bindir}/os-net-config-sriov-bind
%{python3_sitelib}/os_net_config*

%changelog

