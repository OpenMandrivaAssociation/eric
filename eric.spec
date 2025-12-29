%undefine _debugsource_packages
%define oname %{name}7

Name:		eric
Version:	25.12
Release:	3
Summary:	Full featured Python and Ruby editor and IDE
License:	GPLv2+
Group:		Development/Python
URL:		https://eric-ide.python-projects.org/
# URL:      https://sourceforge.net/projects/eric-ide
Source0:	https://downloads.sourceforge.net/project/eric-ide/eric7/%{version}/eric7-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	appstream-util
# From pyqt6BaseModulesList
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	desktop-file-utils
BuildRequires:	fdupes
BuildRequires:	hicolor-icon-theme
BuildRequires:	pkgconfig(python)
BuildRequires:	python-qt6-devel
BuildRequires:	python-qt6-pdf
BuildRequires:	python-qt6-svg-widgets
# Anything commented out is needed from BuildRequires:
BuildRequires:	python%{pyver}dist(asttokens)
BuildRequires:	python%{pyver}dist(black)
BuildRequires:	python%{pyver}dist(chardet)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(cyclonedx-bom)
BuildRequires:	python%{pyver}dist(docutils)
BuildRequires:	python%{pyver}dist(editorconfig)
BuildRequires:	python%{pyver}dist(esprima)
BuildRequires:	python%{pyver}dist(fido2)
BuildRequires:	python%{pyver}dist(isort)
BuildRequires:	python%{pyver}dist(jedi)
BuildRequires:	python%{pyver}dist(markdown)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(parso)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pipdeptree)
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(pyenchant)
BuildRequires:	python%{pyver}dist(pyqt6-charts)
BuildRequires:	python%{pyver}dist(pyqt6-graphs)
BuildRequires:	python%{pyver}dist(pyqt6-qscintilla)
BuildRequires:	python%{pyver}dist(pyqt6-webengine)
BuildRequires:	python%{pyver}dist(pyusb)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(semver)
BuildRequires:	python%{pyver}dist(sip)
BuildRequires:	python%{pyver}dist(spdx-license-list)
BuildRequires:	python%{pyver}dist(tomlkit)
BuildRequires:	python%{pyver}dist(trove-classifiers)
BuildRequires:	python%{pyver}dist(watchdog)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	python%{pyver}dist(pip)
Requires:	python%{pyver}dist(pyqt6-charts)
Requires:	python%{pyver}dist(pyqt6-graphs)
Requires:	python%{pyver}dist(pyqt6-qscintilla)
Requires:	python%{pyver}dist(pyqt6-webengine)
Requires:	python-qt6-help
Requires:	python-qt6-pdf
# From requiredModulesList
Requires:	python%{pyver}dist(asttokens)
Requires:	python%{pyver}dist(black)
Requires:	python%{pyver}dist(coverage)
Requires:	python%{pyver}dist(cyclonedx-bom)
Requires:	python%{pyver}dist(editorconfig)
Requires:	python%{pyver}dist(isort)
Requires:	python%{pyver}dist(jedi)
Requires:	python%{pyver}dist(markdown)
Requires:	python%{pyver}dist(packaging)
Requires:	python%{pyver}dist(parso)
Requires:	python%{pyver}dist(pipdeptree)
Requires:	python%{pyver}dist(psutil)
Requires:	python%{pyver}dist(pygments)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(semver)
Requires:	python%{pyver}dist(spdx-license-list)
Requires:	python%{pyver}dist(tomlkit)
Requires:	python%{pyver}dist(trove-classifiers)
Requires:	python%{pyver}dist(watchdog)
# From optionalModulesList
Recommends:		python%{pyver}dist(chardet)
Recommends:		python%{pyver}dist(docutils)
Recommends:		python%{pyver}dist(esprima)
Recommends:		python%{pyver}dist(fido2)
Recommends:		python%{pyver}dist(markdown)
Recommends:		python%{pyver}dist(pyenchant)
Recommends:		python%{pyver}dist(pyusb)
Recommends:		python%{pyver}dist(pyyaml)
Recommends:		python%{pyver}dist(wheel)
# External tools
Recommends:		pyside6-devel
Recommends:		qt6-qttools-assistant
Recommends:		qt6-qttools-designer
Recommends:		qt6-qttools-doc
Recommends:		qt6-qttools-linguist
Recommends:		git-core
Recommends:		mercurial
Recommends:		subversion
# Additional provides
Provides:	%{oname} = %{version}-%{release}

%description
Eric is a full featured Python and Ruby editor and IDE, written in python. It
is based on the cross platform Qt gui toolkit, integrating the highly flexible
Scintilla editor control. It is designed to be usable as everdays' quick and
dirty editor as well as being usable as a professional project management tool
integrating many advanced features Python offers the professional coder.

%prep
%autosetup -n %{oname}-%{version} -p1
# sed the correct interpreter in this order.
find . -name \*.py -exec sed -i -e 's@#!/usr/bin/env python3@#!/usr/bin/python3@g' '{}' \;
find . -name \*.py -exec sed -i -e 's@#!/usr/bin/env python@#!/usr/bin/python3@g' '{}' \;

%build
# nothing to do

%install
python install.py \
    -i %{buildroot} \
    -b %{_bindir} \
    -d %{python_sitelib} \
    -a %{_qtdir}/qsci/api \
    -z

# non-standard category
desktop-file-edit --remove-category=MicroPython %{buildroot}%{_datadir}/applications/eric7_mpy.desktop

# duplicate files
rm -fv  %{buildroot}%{_datadir}/appdata/eric7.appdata.xml
rm -fv  %{buildroot}%{python_sitelib}/eric7/LICENSE.txt
# deprecated icons
rm -rfv %{buildroot}%{_datadir}/icons/eric*

# Make sure these files are marked executable
chmod a+x %{buildroot}%{python_sitelib}/%{oname}/%{oname}_*.py
chmod a+x %{buildroot}%{python_sitelib}/%{oname}/{MicroPython/Tools/uf2conv,PipInterface/pipcleanup,PipInterface/piplicenses,Plugins/CheckerPlugins/CodeStyleChecker/pycodestyle,Plugins/VcsPlugins/vcsMercurial/HisteditExtension/HgHisteditEditor,Tools/webBrowserSupport,UI/upgrader}.py

# insert missing shebangs
sed -i -e '1i#!/usr/bin/python3' %{buildroot}%{python_sitelib}/eric7config.py %{buildroot}%{python_sitelib}/%{oname}/eric7_mpy.py
chmod a+x %{buildroot}%{python_sitelib}/eric7config.py

# find dupes
%fdupes %{buildroot}%{python_sitelib}/%{oname}
# find i18n
%find_lang %{name} --with-qt --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/eric7.appdata.xml
test "$(grep '^Exec' %{buildroot}%{_datadir}/applications/eric7_ide.desktop)" = "Exec=%{_bindir}/eric7_ide"
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_browser.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_ide.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_mpy.desktop

%files -f %{name}.lang
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/eric*.png
%{_metainfodir}/%{oname}.appdata.xml
%{python_sitelib}/%{oname}/*.py
%{python_sitelib}/%{oname}/*.pyw
%{python_sitelib}/%{oname}/icons
%{python_sitelib}/%{oname}/pixmaps
%{python_sitelib}/%{oname}/[A-Z]*/
%{python_sitelib}/%{oname}/*.ekj
%{python_sitelib}/%{oname}/*.json
%{python_sitelib}/%{oname}plugins/
%{python_sitelib}/%{oname}config.py*
%{_qtdir}/qsci/api/*/*
