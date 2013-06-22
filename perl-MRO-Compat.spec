#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MRO
%define	pnam	Compat
Summary:	MRO::Compat - mro::* interface compatibility for Perls < 5.9.5
Summary(pl.UTF-8):	MRO::Compat - moduł dla kompatybilności z interfejsem mro::* dla Perla < 5.9.5
Name:		perl-MRO-Compat
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BO/BOBTFISH/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06d21a3baf3d578ff3d3e10621656530
URL:		http://search.cpan.org/dist/MRO-Compat/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-C3 >= 0.24
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "mro" namespace provides several utilities for dealing with method
resolution order and method caching in general in Perl 5.9.5 and
higher.

This module provides those interfaces for earlier versions of Perl
(back to 5.6.0 anyways).

%description -l pl.UTF-8
Przestrzeń nazw "mro" zapewnia niektórym narzędziom możliwość obsługi
kolejności rozwiązywania metod i ogólnie pamięci podręcznej metod w
wersji Perla 5.9.5 i wyższych.

Ten moduł udostępnia te interfejsy dla wcześniejszych wersji Perla
(począwszy od 5.6.0).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorlib}/MRO
%{perl_vendorlib}/MRO/Compat.pm
%{_mandir}/man3/MRO::Compat.3pm*
