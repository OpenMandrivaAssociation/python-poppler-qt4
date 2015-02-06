Name:		python-poppler-qt4
Version:	0.16.3
Release:	4
Summary:	Python bindings for the Poppler PDF rendering library
Group:		Office
License:	LGPLv2+
URL:		http://code.google.com/p/%{name}/
Source0:	http://python-poppler-qt4.googlecode.com/files/python-poppler-qt4-%{version}.tar.gz
Patch0:		python-poppler-qt4-0.16.3-link.patch
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
%patch0 -p0 -b .link


%install
python setup.py install --single-version-externally-managed --root=%{buildroot}

%files
%doc ChangeLog LICENSE TODO README
%{python_sitearch}/popplerqt4.so
%{python_sitearch}/python_poppler*


%changelog
* Tue Jan 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.16.2-1
+ Revision: 761983
- imported package python-poppler-qt4

