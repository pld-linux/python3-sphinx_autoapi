#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Sphinx API documentation generator
Summary(pl.UTF-8):	Generator dokumentacji API dla Sphinksa
Name:		python3-sphinx_autoapi
Version:	3.6.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-autoapi/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-autoapi/sphinx_autoapi-%{version}.tar.gz
# Source0-md5:	63b92634cbf39440c5d531b4701c2b6a
URL:		https://pypi.org/project/sphinx-autoapi/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-PyYAML
BuildRequires:	python3-Sphinx >= 7.4.0
BuildRequires:	python3-astroid >= 3.0
BuildRequires:	python3-jinja2
BuildRequires:	python3-pytest
BuildRequires:	python3-unidecode
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx AutoAPI provides "autodoc" style documentation for multiple
programming languages without needing to load, run, or import the
project being documented.

In contrast to the traditional Sphinx autodoc, which is Python-only
and uses code imports, AutoAPI finds and generates documentation by
parsing source code.

%description -l pl.UTF-8
Sphinx AutoAPI zapewnia dokumentację w stylu "autodoc" dla wielu
języków programowania bez potrzeby ładowania, uruchamiania lub
importowania dokumentowanego projektu.

W przeciwieństwie do tradycyjnego autodoc dla Sphinksa, który działa
tylko dla Pythona i wykorzystuje importowanie kodu, AutoAPI wyszukuje
i generuje dokumentację poprzez analizę kodu źródłowego.

%prep
%setup -q -n sphinx_autoapi-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# test_pyintegration.py::TestPipeUnionModule::test_integration requires network for intersphinx
# test_pyintegration.py::TestMovedConfPy::test_{integration,napoleon_integration_not_loaded,show_inheritance,long_signature} need some files not in sdist(?)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests -k 'not test_pyintegration.py'
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst
%{py3_sitescriptdir}/autoapi
%{py3_sitescriptdir}/sphinx_autoapi-%{version}.dist-info
