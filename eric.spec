%define name 	eric
%define version 3.8.2
%define release 1mdk

# py_ver, because modules have to be recompiled for another Python version

Summary:	Python IDE
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Python
Source0:	http://prdownloads.sourceforge.net/eric-ide/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/eric-ide/%{name}-i18n-de-%{version}.tar.bz2
Source2:        http://prdownloads.sourceforge.net/eric-ide/%{name}-i18n-fr-%{version}.tar.bz2
Source3:        http://prdownloads.sourceforge.net/eric-ide/%{name}-i18n-ru-%{version}.tar.bz2
URL:		http://www.die-offenbachs.de/detlev/eric3.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libqscintilla-devel python-devel >= %{pyver} PyQt
Requires:	PyQt 
BuildArch: noarch

%description
Eric3 is a full featured Python IDE that is written in PyQt using the 
QScintilla editor widget. 

%prep
%setup -q 
tar xjf %{SOURCE1}
tar xjf %{SOURCE2}
tar xjf %{SOURCE3}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pyver}/site-packages
%{__python} install.py -i $RPM_BUILD_ROOT -b %{_bindir}

cp -r %{name}-%{version}/%{name}/* $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages/%{name}

#menu
mkdir -p %buildroot/%{_menudir}
cat << EOF > %buildroot/%{_menudir}/%{name}
?package(%{name}): command="eric3" icon="development_environment_section.png" needs="x11" title="Eric" longtitle="Python IDE" section="Applications/Development/Development Environments"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 755)
%doc README THANKS HISTORY LICENSE.GPL
%{_bindir}/*
%{_libdir}/python%{pyver}/site-packages/
%{_menudir}/%name

