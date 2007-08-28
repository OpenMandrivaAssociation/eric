%define name 	eric
%define version 3.9.5
%define release %mkrel 2

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
BuildRequires:	qscintilla-devel python-devel >= %{pyver} PyQt ImageMagick
Requires:	PyQt 
BuildArch: noarch

%description
Eric3 is a full featured Python IDE that is written in PyQt using the 
QScintilla editor widget. 

%prep
%setup -q
# This unpacks the i18n sources correctly. The previous spec unpacked them to the wrong place. -AdamW, 2007/05
%setup -q -D -T -b 1
%setup -q -D -T -b 2
%setup -q -D -T -b 3

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%py_puresitedir/%{name}
%{__python} install.py -i $RPM_BUILD_ROOT -b %{_bindir}

# This looks wrong and the app seems to work without it. -AdamW, 2007/05
#cp -r %{name}-%{version}/%{name}/* $RPM_BUILD_ROOT%py_puresitedir/%{name}

#icons

mkdir -p %buildroot{%_liconsdir,%_miconsdir}
mkdir -p %buildroot%{_iconsdir}/hicolor/{32x32,16x16}/apps
install -m644 %{name}/icons/default/%{name}.png %buildroot%{_iconsdir}/%{name}.png
install -m644 %{name}/icons/default/%{name}.png %buildroot%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 48 %{name}/icons/default/%{name}.png %buildroot%{_liconsdir}/%{name}.png
convert -scale 16 %{name}/icons/default/%{name}.png %buildroot%{_miconsdir}/%{name}.png
convert -scale 16 %{name}/icons/default/%{name}.png %buildroot%{_iconsdir}/hicolor/16x16/apps/%{name}.png

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Eric3
Comment=Python IDE
Exec=%{_bindir}/%{name}3 
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;Development;X-MandrivaLinux-MoreApplications-Development-DevelopmentEnvironments;
EOF

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
%py_puresitedir/eric3config.*
%py_puresitedir/sitecustomize.*
%py_puresitedir/%{name}3
%_iconsdir/hicolor/16x16/apps/%{name}.png
%_iconsdir/hicolor/32x32/apps/%{name}.png
%_liconsdir/%{name}.png
%_iconsdir/%{name}.png
%_miconsdir/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
