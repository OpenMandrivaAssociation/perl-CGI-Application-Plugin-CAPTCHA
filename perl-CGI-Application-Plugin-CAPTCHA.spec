%define upstream_name    CGI-Application-Plugin-CAPTCHA
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Easily create, use, and verify CAPTCHAs in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI::Application)
BuildRequires:	perl(GD::SecurityImage)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Data::Random)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::WWW::Mechanize)
BuildRequires:	perl(HTTP::Server::Simple::CGI)
BuildArch:	noarch

%description
'CGI::Application::Plugin::CAPTCHA' allows programmers to easily add and
verify CAPTCHAs in their CGI::Application-derived web applications.

A CAPTCHA (or Completely Automated Public Turing Test to Tell Computers and
Humans Apart) is an image with a random string of characters. A user must
successfully enter the random string in order to submit a form. This is a
simple (yet annoying) procedure for humans to complete, but one that is
significantly more difficult for a form-stuffing script to complete without
having to integrate some sort of OCR.

CAPTCHAs are not a perfect solution. Any skilled, diligent cracker will
eventually be able to bypass a CAPTCHA, but it should be able to shut down
your average script-kiddie.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/CGI


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 680675
- mass rebuild

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 629521
- update to new version 0.04

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 401709
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.01-2mdv2010.0
+ Revision: 375965
- rebuild

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2009.1
+ Revision: 357979
- import perl-CGI-Application-Plugin-CAPTCHA


* Tue Mar 17 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

