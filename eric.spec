Name: eric
Version: 4.0.1
Release: %mkrel 1
Summary: Eric is a full featured Python and Ruby editor and IDE
License: GPL
Group: Development
Source0: %{name}4-%{version}.tar.gz
Source1: %{name}4-i18n-de-%{version}.tar.gz
Source2: %{name}4-i18n-fr-%{version}.tar.gz
Source3: %{name}4-i18n-ru-%{version}.tar.gz
Source4: %{name}4-i18n-cs_CZ-%{version}.tar.gz
URL: http://www.die-offenbachs.de/eric/index.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires: qscintilla-qt4-devel 
BuildRequires: python-sip
BuildRequires: python-qt4
BuildRequires: python-qt4-qscintilla
%py_requires -d
Requires: python-qt4
Requires: python-svn
Requires"
BuildArch: noarch

%description
Eric is a full featured Python and Ruby editor and IDE, written in python. It is based on the cross
platform Qt gui toolkit, integrating the highly flexible Scintilla editor control. It is designed to
be usable as everdays' quick and dirty editor as well as being usable as a professional project
management tool integrating many advanced features Python offers the professional coder.

%prep
%setup -q -n %{name}4-%version
# This unpacks the i18n sources correctly. The previous spec unpacked them to the wrong place. -AdamW, 2007/05
%setup -q -n %{name}4-%version -D -T -b 1
%setup -q -n %{name}4-%version -D -T -b 2
%setup -q -n %{name}4-%version -D -T -b 3
%setup -q -n %{name}4-%version -D -T -b 4

%install
rm -rf %buildroot
mkdir -p %buildroot%py_puresitedir/%{name}
%{__python} install.py -i %buildroot -b %{_bindir}

%post
%update_menus
%update_icon_cache hicolor
%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 755)
%doc README THANKS LICENSE.GPL
%{_bindir}/*
%py_puresitedir/*
