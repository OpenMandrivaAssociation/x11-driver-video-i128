Name: x11-driver-video-i128
Version: 1.2.1
Release: %mkrel 3
Summary: The X.org driver for Number Nine chipsets
Group: System/X11

########################################################################
# git clone git//git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-i128  xorg/drivers/xf86-video-i128
# cd xorg/drivers/xf86-video/i128
# git-archive --format=tar --prefix=xf86-video-i128-1.2.1/ master | bzip2 -9 > xf86-video-i128-1.2.1.tar.bz2
########################################################################
Source0: xf86-video-i128-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Number Nine chipsets

%prep
%setup -q -n xf86-video-i128-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/i128_drv.la
%{_libdir}/xorg/modules/drivers/i128_drv.so
%{_mandir}/man4/i128.*


