Name: x11-driver-video-i128
Version: 1.3.6
Release: 2
Summary: X.org driver for Number Nine chipsets
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-i128-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-i128 is the X.org driver for Number Nine chipsets.

%prep
%setup -qn xf86-video-i128-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/i128_drv.so
%{_mandir}/man4/i128.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.6-1
+ Revision: 810711
- version update 1.3.6

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.5-1
+ Revision: 786708
- version update 1.3.5

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.3.4-7
+ Revision: 748417
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.4-6
+ Revision: 703795
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.3.4-5
+ Revision: 683575
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-4
+ Revision: 671150
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.4-3mdv2011.0
+ Revision: 595743
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Aug 17 2010 Thierry Vignaud <tv@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 570773
- new release

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3.3-1mdv2010.0
+ Revision: 407725
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.2-1mdv2010.0
+ Revision: 391864
- update to version 1.3.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.3.1-3mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.3.1-2mdv2009.1
+ Revision: 308216
- rebuild for new X server

* Fri Sep 05 2008 Thierry Vignaud <tv@mandriva.org> 1.3.1-1mdv2009.0
+ Revision: 281097
- new release

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-2mdv2009.0
+ Revision: 265921
- rebuild early 2009.0 package (before pixel changes)
- improved description
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.3.0-1mdv2009.0
+ Revision: 194197
- Update to version 1.3.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.1-5mdv2008.1
+ Revision: 165564
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.1-4mdv2008.1
+ Revision: 156606
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.1-3mdv2008.1
+ Revision: 154858
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to generate tar file from existing tag xf86-video-i128-1.2.1, but
  don't move mandriva branch point, and add patches to reach there.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.1-2mdv2008.1
+ Revision: 98693
- minor spec cleanup
- build against new xserver (1.4)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

