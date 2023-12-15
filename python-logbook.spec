#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A logging replacement for Python
Summary(pl.UTF-8):	Zamiennik biblioteki logging dla Pythona
Name:		python-logbook
# keep 1.5.x here for python2 support
Version:	1.5.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/logbook/
Source0:	https://files.pythonhosted.org/packages/source/l/logbook/Logbook-%{version}.tar.gz
# Source0-md5:	719970ea22dd274797bb4328161d700f
URL:		https://pypi.org/project/Logbook/
BuildRequires:	python >= 1:2.7
BuildRequires:	python-Cython
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Logbook is a nice logging replacement.

%description -l pl.UTF-8
Logbook to przyjemny zamiennik biblioteki logging.

%prep
%setup -q -n Logbook-%{version}

%build
cd logbook
cythonize _speedups.pyx
cd ..
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-2/lib.linux-*) \
%{__python} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.md
%dir %{py_sitedir}/logbook
%attr(755,root,root) %{py_sitedir}/logbook/_speedups.so
%{py_sitedir}/logbook/*.py[co]
%{py_sitedir}/Logbook-%{version}-py*.egg-info
