Name:       asahi-fedora-remix-logos
Version:    38.0
Release:    1%{?dist}
Summary:    Asahi Fedora Remix icons and logos

Group:      System Environment/Base
URL:        https://pagure.io/fedora-asahi/asahi-fedora-remix-logos/
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
License:    CC-BY-SA-4.0
BuildArch:  noarch

Provides:   redhat-logos = %{version}-%{release}
Provides:   system-logos = %{version}-%{release}

Obsoletes:  fedora-logos < 1:%{version}-%{release}
Provides:   fedora-logos = 1:%{version}-%{release}
Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5
BuildRequires: hardlink

%description
The asahi-fedora-remix-logos package contains various image files which can be
used by the bootloader, anaconda, and other related tools.

%package httpd
Summary: Fedora-related icons and pictures used by httpd
Provides: system-logos-httpd = %{version}-%{release}
Obsoletes: fedora-logos-httpd < 1:%{version}-%{release}
Provides: fedora-logos-httpd = 1:%{version}-%{release}
BuildArch: noarch

%description httpd
The asahi-fedora-remix-logos-httpd package contains image files which can be used by
httpd.

%prep
%autosetup

%build
# Do nothing

%install
# Bootloader related files
mkdir -p %{buildroot}%{_datadir}/pixmaps/bootloader
# To regenerate this file, see the bootloader/fedora.icns entry in the Makefile
install -p -m 644 bootloader/fedora.icns %{buildroot}%{_datadir}/pixmaps/bootloader

# To regenerate these files, run:
# pngtopnm foo.png | ppmtoapplevol > foo.vol
install -p -m 644 bootloader/fedora.vol bootloader/fedora-media.vol %{buildroot}%{_datadir}/pixmaps/bootloader

# m1n1 logos, see Makefile for how to regenerate
install -p -m 644 bootloader/bootlogo_128.png %{buildroot}%{_datadir}/pixmaps/bootloader/bootlogo_128.png
install -p -m 644 bootloader/bootlogo_256.png %{buildroot}%{_datadir}/pixmaps/bootloader/bootlogo_256.png

# General purpose Fedora logos
for i in pixmaps/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps
done

# The Plymouth charge theme
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/charge
for i in plymouth/charge/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/plymouth/themes/charge
done

# The Plymoth spinner theme Fedora logo bits
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/spinner
install -p -m 644 pixmaps/fedora-gdm-logo.png %{buildroot}%{_datadir}/plymouth/themes/spinner/watermark.png

# Fedora logo icons
for size in 16x16 32x32 48x48 64x64 128x128 256x256 512x512 ; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size/apps
  mkdir -p %{buildroot}%{_datadir}/icons/Bluecurve/$size/apps
  pushd %{buildroot}%{_datadir}/icons/Bluecurve/$size/apps
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png icon-panel-menu.png
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png gnome-main-menu.png
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png kmenu.png
    ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png start-here.png
  popd
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 $i %{buildroot}%{_datadir}/icons/hicolor/$size/apps
  done
done

for i in 16 32 48 64 128 256 512 ; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/places
  install -p -m 644 -D %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/fedora-logo-icon.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/places/start-here.png
done

# Fedora favicon
mkdir -p %{buildroot}%{_sysconfdir}
pushd %{buildroot}%{_sysconfdir}
  ln -s %{_datadir}/icons/hicolor/16x16/apps/fedora-logo-icon.png favicon.png
popd

# Fedora hicolor icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/xfce4_xicon1.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/fedora-logo-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/start-here.svg
install -p -m 644 icons/hicolor/scalable/apps/org.fedoraproject.AnacondaInstaller.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.fedoraproject.AnacondaInstaller.svg
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/places/
pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/places/
  ln -s ../apps/start-here.svg .
popd
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps
install -p -m 644 icons/hicolor/symbolic/apps/org.fedoraproject.AnacondaInstaller-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/

# Fedora art in anaconda
# To regenerate the lss file, see anaconda/Makefile
mkdir -p %{buildroot}%{_datadir}/anaconda/boot
#install -p -m 644 anaconda/splash.lss %{buildroot}%{_datadir}/anaconda/boot/
install -p -m 644 anaconda/syslinux-splash.png %{buildroot}%{_datadir}/anaconda/boot/
# note the filename change
install -p -m 644 anaconda/syslinux-vesa-splash.png %{buildroot}%{_datadir}/anaconda/boot/splash.png
mkdir -p %{buildroot}%{_datadir}/anaconda/pixmaps
install -p -m 644 anaconda/anaconda_header.png %{buildroot}%{_datadir}/anaconda/pixmaps/
# This had not been regenerated since Fedora 17. Clearly not used anymore.
# install -p -m 644 anaconda/progress_first.png %%{buildroot}%%{_datadir}/anaconda/pixmaps/
# install -p -m 644 anaconda/splash.png %%{buildroot}%%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/sidebar-logo.png %{buildroot}%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/sidebar-bg.png %{buildroot}%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/topbar-bg.png %{buildroot}%{_datadir}/anaconda/pixmaps/

# SVG Fedora logos
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a fedora/*.svg %{buildroot}%{_datadir}/%{name}

# save some dup'd icons
# Except in /boot. Because some people think it is fun to use VFAT for /boot.
# hardlink is /usr/sbin/hardlink on Fedora <= 30 and /usr/bin/hardlink on F31+
hardlink -vv %{buildroot}/usr

%files
%license LICENSE
%doc README
%{_datadir}/anaconda/boot/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%{_datadir}/plymouth/themes/charge/*
%{_datadir}/plymouth/themes/spinner/*
%{_datadir}/icons/Bluecurve/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/%{name}/

%files httpd
%license LICENSE
%{_sysconfdir}/favicon.png
%{_datadir}/pixmaps/poweredby.png

%changelog
* Thu Feb 16 2023 Neal Gompa <ngompa@fedoraproject.org> - 38.0-1
- Initial release
