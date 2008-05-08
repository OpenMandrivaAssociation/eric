Name: eric
Version: 4.1.3
Release: %mkrel 2
Summary: Full featured Python and Ruby editor and IDE
License: GPLv2+
Group: Development/Python
Source0: http://dfn.dl.sourceforge.net/sourceforge/eric-ide/%{name}4-%{version}.tar.gz
Source1: http://dfn.dl.sourceforge.net/sourceforge/eric-ide/%{name}4-i18n-de-%{version}.tar.gz
Source2: http://dfn.dl.sourceforge.net/sourceforge/eric-ide/%{name}4-i18n-fr-%{version}.tar.gz
Source3: http://dfn.dl.sourceforge.net/sourceforge/eric-ide/%{name}4-i18n-ru-%{version}.tar.gz
Source4: http://dfn.dl.sourceforge.net/sourceforge/eric-ide/%{name}4-i18n-cs-%{version}.tar.gz
URL: http://www.die-offenbachs.de/eric/index.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires: qscintilla-qt4-devel 
BuildRequires: python-sip
BuildRequires: python-qt4
BuildRequires: python-qt4-qscintilla
BuildRequires: imagemagick
%py_requires -d
Requires: python-qt4
Requires: python-qt4-qscintilla
Requires: python-svn
BuildArch: noarch

%description
Eric is a full featured Python and Ruby editor and IDE, written in python. It
is based on the cross platform Qt gui toolkit, integrating the highly flexible
Scintilla editor control. It is designed to be usable as everdays' quick and
dirty editor as well as being usable as a professional project management tool
integrating many advanced features Python offers the professional coder.

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

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Eric
Comment=Python IDE
Exec=eric4
Icon=%{name}
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Development;IDE;QT;
EOF

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert -scale 48 %{buildroot}%{py_puresitedir}/eric4/icons/default/eric.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 %{buildroot}%{py_puresitedir}/eric4/icons/default/eric.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{buildroot}%{py_puresitedir}/eric4/icons/default/eric.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%post
%{update_icon_cache hicolor}
%{update_menus}

%postun
%{clean_icon_cache hicolor}
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 755)
%doc README THANKS
%{_bindir}/*
%py_puresitedir/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
