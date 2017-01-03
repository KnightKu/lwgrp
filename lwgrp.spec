Name:		lwgrp
Version:	1.0.1
Release:	1%{?dist}
Summary:	The Light-weight Group Library

Group:		System Environment/Libraries
License:	Copyright and BSD License
URL:		https://github.com/LLNL/lwgrp
Source:		%{name}-%{version}.tar.gz
BuildRoot:      %_topdir/BUILDROOT
#Release:	1%{?dist}

%description
The Light-weight Group Library provides methods for MPI codes to quickly create and destroy process groups

%prep
%setup -q


%build
export CFLAGS="-g -O0"
%configure

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
/usr/include/lwgrp.h
/usr/lib64/liblwgrp.a
/usr/lib64/liblwgrp.la
/usr/lib64/liblwgrp.so
/usr/lib64/pkgconfig/liblwgrp.pc

%doc
/usr/share/lwgrp/LICENSE.TXT
/usr/share/lwgrp/README



%changelog

