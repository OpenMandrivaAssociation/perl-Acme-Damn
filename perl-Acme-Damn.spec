%define upstream_name    Acme-Damn
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    'Unbless' Perl objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Acme/Acme-Damn-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel

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
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.40.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.40.0-3
+ Revision: 680442
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 555217
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 401792
- rebuild using %%perl_convert_version
- fixed license field

* Tue May 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2010.0
+ Revision: 377487
- import perl-Acme-Damn


* Tue May 19 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist


