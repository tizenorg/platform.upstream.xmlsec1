%define keepstatic 1
Name:           xmlsec1
Version:        1.2.19
Release:        1
License:        MIT
Summary:        Library providing support for "XML Signature" and "XML Encryption" standards
Url:            http://www.aleksey.com/xmlsec/index.html
Group:          System/Libraries
Source0:        http://www.aleksey.com/xmlsec/download/xmlsec1-%{version}.tar.gz
Source1001: 	xmlsec1.manifest
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package gcrypt
Summary:        Gcrypt crypto plugin for XML Security Library
Group:          System/Libraries
Requires:       %{name} = %{version}

%description gcrypt
Gcrypt plugin for XML Security Library provides gcrypt based crypto services
for the xmlsec library.

%package openssl
Summary:        OpenSSL crypto plugin for XML Security Library
Group:          System/Libraries
Requires:       %{name} = %{version}

%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.

%package devel
Summary:        Libraries, includes, etc
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed.

%package devel-static
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries
Requires:       %{name}-devel = %{version}

%description devel-static
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed.
This package contains static versions of the libxmlsec1 library.

%prep
%setup -q
cp %{SOURCE1001} .


%build

%configure --enable-static \
    --enable-dynamic --disable-crypto-dl --disable-apps-crypto-dl --without-gnutls

make %{?_smp_mflags}

%install
%make_install


%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post gcrypt -p /sbin/ldconfig

%postun gcrypt -p /sbin/ldconfig


%post openssl -p /sbin/ldconfig

%postun openssl -p /sbin/ldconfig



%files
%manifest %{name}.manifest
%license COPYING
%doc Copyright
%{_libdir}/libxmlsec1.so.*
%{_bindir}/xmlsec1


%files gcrypt
%manifest %{name}.manifest
%{_libdir}/libxmlsec1-gcrypt.so.*

%files openssl
%manifest %{name}.manifest
%{_libdir}/libxmlsec1-openssl.so.*

%files devel
%manifest %{name}.manifest
%doc Copyright
%{_includedir}/xmlsec1
%{_bindir}/xmlsec1-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/xmlsec1Conf.sh
%{_datadir}/aclocal/xmlsec1.m4

%files devel-static
%manifest %{name}.manifest
%{_libdir}/*.a

