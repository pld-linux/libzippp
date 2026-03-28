%define		libzip_ver	1.10.1

Summary:	C++ wrapper for libzip
Summary(pl.UTF-8):	Interfejs C++ do libzip
Name:		libzippp
Version:	7.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/ctabin/libzippp/releases
Source0:	https://github.com/ctabin/libzippp/archive/libzippp-v%{version}-%{libzip_ver}/%{name}-%{version}.tar.gz
# Source0-md5:	dd6e9cc5ddcd287d669159a36ac63055
Patch0:		soname.patch
URL:		https://github.com/ctabin/libzippp
BuildRequires:	cmake >= 3.16.0
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	libzip-devel >= %{libzip_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	libzip%{?_isa} >= %{libzip_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libzippp is a simple basic C++ wrapper around the libzip library. It
is meant to be a portable and easy-to-use library for ZIP handling.

%description -l pl.UTF-8
libzippp to proste, podstawowe obudowanie C++ biblioteki libzip. Jest
pomyślany jako przenośna i łatwa w użyciu biblioteka do obsługi
formatu ZIP.

%package devel
Summary:	Development files for libzippp
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libzippp
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.8.1

%description devel
This package contains the header files for developing applications
that use libzippp.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libzippp.

%prep
%setup -q -n libzippp-libzippp-v%{version}-%{libzip_ver}
%patch -P0 -p1

%build
%cmake -B build \
	-DLIBZIPPP_GNUINSTALLDIRS:BOOL=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENCE README.md
%{_libdir}/libzippp.so.*.*.*
%ghost %{_libdir}/libzippp.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libzippp.so
%dir %{_includedir}/libzippp
%{_includedir}/libzippp/libzippp.h
%{_libdir}/cmake/libzippp
%{_pkgconfigdir}/libzippp.pc
