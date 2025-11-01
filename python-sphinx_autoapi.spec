#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-sphinx_autoapi.spec)

Summary:	Sphinx API documentation generator
Summary(pl.UTF-8):	Generator dokumentacji API dla Sphinksa
Name:		python-sphinx_autoapi
# keep 1.5.x here for python2 support
Version:	1.5.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-autoapi/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-autoapi/sphinx-autoapi-%{version}.tar.gz
# Source0-md5:	afcddb6cfbd234dbc1f65ed73eb25330
URL:		https://pypi.org/project/sphinx-autoapi/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML
BuildRequires:	python-Sphinx >= 1.6
BuildRequires:	python-astroid
BuildRequires:	python-jinja2
BuildRequires:	python-mock
BuildRequires:	python-pytest
BuildRequires:	python-sphinxcontrib-dotnetdomain
BuildRequires:	python-sphinxcontrib-golangdomain
BuildRequires:	python-unidecode
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML
BuildRequires:	python3-Sphinx >= 1.6
BuildRequires:	python3-astroid
BuildRequires:	python3-jinja2
BuildRequires:	python3-mock
BuildRequires:	python3-pytest
BuildRequires:	python3-sphinxcontrib-dotnetdomain
BuildRequires:	python3-sphinxcontrib-golangdomain
BuildRequires:	python3-unidecode
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-sphinx_autoapi
Summary:	Sphinx API documentation generator
Summary(pl.UTF-8):	Generator dokumentacji API dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-sphinx_autoapi
Sphinx AutoAPI provides "autodoc" style documentation for multiple
programming languages without needing to load, run, or import the
project being documented.

In contrast to the traditional Sphinx autodoc, which is Python-only
and uses code imports, AutoAPI finds and generates documentation by
parsing source code.

%description -n python3-sphinx_autoapi -l pl.UTF-8
Sphinx AutoAPI zapewnia dokumentację w stylu "autodoc" dla wielu
języków programowania bez potrzeby ładowania, uruchamiania lub
importowania dokumentowanego projektu.

W przeciwieństwie do tradycyjnego autodoc dla Sphinksa, który działa
tylko dla Pythona i wykorzystuje importowanie kodu, AutoAPI wyszukuje
i generuje dokumentację poprzez analizę kodu źródłowego.

%prep
%setup -q -n sphinx-autoapi-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.rst README.rst
%{py_sitescriptdir}/autoapi
%{py_sitescriptdir}/sphinx_autoapi-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_autoapi
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.rst README.rst
%{py3_sitescriptdir}/autoapi
%{py3_sitescriptdir}/sphinx_autoapi-%{version}-py*.egg-info
%endif
