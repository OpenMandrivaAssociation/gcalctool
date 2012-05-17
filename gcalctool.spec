Summary: GNOME desktop calculator
Name: gcalctool
Version: 6.4.2.1
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://calctool.sourceforge.net/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

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
for l in C bg ca cs de el es eu fi fr gl hu it ja ko lv oc pt_BR ru sl sv te zh_CN zh_HK zh_TW; do
	echo "%%dir %%{_datadir}/help/$l"
	echo "%%lang($l) %%{_datadir}/help/$l/%%{name}"
done >> %{name}.lang

%files -f %{name}.lang
%doc README NEWS AUTHORS 
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.gcalctool.gschema.xml
%{_mandir}/man1/*

