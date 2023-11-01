%undefine _debugsource_packages
%define oname %{name}7

Name:		eric
Version:	23.11
Release:	1
Summary:	Full featured Python and Ruby editor and IDE
License:	GPLv2+
Group:		Development/Python
URL:		http://eric-ide.python-projects.org/
Source0:	https://downloads.sourceforge.net/project/eric-ide/eric7/%{version}/eric7-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-sip
BuildRequires:	python-qt6-devel
BuildRequires:	python-qt6-webengine
BuildRequires:	python-qt6-qscintilla
BuildRequires:	python-qt6-svg-widgets
BuildRequires:	python-qt6-pdf
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	desktop-file-utils
Requires:	python-qt6-webengine
Requires:	python-qt6-qscintilla
Requires:	python-qt6-svg-widgets
Requires:	python-qt6-help
Requires:	python-qt6-pdf

%description
Eric is a full featured Python and Ruby editor and IDE, written in python. It
is based on the cross platform Qt gui toolkit, integrating the highly flexible
Scintilla editor control. It is designed to be usable as everdays' quick and
dirty editor as well as being usable as a professional project management tool
integrating many advanced features Python offers the professional coder.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
# nothing to do

%install
python install.py \
    -i %{buildroot} \
    -b %{_bindir} \
    -d %{python_sitelib} \
    -a %{_qtdir}/qsci/api \
    -z

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/eric*.png
%{_datadir}/icons/*.png
%{_metainfodir}/%{oname}.appdata.xml
%{python_sitelib}/%{oname}/
%{python_sitelib}/%{oname}plugins/
%{python_sitelib}/%{oname}config.py*
%{_qtdir}/qsci/api/*/*
