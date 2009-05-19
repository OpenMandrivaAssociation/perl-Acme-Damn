
%define realname   Acme-Damn
%define version    0.04
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    'Unbless' Perl objects
Source:     http://www.cpan.org/modules/by-module/Acme/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)



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
%setup -q -n %{realname}-%{version} 

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


