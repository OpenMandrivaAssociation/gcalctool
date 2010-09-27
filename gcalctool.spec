Summary: GNOME desktop calculator
Name: gcalctool
Version: 5.32.0
Release: %mkrel 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://calctool.sourceforge.net/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: gcalctool-32.png
Source2: gcalctool-16.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel
BuildRequires: glib2-devel >= 2.25
BuildRequires: libGConf2-devel
BuildRequires: libsoup-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: intltool
#gw libtool dep:
BuildRequires: dbus-glib-devel
#gw if we call aclocal
BuildRequires: automake
BuildRequires: gnome-common
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Conflicts: gnome-utils < 2.3.3

%description
gcalctool is a desktop calculator.
It has Basic, Financial and Scientific modes. Internally it uses multiple
precision arithmetic to produce results to a high degree of accuracy.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

%find_lang %{name} --with-gnome
#for omf in %buildroot%_datadir/omf/*/{*-??.omf,*-??_??.omf};do
#echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
#done

mkdir -p %buildroot{%_liconsdir,%_miconsdir,%_iconsdir}
install -m 644 %SOURCE1 %buildroot%_iconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_miconsdir/%name.png
#gw this is in the gnome-icon-theme package
ln -s %{_datadir}/icons/hicolor/48x48/apps/gnome-calculator.png %buildroot%{_liconsdir}/%name.png

rm -rf %buildroot/var/lib/scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT


%post
touch %{_datadir}/gnome/help/gcalctool/C/gcalctool.html

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README NEWS AUTHORS 
#TODO
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
#%dir %{_datadir}/omf/%{name}
#%{_datadir}/omf/%{name}/%{name}-C.omf
%{_datadir}/%name
%_datadir/glib-2.0/schemas/org.gnome.gcalctool.gschema.xml
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
