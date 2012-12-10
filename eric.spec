Name: eric
Version: 4.5.7
Release: 1
Summary: Full featured Python and Ruby editor and IDE
License: GPLv2+
Group: Development/Python
Source0: http://heanet.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-%{version}.tar.gz
Source1: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-de-%{version}.tar.gz
Source2: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-fr-%{version}.tar.gz
Source3: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-ru-%{version}.tar.gz
Source4: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-cs-%{version}.tar.gz
Source5: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-es-%{version}.tar.gz
Source6: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-tr-%{version}.tar.gz
Source7: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-zh_CN.GB2312-%{version}.tar.gz
Source8: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-it-%{version}.tar.gz
Source9: http://switch.dl.sourceforge.net/project/eric-ide/eric4/stable/%{version}/%{name}4-i18n-en-%{version}.tar.gz
URL: http://eric-ide.python-projects.org/
BuildRequires: qscintilla-qt4-devel 
BuildRequires: python-sip
BuildRequires: python-qt4
BuildRequires: python-qt4-qscintilla
BuildRequires: imagemagick
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
%setup -q -n %{name}4-%version -D -T -b 9

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


%changelog
* Fri Jun 03 2011 Funda Wang <fwang@mandriva.org> 4.4.15-1mdv2011.0
+ Revision: 682542
- update to new version 4.4.15

* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 4.4.14-1
+ Revision: 672652
- update to new version 4.4.14

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 4.4.13-1
+ Revision: 649922
- update to new version 4.4.13

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 4.4.12-1
+ Revision: 636420
- update to new version 4.4.12

* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 4.4.11-1mdv2011.0
+ Revision: 627666
- update to new version 4.4.11

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 4.4.10-2mdv2011.0
+ Revision: 624724
- rebuild

* Sat Dec 04 2010 Funda Wang <fwang@mandriva.org> 4.4.10-1mdv2011.0
+ Revision: 609432
- new version 4.4.10

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 4.4.7-3mdv2011.0
+ Revision: 590860
- rebuild

* Sun Sep 05 2010 Funda Wang <fwang@mandriva.org> 4.4.7-2mdv2011.0
+ Revision: 576149
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 4.4.7-1mdv2011.0
+ Revision: 564824
- update to new version 4.4.7

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 4.4.6-1mdv2011.0
+ Revision: 553649
- update to new version 4.4.6

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 4.4.3-1mdv2010.1
+ Revision: 531400
- update to new version 4.4.3

* Sat Mar 06 2010 Funda Wang <fwang@mandriva.org> 4.4.2-1mdv2010.1
+ Revision: 514912
- update to new version 4.4.2
- update source url

* Sat Feb 06 2010 Funda Wang <fwang@mandriva.org> 4.4.1-2mdv2010.1
+ Revision: 501340
- add it translation

* Sat Feb 06 2010 Funda Wang <fwang@mandriva.org> 4.4.1-1mdv2010.1
+ Revision: 501339
- New version 4.4.1

* Wed Jan 20 2010 Michael Scherer <misc@mandriva.org> 4.4.0-2mdv2010.1
+ Revision: 493984
- fix missing Requires, as pyqt4 was splitted

* Sat Jan 09 2010 Funda Wang <fwang@mandriva.org> 4.4.0-1mdv2010.1
+ Revision: 488109
- New verrsion 4.4.0

* Sat Dec 12 2009 Funda Wang <fwang@mandriva.org> 4.3.10-1mdv2010.1
+ Revision: 477742
- new version 4.3.10

* Mon Nov 09 2009 Frederik Himpe <fhimpe@mandriva.org> 4.3.9-1mdv2010.1
+ Revision: 463630
- update to new version 4.3.9

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 4.3.8-1mdv2010.1
+ Revision: 462593
- update to new version 4.3.8

* Wed Sep 30 2009 Funda Wang <fwang@mandriva.org> 4.3.7.1-3mdv2010.0
+ Revision: 451123
- rebuild
- rebuild

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 4.3.7.1-1mdv2010.0
+ Revision: 443154
- update to new version 4.3.7.1

* Sat Aug 01 2009 Funda Wang <fwang@mandriva.org> 4.3.6-1mdv2010.0
+ Revision: 406435
- new version 4.3.6
- new version 4.3.5
- New version 4.3.4

  + Lev Givon <lev@mandriva.org>
    - Update project web site.

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 4.3.3-1mdv2010.0
+ Revision: 370921
- new version 4.3.3

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 4.3.1-1mdv2009.1
+ Revision: 351648
- New version 4.3.1

* Tue Feb 10 2009 Funda Wang <fwang@mandriva.org> 4.3.0-1mdv2009.1
+ Revision: 339058
- use upstream newer install.py
- New version 4.3.0

* Wed Jan 07 2009 Frederik Himpe <fhimpe@mandriva.org> 4.2.5-1mdv2009.1
+ Revision: 326794
- update to new version 4.2.5

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 4.2.4a-2mdv2009.1
+ Revision: 323368
- rebuild

* Tue Dec 09 2008 Funda Wang <fwang@mandriva.org> 4.2.4a-1mdv2009.1
+ Revision: 312084
- new version 4.2.4a

* Sun Dec 07 2008 Funda Wang <fwang@mandriva.org> 4.2.4-1mdv2009.1
+ Revision: 311619
- new version 4.2.4

* Mon Nov 10 2008 Funda Wang <fwang@mandriva.org> 4.2.3-1mdv2009.1
+ Revision: 301675
- New version 4.2.3

* Sat Oct 11 2008 Frederik Himpe <fhimpe@mandriva.org> 4.2.2a-1mdv2009.1
+ Revision: 291686
- update to new version 4.2.2a

* Sat Aug 09 2008 Funda Wang <fwang@mandriva.org> 4.2.0-1mdv2009.0
+ Revision: 270092
- add destdir patch
- New version 4.2.0

* Thu Aug 07 2008 Frederik Himpe <fhimpe@mandriva.org> 4.1.6-1mdv2009.0
+ Revision: 266886
- update to new version 4.1.6

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.1.5-2mdv2009.0
+ Revision: 266732
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 4.1.5-1mdv2009.0
+ Revision: 216781
- update to new version 4.1.5

* Fri May 23 2008 Frederik Himpe <fhimpe@mandriva.org> 4.1.4-1mdv2009.0
+ Revision: 210716
- update to new version 4.1.4

* Sun May 11 2008 Frederik Himpe <fhimpe@mandriva.org> 4.1.3-2mdv2009.0
+ Revision: 205437
- Use correct image for menu item icon
- Install in /usr/lib too when built on x86_64
- Add menu item and icon

* Mon May 05 2008 Frederik Himpe <fhimpe@mandriva.org> 4.1.3-1mdv2009.0
+ Revision: 201580
- New version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 4.0.4-2mdv2008.1
+ Revision: 171862
- fix update-menus-without-menu-file-in-%%post(|un)
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 15 2007 Funda Wang <fwang@mandriva.org> 4.0.4-1mdv2008.1
+ Revision: 120378
- New version 4.0.4

* Wed Oct 03 2007 Olivier Blin <oblin@mandriva.com> 4.0.1-2mdv2008.0
+ Revision: 95215
- require python-qt4-qscintilla

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 4.0.1-1mdv2008.0
+ Revision: 80204
- New eric with python qt 4

  + Funda Wang <fwang@mandriva.org>
    - fix desktop entry comment

* Thu May 24 2007 Adam Williamson <awilliamson@mandriva.org> 3.9.5-1mdv2008.0
+ Revision: 30588
- correct BuildRequires
- don't dump the entire tarball into the package
- don't own py_puresitedir
- generate fd.o-compliant icons and use in .desktop file
- unpack i18n sources correctly
- use py_puresitedir macro
- 3.9.5 (initial spec from Alex Kurtakov)


* Thu Apr 20 2006 Jerome Martin <jmartin@mandriva.org> 3.8.2-1mdk
- 3.8.2

* Fri Feb 03 2006 Austin Acton <austin@mandriva.org> 3.8.1-1mdk
- New release 3.8.1

* Tue Nov 29 2005 Austin Acton <austin@mandriva.org> 3.8.0-1mdk
- New release 3.8.0

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 3.7.2-1mdk
- New release 3.7.2

* Sat Jul 09 2005 Austin Acton <austin@mandriva.org> 3.7.1-1mdk
- New release 3.7.1

* Sun Jun 05 2005 Austin Acton <austin@mandriva.org> 3.7.0-1mdk
- New release 3.7.0

* Sun Feb 27 2005 Austin Acton <austin@mandrake.org> 3.6.2-2mdk
- remove all referneces to buildroot (thanks Jim Lawton)

* Sun Feb 20 2005 Austin Acton <austin@mandrake.org> 3.6.2-1mdk
- 3.6.2

* Mon Jan 24 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.6.0-1mdk
- 3.6.0
- install translations

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 3.5.1-2mdk
- Rebuild for new python

* Sun Nov 28 2004 Austin Acton <austin@mandrake.org> 3.5.1-1mdk
- 3.5.1
- source URL

* Mon Sep 27 2004 Austin Acton <austin@mandrake.org> 3.4.2-1mdk
- 3.4.2
- new menu

* Sun May 02 2004 Austin Acton <austin@mandrake.org> 3.4.1-1mdk
- 3.4.1

* Wed Feb 18 2004 David Baudens <baudens@mandrakesoft.com> 3.3.1-2mdk
- Fix icon

* Wed Dec 31 2003 Austin Acton <austin@linux.ca> 3.3.1-1mdk
- 3.3.1

* Sat Dec 06 2003 Austin Acton <austin@linux.ca> 3.3-1mdk
- 3.3

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.1-2mdk
- rebuild for new python
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install

* Thu May 01 2003 Austin Acton <aacton@yorku.ca> 3.1-1mdk
- from Jérôme Martin <jerome.f.martin@free.fr>:
  - Initial version
- add menu entry

