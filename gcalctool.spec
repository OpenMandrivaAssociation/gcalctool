Summary: GNOME desktop calculator
Name: gcalctool
Version: 6.0.1
Release: %mkrel 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://calctool.sourceforge.net/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel >= 2.21.8
BuildRequires: glib2-devel >= 2.25.10
BuildRequires: libxml2-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: intltool
Conflicts: gnome-utils < 2.3.3

%description
gcalctool is a desktop calculator.
It has Basic, Financial and Scientific modes. Internally it uses multiple
precision arithmetic to produce results to a high degree of accuracy.

%prep
%setup -q

%build
%configure2_5x --with-gtk=2.0
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README NEWS AUTHORS 
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/%name
%_datadir/glib-2.0/schemas/org.gnome.gcalctool.gschema.xml
