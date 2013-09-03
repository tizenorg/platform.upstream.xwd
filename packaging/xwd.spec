Summary: dump an image of an X Window
Name: xwd
# NOTE: The package version should be set to the X11 major release from which
# the OS release is based upon.
Version: 1.0.6
Release: 1
License: MIT
Group: User Interface/X
URL: http://www.x.org

Source: %{name}-%{version}.tar.gz

#Source2:  ftp://ftp.x.org/pub/individual/app/xwd-1.0.4.tar.bz2

BuildRequires: autoconf automake

#BuildRequires: xorg-x11-xutils-dev
# xfd needs gettext
BuildRequires: gettext
BuildRequires: zlib-devel
BuildRequires: libfontenc-devel
BuildRequires: libX11-devel
BuildRequires: libXmu-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel
BuildRequires: libXaw-devel
BuildRequires: libXpm-devel
BuildRequires: libXft-devel
BuildRequires: libXrender-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXcursor-devel
BuildRequires: libpng-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel >= 1.2
BuildRequires: libXxf86vm-devel
BuildRequires: xorg-x11-xbitmaps

Provides: xwd

%description
X Window System window dumping utility.  Xwd allows X users to store
window  images in a specially formatted dump file.  This file can then be read
by various other X utilities for redisplay, printing, editing, formatting, ar‐
chiving, image processing, etc.  The target window is selected by clicking the
pointer in the desired window.  The keyboard bell is rung once at  the  begin‐
ning of the dump and twice when the dump is completed.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}

{
	make install DESTDIR=$RPM_BUILD_ROOT
}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
/usr/share/license/%{name}
#%{_bindir}/xwd
