%define name		fplll
%define major		0
%define libfplll	%mklibname %{name} %{major}
%define libfplll_devel	%mklibname %{name} -d

Epoch:		1
Name:		%{name}
Group:		Sciences/Mathematics
License:	LGPLv2+
Summary:	LLL-reduction of euclidean lattices
Version:	4.0.4
Release:	3
Source:		http://perso.ens-lyon.fr/damien.stehle/fplll/lib%{name}-%{version}.tar.gz
URL:		https://perso.ens-lyon.fr/damien.stehle/fplll/
BuildRequires:	mpfr-devel

%description
fplll contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It contains a 'wrapper' choosing the
estimated best sequence of variants in order to provide a guaranteed
output as fast as possible. In the case of the wrapper, the
succession of variants is oblivious to the user. It also includes
a rigorous floating-point implementation of the Kannan-Fincke-Pohst
algorithm that finds a shortest non-zero lattice vector, and the BKZ
reduction algorithm.

%package	-n %{libfplll}
Summary:	lib%{name} shared libraries
Group:		System/Libraries

%description	-n %{libfplll}
libfpll shared libraries. fplll is code that LLL-reduces euclidean lattices.

%package	-n %{libfplll_devel}
Summary:	lib%{name} libraries, includes, etc
Group:		Development/C
Requires:	%{libfplll} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description	-n %{libfplll_devel}
libfpll libraries, includes, etc. fplll is code that LLL-reduces
euclidean lattices.

%prep
%setup -q -n lib%{name}-%{version}

%build
%configure2_5x --disable-static LDFLAGS="-Wl,--as-needed $RPM_LD_FLAGS"

# Eliminate hardcoded rpaths, and workaround libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool
%make

%install
%makeinstall_std
rm %{buildroot}%{_libdir}/libfplll.la

%check
export LD_LIBRARY_PATH=$PWD/src/.libs
make check

%files
%{_bindir}/*

%files		-n %{libfplll}
%{_libdir}/libfplll.so.*

%files		-n %{libfplll_devel}
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_libdir}/libfplll.so
