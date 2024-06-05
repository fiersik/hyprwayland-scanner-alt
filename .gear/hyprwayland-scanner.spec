Name: hyprwayland-scanner
Version: 0.3.4
Release: alt1

Summary: Hyprland implementation of wayland-scanner
License: BSD-3-Clause
Group: Development/C++

Url: https://github.com/hyprwm/hyprwayland-scanner

ExcludeArch: i586
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libpugixml-devel

%description
A Hyprland implementation of wayland-scanner, in and for C++.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_pkgconfigdir/*.pc
%_libdir/cmake/%name/
