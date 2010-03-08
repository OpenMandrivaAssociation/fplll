%define name		fplll
%define version		3.0
%define release		%mkrel 3
%define major		3
%define patchlevel	12
%define libname		%mklibname %{name} %{major}
%define devname		%mklibname %{name} -d

Name:		%{name}
Group:		Sciences/Mathematics
License:	LGPL
Summary:	LLL-reduction of euclidean lattices
Version:	%{version}
Release:	%{release}
Source:		http://perso.ens-lyon.fr/damien.stehle/downloads/lib%{name}-%{version}.%{patchlevel}.tar.gz
URL:		http://perso.ens-lyon.fr/damien.stehle/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel

%description
%{name}-%{version} is a code distributed under the LGPL that LLL-reduces
euclidean lattices. The code has been written by David Cadé, Xavier Pujol
and Damien Stehlé.

%package	-n %{libname}
Summary:	lib%{name} shared libraries
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description	-n %{libname}
libfpll shared libraries. fplll is code that LLL-reduces euclidean lattices.

%package	-n %{devname}
Summary:	lib%{name} libraries, includes, etc
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{devname}
libfpll libraries, includes, etc. fplll is code that LLL-reduces
euclidean lattices.

%prep
%setup -q -n lib%{name}-%{version}.%{patchlevel}

%build
autoreconf
%configure --enable-shared --disable-static --includedir=%{_includedir}/%{name}

%make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/fplll
%{_bindir}/fplll_micro
%{_bindir}/fplll_verbose
%{_bindir}/generate
%{_bindir}/llldiff

%files		-n %{libname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libfplll.so.*

%files		-n %{devname}
%defattr(-,root,root)
%{_libdir}/libfplll.la
%{_libdir}/libfplll.so
