#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : python-ceilometerclient
Version  : 2.9.0
Release  : 41
URL      : http://tarballs.openstack.org/python-ceilometerclient/python-ceilometerclient-2.9.0.tar.gz
Source0  : http://tarballs.openstack.org/python-ceilometerclient/python-ceilometerclient-2.9.0.tar.gz
Source1  : http://tarballs.openstack.org/python-ceilometerclient/python-ceilometerclient-2.9.0.tar.gz.asc
Summary  : OpenStack Telemetry API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-ceilometerclient-bin = %{version}-%{release}
Requires: python-ceilometerclient-license = %{version}-%{release}
Requires: python-ceilometerclient-python = %{version}-%{release}
Requires: python-ceilometerclient-python3 = %{version}-%{release}
Requires: iso8601
Requires: keystoneauth1
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : iso8601
BuildRequires : keystoneauth1
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore

%description
=====================================

%package bin
Summary: bin components for the python-ceilometerclient package.
Group: Binaries
Requires: python-ceilometerclient-license = %{version}-%{release}

%description bin
bin components for the python-ceilometerclient package.


%package license
Summary: license components for the python-ceilometerclient package.
Group: Default

%description license
license components for the python-ceilometerclient package.


%package python
Summary: python components for the python-ceilometerclient package.
Group: Default
Requires: python-ceilometerclient-python3 = %{version}-%{release}

%description python
python components for the python-ceilometerclient package.


%package python3
Summary: python3 components for the python-ceilometerclient package.
Group: Default
Requires: python3-core
Provides: pypi(python_ceilometerclient)
Requires: pypi(iso8601)
Requires: pypi(keystoneauth1)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(stevedore)

%description python3
python3 components for the python-ceilometerclient package.


%prep
%setup -q -n python-ceilometerclient-2.9.0
cd %{_builddir}/python-ceilometerclient-2.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583540244
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-ceilometerclient
cp %{_builddir}/python-ceilometerclient-2.9.0/LICENSE %{buildroot}/usr/share/package-licenses/python-ceilometerclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ceilometer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-ceilometerclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
