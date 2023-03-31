%global debug_package %{nil}
%define oname %{name}6

Name:		eric
Version:	20.9
Release:	2
Summary:	Full featured Python and Ruby editor and IDE
License:	GPLv2+
Group:		Development/Python
URL:		http://eric-ide.python-projects.org/
Source0:	https://sourceforge.net/projects/eric-ide/files/%{oname}/stable/%{version}/%{oname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-sip
BuildRequires:	python-qt5-devel
BuildRequires:	python-qt5-qscintilla
BuildRequires:	python-qt5-chart
BuildRequires:	python-qt5-webengine
BuildRequires:	python-qt5-webengine-widgets
BuildRequires:	qscintilla-qt5-devel
BuildRequires:	qt5-qtbase-macros
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
Requires:	python-qt5-qscintilla
Requires:	python-qt5-chart
Requires:	python-qt5-webengine
Requires:	python-qt5-webengine-widgets

%description
Eric is a full featured Python and Ruby editor and IDE, written in python. It
is based on the cross platform Qt gui toolkit, integrating the highly flexible
Scintilla editor control. It is designed to be usable as everdays' quick and
dirty editor as well as being usable as a professional project management tool
integrating many advanced features Python offers the professional coder.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
# nothingg to do

%install
python install.py \
    -i %{buildroot} \
    -b %{_bindir} \
    -d %{python_sitelib} \
    -a %{_qt5_datadir}/qsci/api \
    -z

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{128x128,64x64,48x48,32x32,16x16}/apps

convert -scale 128 %{buildroot}%{_datadir}/pixmaps/eric.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/eric.png
convert -scale 64 %{buildroot}%{_datadir}/pixmaps/eric.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/eric.png
convert -scale 48 %{buildroot}%{_datadir}/pixmaps/eric.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/eric.png
convert -scale 32 %{buildroot}%{_datadir}/pixmaps/eric.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/eric.png
convert -scale 16 %{buildroot}%{_datadir}/pixmaps/eric.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/eric.png
convert -scale 48 %{buildroot}%{_datadir}/pixmaps/ericWeb.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/ericWeb.png
convert -scale 32 %{buildroot}%{_datadir}/pixmaps/ericWeb.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/ericWeb.png
convert -scale 16 %{buildroot}%{_datadir}/pixmaps/ericWeb.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/ericWeb.png

# deprecated icons
rm -rf %{buildroot}%{_datadir}/pixmaps

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%doc eric/docs/{changelog,README.rst,THANKS}
%license eric/docs/LICENSE.GPL3
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/eric*.png
%{_metainfodir}/%{oname}.appdata.xml
%{python_sitelib}/__pycache__/eric6config.cpython-*.pyc
%{python_sitelib}/%{oname}/
%{python_sitelib}/%{oname}plugins/
%{python_sitelib}/%{oname}config.py*
%{_qt5_datadir}/qsci/api/*/*
