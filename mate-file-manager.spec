%define major		1
%define girmajor	2.0
%define libname	%mklibname caja-extension %{major}
%define girname %mklibname caja-gir %{girmajor}
%define devname	%mklibname -d caja-extension

Summary:	File manager for the MATE desktop environment
Name:		mate-file-manager
Version:	1.4.0
Release:	1
Group:		File tools
License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(pangox)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(unique-1.0)

Requires(post,postun):	shared-mime-info
Requires(post,postun):	desktop-file-utils

%description
Mate-file-manager is an excellent file manager for the MATE desktop 
environment.

%package -n %{libname}
Summary:	Libraries for Mate File manager
Group:		System/Libraries

%description -n %{libname}
This package contains library used by %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for developing mate-file-manager components
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n %{devname}
This package provides the necessary development libraries and include 
files to allow you to develop mate-file-manager components.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-update-mimedb \
	--disable-schemas-compile

%make LIBS='-lm -lgmodule-2.0'

%install
%makeinstall_std
find %{buildroot} -name "*.la" -exec rm -rf {} \;

mkdir -p %{buildroot}%{_localstatedir}/lib/gnome/desktop \
	%{buildroot}%{_datadir}/mate-file-manager/default-desktop \
	%{buildroot}%{_libdir}/mate-file-manager/extensions-2.0

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc README NEWS HACKING AUTHORS MAINTAINERS
%dir %{_localstatedir}/lib/gnome/desktop
%dir %{_localstatedir}/lib/gnome/
%{_sysconfdir}/mateconf/schemas/apps_caja_preferences.schemas
%{_bindir}/*
%{_libexecdir}/caja-convert-metadata
%dir %{_libdir}/mate-file-manager
%{_datadir}/applications/*
%dir %{_datadir}/caja
%{_datadir}/caja/*
%dir %{_datadir}/mate-file-manager
%{_datadir}/mate-file-manager/*
%{_datadir}/mime/packages/caja.xml
%dir %{_datadir}/pixmaps/caja
%{_datadir}/pixmaps/caja/*
%{_iconsdir}/hicolor/*/apps/caja.*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libcaja-extension.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Caja-%{girmajor}.typelib

%files -n %{devname}
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Caja-%{girmajor}.gir
%doc %{_datadir}/gtk-doc/html/libcaja-extension



%changelog
* Thu Aug 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811606
- new version 1.4.0

* Fri Jun 01 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.2-1
+ Revision: 801825
- imported package mate-file-manager

