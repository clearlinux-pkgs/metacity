#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : metacity
Version  : 3.50.0
Release  : 35
URL      : https://download.gnome.org/sources/metacity/3.50/metacity-3.50.0.tar.xz
Source0  : https://download.gnome.org/sources/metacity/3.50/metacity-3.50.0.tar.xz
Summary  : Metacity library
Group    : Development/Tools
License  : GPL-2.0
Requires: metacity-bin = %{version}-%{release}
Requires: metacity-data = %{version}-%{release}
Requires: metacity-lib = %{version}-%{release}
Requires: metacity-license = %{version}-%{release}
Requires: metacity-locales = %{version}-%{release}
Requires: metacity-man = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : libgtop-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(xpresent)
BuildRequires : pkgconfig(xres)
BuildRequires : startup-notification-dev
BuildRequires : zenity
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Metacity is not a meta-City as in an urban center, but rather
Meta-ness as in the state of being meta. i.e. metacity : meta as
opacity : opaque. Also it may have something to do with the Meta key
on UNIX keyboards.

%package bin
Summary: bin components for the metacity package.
Group: Binaries
Requires: metacity-data = %{version}-%{release}
Requires: metacity-license = %{version}-%{release}

%description bin
bin components for the metacity package.


%package data
Summary: data components for the metacity package.
Group: Data

%description data
data components for the metacity package.


%package dev
Summary: dev components for the metacity package.
Group: Development
Requires: metacity-lib = %{version}-%{release}
Requires: metacity-bin = %{version}-%{release}
Requires: metacity-data = %{version}-%{release}
Provides: metacity-devel = %{version}-%{release}
Requires: metacity = %{version}-%{release}

%description dev
dev components for the metacity package.


%package lib
Summary: lib components for the metacity package.
Group: Libraries
Requires: metacity-data = %{version}-%{release}
Requires: metacity-license = %{version}-%{release}

%description lib
lib components for the metacity package.


%package license
Summary: license components for the metacity package.
Group: Default

%description license
license components for the metacity package.


%package locales
Summary: locales components for the metacity package.
Group: Default

%description locales
locales components for the metacity package.


%package man
Summary: man components for the metacity package.
Group: Default

%description man
man components for the metacity package.


%prep
%setup -q -n metacity-3.50.0
cd %{_builddir}/metacity-3.50.0
pushd ..
cp -a metacity-3.50.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695686701
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1695686701
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/metacity
cp %{_builddir}/metacity-%{version}/COPYING %{buildroot}/usr/share/package-licenses/metacity/7222ccadf8bf66ff80f555df6cd9882482d6622e || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang metacity
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/metacity
/V3/usr/bin/metacity-message
/V3/usr/bin/metacity-theme-viewer
/usr/bin/metacity
/usr/bin/metacity-message
/usr/bin/metacity-theme-viewer

%files data
%defattr(-,root,root,-)
/usr/share/applications/metacity.desktop
/usr/share/glib-2.0/schemas/org.gnome.metacity.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.metacity.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.metacity.keybindings.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.metacity.theme.gschema.xml
/usr/share/gnome-control-center/keybindings/50-metacity-navigation.xml
/usr/share/gnome-control-center/keybindings/50-metacity-system.xml
/usr/share/gnome-control-center/keybindings/50-metacity-windows.xml

%files dev
%defattr(-,root,root,-)
/usr/include/metacity/libmetacity/meta-button.h
/usr/include/metacity/libmetacity/meta-color.h
/usr/include/metacity/libmetacity/meta-frame-borders.h
/usr/include/metacity/libmetacity/meta-frame-enums.h
/usr/include/metacity/libmetacity/meta-theme.h
/usr/lib64/libmetacity.so
/usr/lib64/pkgconfig/libmetacity.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmetacity.so.3.0.0
/usr/lib64/libmetacity.so.3
/usr/lib64/libmetacity.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/metacity/7222ccadf8bf66ff80f555df6cd9882482d6622e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/metacity-message.1
/usr/share/man/man1/metacity-theme-viewer.1
/usr/share/man/man1/metacity.1

%files locales -f metacity.lang
%defattr(-,root,root,-)

