%define _disable_ld_no_undefined 1

Summary:	X.org driver for Number Nine chipsets
Name:		x11-driver-video-i128
Version:	1.3.6
Release:	15
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-i128-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-i128 is the X.org driver for Number Nine chipsets.

%prep
%setup -qn xf86-video-i128-%{version}
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/i128_drv.so
%{_mandir}/man4/i128.*

