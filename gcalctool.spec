%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME desktop calculator
Name:		gcalctool
Version:	6.6.2
Release:	3
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://calctool.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
gcalctool is a desktop calculator.
It has Basic, Financial and Scientific modes. Internally it uses multiple
precision arithmetic to produce results to a high degree of accuracy.

%prep
%setup -q

%build
%configure2_5x \
	--with-gtk=3.0

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS 
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.gcalctool.gschema.xml
%{_mandir}/man1/*

