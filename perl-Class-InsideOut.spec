#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Class
%define	pnam	InsideOut
Summary:	Class::InsideOut - a safe, simple inside-out object construction kit
Summary(pl.UTF-8):	Class::InsideOut - bezpieczne, proste tworzenie obiektów inside-out
Name:		perl-Class-InsideOut
Version:	1.10
Release:	1
License:	Apache
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	942347c9fe1d36da470bf89de1753571
URL:		http://search.cpan.org/dist/Class-InsideOut/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple, safe and streamlined toolkit for building inside-out
objects. Unlike most other inside-out object building modules already
on CPAN, this module aims for minimalism and robustness.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do prostego i bezpiecznego tworzenia
obiektów inside-out. W przeciwieństwie do innych modułów tworzących
obiekty inside-out, wcześniej występujących w archiwum CPAN, ten moduł
ma być minimalnym i mocnym narzędziem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Class/*.pm
%{perl_vendorlib}/Class/InsideOut
# no pod in .pm, i like perldoc
%{perl_vendorlib}/Class/InsideOut.pod
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
