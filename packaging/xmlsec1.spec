Name:           xmlsec1
Version:        1.2.18
Release:        1
License:        MIT
Summary:        Library providing support for "XML Signature" and "XML Encryption" standards
Url:            http://www.aleksey.com/xmlsec/index.html
Group:          System/Libraries
Source0:        http://www.aleksey.com/xmlsec/download/xmlsec1-%{version}.tar.gz
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package openssl
Summary:        OpenSSL crypto plugin for XML Security Library
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

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

%prep
%setup -q


%build

%configure --disable-static \
    --enable-dynamic --disable-crypto-dl --disable-apps-crypto-dl --without-gnutls

make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%post openssl -p /sbin/ldconfig

%postun openssl -p /sbin/ldconfig




%files
%doc Copyright
%{_libdir}/libxmlsec1.so.*
/usr/bin/xmlsec1


%files openssl
%{_libdir}/libxmlsec1-openssl.so.*

%files devel
%doc Copyright
%{_includedir}/*.h
%{_bindir}/xmlsec1-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/xmlsec1Conf.sh
/usr/share/aclocal/xmlsec1.m4

