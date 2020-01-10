Name:		python-poppler-qt4
Version:	0.24.0
Release:	1
Summary:	Python bindings for the Poppler PDF rendering library
Group:		Office
License:	LGPLv2+
URL:		https://github.com/wbsoft/python-poppler-qt4
Source0:	https://github.com/wbsoft/python-poppler-qt4/releases/python-poppler-qt4-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-qt4-devel
BuildRequires:	pkgconfig(poppler-qt4) >= 0.12.0
BuildRequires:	python-sip >= 4.9.1
BuildRequires:	python-distribute

%description
Python bindings for the Poppler PDF rendering library. It is needed to run
programs written in Python and using Poppler set.


%prep
%setup -q
%autopatch -p1

%install
python setup.py install --single-version-externally-managed --root=%{buildroot} build_ext -lQtGui -lQtCore

%files
%doc ChangeLog LICENSE TODO README.rst
%{python_sitearch}/popplerqt4.*.so
%{python_sitearch}/python_poppler*
