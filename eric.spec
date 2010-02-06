Name: eric
Version: 4.4.1
Release: %mkrel 2
Summary: Full featured Python and Ruby editor and IDE
License: GPLv2+
Group: Development/Python
Source0: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-%{version}.tar.gz
Source1: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-de-%{version}.tar.gz
Source2: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-fr-%{version}.tar.gz
Source3: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-ru-%{version}.tar.gz
Source4: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-cs-%{version}.tar.gz
Source5: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-es-%{version}.tar.gz
Source6: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-tr-%{version}.tar.gz
Source7: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-zh_CN.GB2312-%{version}.tar.gz
Source8: http://prdownloads.sourceforge.net/project/eric-ide/eric4/stable/%{name}/%{name}4-i18n-it-%{version}.tar.gz
URL: http://eric-ide.python-projects.org/
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
Requires: python-qt4-help
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
%setup -q -n %{name}4-%version -D -T -b 5
%setup -q -n %{name}4-%version -D -T -b 6
%setup -q -n %{name}4-%version -D -T -b 7
%setup -q -n %{name}4-%version -D -T -b 8

%install
rm -rf %buildroot
mkdir -p %buildroot%py_puresitedir/%{name}
%{__python} install.py -i %{buildroot} \
	-b %{_bindir} -d %{py_puresitedir} \
	-a %{qt4dir}/qsci/api

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Eric
Comment=Python IDE
Exec=eric4
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;IDE;QT;
EOF

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert -scale 48 %{buildroot}%{py_puresitedir}/eric4/icons/default/erict.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 %{buildroot}%{py_puresitedir}/eric4/icons/default/erict.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{buildroot}%{py_puresitedir}/eric4/icons/default/erict.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%if %mdkversion < 200900
%post
%{update_icon_cache hicolor}
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_icon_cache hicolor}
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 755)
%doc README THANKS
%{_bindir}/*
%{qt4dir}/qsci/api
%py_puresitedir/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
