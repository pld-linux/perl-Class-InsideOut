#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	InsideOut
Summary:	Class::InsideOut - a safe, simple inside-out object construction kit
#Summary(pl):	
Name:		perl-Class-InsideOut
Version:	1.08
Release:	1
License:	Apache
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/Class-InsideOut-1.08.tar.gz
# Source0-md5:	74939b510a64a2a8e1f6fe207cbbaeb3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple, safe and streamlined toolkit for building inside-out objects.
Unlike most other inside-out object building modules already on CPAN, this
module aims for minimalism and robustness:

It provides the minimal support necessary for creating safe inside-out objects
and generating flexible accessors.  



# %description -l pl
# TODO

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
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

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
