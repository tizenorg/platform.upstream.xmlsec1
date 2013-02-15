#sbs-git:slp/pkgs/x/xmlsec1 xmlsec1 1.2.14 bd7cd922035219f41232d25d9eaf5a2894474165

Name:       xmlsec1
Summary:    Library providing support for "XML Signature" and "XML Encryption" standards
Version: 1.2.14
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.aleksey.com/xmlsec/index.html
Source0:    http://www.aleksey.com/xmlsec/download/xmlsec1-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(openssl)


%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine



%package openssl
Summary:    OpenSSL crypto plugin for XML Security Library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.


%package devel
Summary:    Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support.
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed.



%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static \
    --enable-dynamic --disable-crypto-dl --disable-apps-crypto-dl --without-gnutls

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%post openssl -p /sbin/ldconfig

%postun openssl -p /sbin/ldconfig




%files
%manifest xmlsec1.manifest
%defattr(-,root,root,-)
%doc Copyright AUTHORS README NEWS ChangeLog
%{_libdir}/libxmlsec1.so.*
/usr/bin/xmlsec1
/usr/share/man/man1/xmlsec1.1.gz


%files openssl
%manifest xmlsec1.manifest
%defattr(-,root,root,-)
%{_libdir}/libxmlsec1-openssl.so.*

%files devel
%defattr(-,root,root,-)
%doc Copyright ChangeLog AUTHORS README NEWS TODO
/usr/include/*
/usr/bin/xmlsec1-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/xmlsec1Conf.sh
/usr/share/doc/xmlsec1/*
/usr/share/man/man1/xmlsec1-config.1.gz
/usr/share/aclocal/xmlsec1.m4

