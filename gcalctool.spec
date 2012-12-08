Summary: GNOME desktop calculator
Name: gcalctool
Version: 6.5.91
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
#for l in C bg ca cs de el es eu fi fr gl hu it ja ko lv oc pt_BR ru sl sv te zh_CN zh_HK zh_TW; do
#	echo "%%lang($l) %%{_datadir}/help/$l/%%{name}"
#done >> %{name}.lang

%files -f %{name}.lang
%doc README NEWS AUTHORS 
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.gcalctool.gschema.xml
%{_mandir}/man1/*



%changelog
* Thu May 17 2012 Matthew Dawkins <mattydaw@mandriva.org> 6.4.2.1-1
+ Revision: 799376
- update to new version 6.4.2.1

* Fri May 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 6.4.1.1-1
+ Revision: 796154
- new version 6.4.1.1
- gtk3 build

* Tue May 24 2011 Götz Waschk <waschk@mandriva.org> 6.0.2-1
+ Revision: 678058
- new version

* Wed Apr 27 2011 Funda Wang <fwang@mandriva.org> 6.0.1-1
+ Revision: 659519
- update to new version 6.0.1

* Mon Apr 04 2011 Funda Wang <fwang@mandriva.org> 6.0.0-1
+ Revision: 650172
- new version 6.0.0

* Tue Nov 23 2010 Götz Waschk <waschk@mandriva.org> 5.32.2-1mdv2011.0
+ Revision: 599911
- update to new version 5.32.2

* Mon Nov 15 2010 Götz Waschk <waschk@mandriva.org> 5.32.1-1mdv2011.0
+ Revision: 597755
- update to new version 5.32.1

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 5.32.0-1mdv2011.0
+ Revision: 581287
- update to new version 5.32.0

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 5.31.91-1mdv2011.0
+ Revision: 574276
- update to new version 5.31.91

* Mon Aug 16 2010 Götz Waschk <waschk@mandriva.org> 5.31.90-1mdv2011.0
+ Revision: 570278
- update to new version 5.31.90

* Tue Aug 03 2010 Götz Waschk <waschk@mandriva.org> 5.31.6-1mdv2011.0
+ Revision: 565391
- update to new version 5.31.6

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 5.31.5-1mdv2011.0
+ Revision: 563578
- new version
- bump deps

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 5.30.2-1mdv2011.0
+ Revision: 550703
- update to new version 5.30.2

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 5.30.1-1mdv2010.1
+ Revision: 538832
- new version
- drop patch

* Wed Apr 07 2010 Frederic Crozat <fcrozat@mandriva.com> 5.30.0-2mdv2010.1
+ Revision: 532745
- Fix buildrequires
- Patch0 (GIT): fix untranslated UI (Mdv bug #58491)

* Mon Mar 29 2010 Funda Wang <fwang@mandriva.org> 5.30.0-1mdv2010.1
+ Revision: 528711
- update to new version 5.30.0

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 5.29.92-1mdv2010.1
+ Revision: 516900
- update to new version 5.29.92

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 5.29.91-1mdv2010.1
+ Revision: 509417
- new version
- update file list

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 5.29.90-1mdv2010.1
+ Revision: 502596
- update to new version 5.29.90

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 5.29.6-1mdv2010.1
+ Revision: 496636
- update to new version 5.29.6

* Tue Dec 22 2009 Götz Waschk <waschk@mandriva.org> 5.29.4-1mdv2010.1
+ Revision: 481217
- update to new version 5.29.4
- update build deps
- update to new version 5.29.2

* Wed Oct 21 2009 Frederic Crozat <fcrozat@mandriva.com> 5.28.1-1mdv2010.0
+ Revision: 458606
- Release 5.28.1

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 5.28.0-2mdv2010.0
+ Revision: 454761
- do not package huge ChangeLog

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 5.28.0-1mdv2010.0
+ Revision: 447185
- update to new version 5.28.0

* Mon Sep 07 2009 Götz Waschk <waschk@mandriva.org> 5.27.92-1mdv2010.0
+ Revision: 432539
- update to new version 5.27.92

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 5.27.91-1mdv2010.0
+ Revision: 421334
- update to new version 5.27.91

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 5.27.90-1mdv2010.0
+ Revision: 414927
- update to new version 5.27.90

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 5.27.5-1mdv2010.0
+ Revision: 401402
- update to new version 5.27.5

* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 5.27.4-1mdv2010.0
+ Revision: 395827
- update to new version 5.27.4

* Tue Jun 16 2009 Götz Waschk <waschk@mandriva.org> 5.27.3-1mdv2010.0
+ Revision: 386289
- update to new version 5.27.3

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 5.27.2-1mdv2010.0
+ Revision: 379501
- new version
- remove TODO

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 5.27.1-1mdv2010.0
+ Revision: 374174
- new version
- update build deps

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 5.26.1-1mdv2009.1
+ Revision: 366974
- update to new version 5.26.1

* Tue Mar 17 2009 Funda Wang <fwang@mandriva.org> 5.26.0-1mdv2009.1
+ Revision: 356457
- New version 5.26.0

* Tue Mar 03 2009 Götz Waschk <waschk@mandriva.org> 5.25.92-1mdv2009.1
+ Revision: 347630
- update to new version 5.25.92

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 5.25.91-1mdv2009.1
+ Revision: 341246
- update to new version 5.25.91

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 5.25.90-1mdv2009.1
+ Revision: 336703
- update to new version 5.25.90

* Mon Jan 19 2009 Funda Wang <fwang@mandriva.org> 5.25.5-1mdv2009.1
+ Revision: 331083
- New version 5.25.5

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 5.25.4-1mdv2009.1
+ Revision: 325239
- update to new version 5.25.4

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 5.25.3-1mdv2009.1
+ Revision: 315789
- update to new version 5.25.3

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 5.25.2-1mdv2009.1
+ Revision: 308993
- update to new version 5.25.2

* Tue Nov 04 2008 Götz Waschk <waschk@mandriva.org> 5.25.1-1mdv2009.1
+ Revision: 299789
- update to new version 5.25.1

* Mon Oct 20 2008 Götz Waschk <waschk@mandriva.org> 5.24.1-1mdv2009.1
+ Revision: 295493
- fix build deps
- update to new version 5.24.1

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 5.24.0-1mdv2009.0
+ Revision: 286808
- new version

* Sun Sep 07 2008 Götz Waschk <waschk@mandriva.org> 5.23.92-1mdv2009.0
+ Revision: 282278
- new version

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 5.23.91-1mdv2009.0
+ Revision: 278408
- new version

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 5.23.90-1mdv2009.0
+ Revision: 273606
- new version

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 5.23.6-1mdv2009.0
+ Revision: 263651
- New version 5.23.6

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 5.23.5-1mdv2009.0
+ Revision: 240073
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 5.23.4-1mdv2009.0
+ Revision: 231022
- new version

* Sun Jun 29 2008 Götz Waschk <waschk@mandriva.org> 5.22.3-1mdv2009.0
+ Revision: 230068
- new version

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - use %%update_scrollkeeper/%%clean_scrollkeeper
    - use %%preun_uninstall_gconf_schemas
    - use %%post_install_gconf_schemas/%%preun_uninstall_gconf_schemas

* Wed May 28 2008 Götz Waschk <waschk@mandriva.org> 5.22.2-1mdv2009.0
+ Revision: 212327
- new version
- drop patch
- fix buildrequires

* Sun Apr 20 2008 Frederik Himpe <fhimpe@mandriva.org> 5.22.1-2mdv2009.0
+ Revision: 195866
- Add patch0 from Fedora: fix fortify abortion when clicking on first number
- New license policy

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 5.22.1-1mdv2009.0
+ Revision: 192465
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 5.22.0-1mdv2008.1
+ Revision: 183570
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 5.21.92-1mdv2008.1
+ Revision: 174558
- new version

* Mon Feb 11 2008 Götz Waschk <waschk@mandriva.org> 5.21.91-1mdv2008.1
+ Revision: 165344
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 5.21.90-1mdv2008.1
+ Revision: 159182
- new version

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 5.21.5-1mdv2008.1
+ Revision: 151583
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 5.21.4-1mdv2008.1
+ Revision: 130072
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - drop old menu

* Tue Dec 04 2007 Götz Waschk <waschk@mandriva.org> 5.21.3-1mdv2008.1
+ Revision: 115197
- new version

* Tue Nov 13 2007 Götz Waschk <waschk@mandriva.org> 5.21.2-1mdv2008.1
+ Revision: 108525
- new version

* Mon Oct 29 2007 Götz Waschk <waschk@mandriva.org> 5.21.1-1mdv2008.1
+ Revision: 102928
- new version
- update file list
- update buildrequires

* Tue Oct 09 2007 Götz Waschk <waschk@mandriva.org> 5.21.0-1mdv2008.1
+ Revision: 95772
- new version

* Tue Oct 02 2007 Götz Waschk <waschk@mandriva.org> 5.20.1-1mdv2008.0
+ Revision: 94419
- new version

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 5.20.0-1mdv2008.0
+ Revision: 89203
- new version

* Mon Sep 03 2007 Götz Waschk <waschk@mandriva.org> 5.19.92-1mdv2008.0
+ Revision: 78657
- new version

* Mon Aug 27 2007 Götz Waschk <waschk@mandriva.org> 5.19.91-1mdv2008.0
+ Revision: 71972
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 5.19.90-1mdv2008.0
+ Revision: 63027
- new version

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 5.19.6-1mdv2008.0
+ Revision: 56520
- new version

* Sun Jul 08 2007 Götz Waschk <waschk@mandriva.org> 5.19.5-1mdv2008.0
+ Revision: 49884
- new version

* Mon Jun 18 2007 Götz Waschk <waschk@mandriva.org> 5.19.4-1mdv2008.0
+ Revision: 40932
- new version
- fix buildrequires
- new version

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 5.9.14-1mdv2007.1
+ Revision: 141866
- new version

* Sun Feb 25 2007 Götz Waschk <waschk@mandriva.org> 5.9.13-1mdv2007.1
+ Revision: 125675
- new version

* Mon Feb 12 2007 Götz Waschk <waschk@mandriva.org> 5.9.12-1mdv2007.1
+ Revision: 120015
- new version

* Mon Jan 22 2007 Götz Waschk <waschk@mandriva.org> 5.9.11-1mdv2007.1
+ Revision: 111956
- new version

* Mon Dec 18 2006 Götz Waschk <waschk@mandriva.org> 5.9.9-1mdv2007.1
+ Revision: 98394
- new version

* Tue Dec 05 2006 Götz Waschk <waschk@mandriva.org> 5.9.8-1mdv2007.1
+ Revision: 90723
- new version

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 5.9.7-2mdv2007.1
+ Revision: 87909
- bot rebuild
- new version

* Thu Nov 02 2006 Götz Waschk <waschk@mandriva.org> 5.8.25-1mdv2007.1
+ Revision: 75992
- Import gcalctool

* Thu Nov 02 2006 Götz Waschk <waschk@mandriva.org> 5.8.25-1mdv2007.1
- New version 5.8.25

* Tue Sep 05 2006 Götz Waschk <waschk@mandriva.org> 5.8.24-1mdv2007.0
- New release 5.8.24

* Sat Aug 19 2006 Frederic Crozat <fcrozat@mandriva.com> 5.8.23-1mdv2007.0
- Release 5.8.23

* Tue Aug 08 2006 Götz Waschk <waschk@mandriva.org> 5.8.20-1mdv2007.0
- New release 5.8.20

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 5.8.19-2mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 5.8.19-1
- New release 5.8.19

* Tue Jul 11 2006 G�tz Waschk <waschk@mandriva.org> 5.8.17-1mdv2007.0
- xdg menu
- New release 5.8.17

* Sat Jun 10 2006 Götz Waschk <waschk@mandriva.org> 5.8.16-1
- New release 5.8.16

* Sun Jun 04 2006 G�tz Waschk <waschk@mandriva.org> 5.8.13-2mdv2007.0
- fix buildrequires

* Sat Jun 03 2006 Frederic Crozat <fcrozat@mandriva.com> 5.8.13-1mdv2007.0
- Release 5.8.13

* Sat Apr 29 2006 Frederic Crozat <fcrozat@mandriva.com> 5.7.32-2mdk
- Rebuild

* Wed Apr 19 2006 Frederic Crozat <fcrozat@mandriva.com> 5.7.32-1mdk
- Release 5.7.32

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 5.6.31-3mdk
- Use mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 5.6.31-2mdk
- Rebuild

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 5.6.31-1mdk
- Release 5.6.31

* Sun May 22 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 5.5.42-6mdk
- add BuildRequires: automake1.8

* Fri May 20 2005 G�tz Waschk <waschk@mandriva.org> 5.5.42-5mdk
- fix URL (Gaetan Lehmann)

* Fri May 20 2005 G�tz Waschk <waschk@mandriva.org> 5.5.42-4mdk
- fix buildrequires

* Wed May 04 2005 G�tz Waschk <waschk@mandriva.org> 5.5.42-3mdk
- fix build on x86_64

* Wed Apr 20 2005 G�tz Waschk <waschk@mandriva.org> 5.5.42-2mdk
- fix buildrequires

* Wed Apr 20 2005 Frederic Crozat <fcrozat@mandriva.com> 5.5.42-1mdk 
- Release 5.5.42 (based on G�tz Waschk package)

* Thu Jan 13 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 4.4.22-1mdk
- New release 4.4.22

* Wed Oct 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 4.4.20-1mdk
- New release 4.4.20

* Wed Jul 14 2004 G�tz Waschk <waschk@linux-mandrake.com> 4.3.51-3mdk
- fix menu conflict with X11R6-contrib

* Thu Jun 10 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 4.3.51-2mdk
- Revert to 4.3.51 (4.4.8 is not 2.6 material)

* Wed Jun 09 2004 G�tz Waschk <waschk@linux-mandrake.com> 4.4.8-1mdk
- fix icon
- adapt file list
- New release 4.4.8

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 4.3.51-1mdk
- New release 4.3.51

