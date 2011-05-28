%define upstream_name    Acme-Damn
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    'Unbless' Perl objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Acme/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
*Acme::Damn* provides a single routine, *damn()*, which takes a blessed
reference (a Perl object), and _unblesses_ it, to return the original
reference. I can't think of any reason why you might want to do this, but
just because it's of no use doesn't mean that you shouldn't be able to do
it.

EXPORT
    By default, *Acme::Damn* exports the method *damn()* into the current
    namespace. Aliases for *damn()* (see below) may be imported upon
    request.

Methods
    * *damn* _object_

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
