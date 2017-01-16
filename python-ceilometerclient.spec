#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-ceilometerclient
Version  : 2.4.0
Release  : 28
URL      : http://tarballs.openstack.org/python-ceilometerclient/python-ceilometerclient-2.4.0.tar
Source0  : http://tarballs.openstack.org/python-ceilometerclient/python-ceilometerclient-2.4.0.tar
Summary  : OpenStack Telemetry API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-ceilometerclient-bin
Requires: python-ceilometerclient-python
BuildRequires : Babel-python
BuildRequires : Jinja2-python
BuildRequires : Pygments-python
BuildRequires : Sphinx-python
BuildRequires : configparser-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : enum34-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : hacking-python
BuildRequires : imagesize-python
BuildRequires : iso8601-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : monotonic-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr-python
BuildRequires : netifaces-python
BuildRequires : oslo.config-python
BuildRequires : oslo.i18n
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable-python
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : testrepository-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
Python bindings to the Ceilometer API
=====================================
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ``ceilometerclient`` module) and a command-line tool
(``ceilometer``).

%package bin
Summary: bin components for the python-ceilometerclient package.
Group: Binaries

%description bin
bin components for the python-ceilometerclient package.


%package python
Summary: python components for the python-ceilometerclient package.
Group: Default
Requires: iso8601-python
Requires: oslo.i18n-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: python-keystoneclient-python
Requires: requests-python
Requires: six-python

%description python
python components for the python-ceilometerclient package.


%prep
%setup -q -n python-ceilometerclient-2.4.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484567289
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1484567289
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ceilometer

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
