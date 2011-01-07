%define upstream_name    CGI-Application-Plugin-CAPTCHA
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Easily create, use, and verify CAPTCHAs in
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(GD::SecurityImage)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Data::Random)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::WWW::Mechanize)
BuildRequires: perl(HTTP::Server::Simple::CGI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%perl_vendorlib/CGI
