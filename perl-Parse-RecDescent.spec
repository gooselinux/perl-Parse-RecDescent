Name:           perl-Parse-RecDescent
Version:        1.962.2
Release:        2%{?dist}
Summary:        Parse-RecDescent Perl module

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Parse-RecDescent/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Parse-RecDescent-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker), perl(version), perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Balanced)

%{?perl_default_filter}

%description
Parse::RecDescent incrementally generates top-down recursive-descent
text parsers from simple yacc-like grammar specifications. It
provides:
    * Regular expressions or literal strings as terminals (tokens),
    * Multiple (non-contiguous) productions for any rule,
    * Repeated and optional subrules within productions,
    * Full access to Perl within actions specified as part of the
      grammar,
    * Simple automated error reporting during parser generation and
      parsing,
    * The ability to commit to, uncommit to, or reject particular
      productions during a parse,
    * The ability to pass data up and down the parse tree ("down" via
      subrule argument lists, "up" via subrule return values)
    * Incremental extension of the parsing grammar (even during a
      parse),
    * Precompilation of parser objects,

User-definable reduce-reduce conflict resolution via "scoring" of
matching productions.


%prep
%setup -q -n Parse-RecDescent-%{version}
chmod a-x demo/* tutorial/*
%{__perl} -pi -e 's|^#!\s?/usr/local/bin/perl\b|#!%{__perl}|' demo/*
for f in demo/demo_dot.pl; do
  iconv -f iso-8859-1 -t utf-8 < "$f" > "${f}_" && mv -f "${f}_" "$f"
done


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{perl_vendorlib}/Parse/
%{_mandir}/man3/*.3*
%doc Changes README demo/ tutorial/


%changelog
* Fri Jan 14 2011 Marcela Maslanova <mmaslano@redhat.com> 1.962.2-2
- rebuilt for RHEL-6
- Related: rhbz#643547

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.962.2-1
- updated for latest GA SQL::Translator
- add default filtering
- auto-update to 1.962.2 (by cpan-spec-update 0.01)
- added a new br on perl(Text::Balanced) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Stepan Kasal <skasal@redhat.com> - 1.96-1
- new upstream version

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.95.1-5
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.95.1-4
- rebuild for new perl

* Wed Nov 14 2007 Robin Norwood <rnorwood@redhat.com> - 1.95.1-3
- Apply fixes from package review:
  - Remove BR: perl
  - Use iconv to convert file to utf-8
  - Include BR: perl(Test::Pod)
  - Fix old changelog entry
- Resolves: bz#226274

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.95.1-2
- add BR: perl(version), perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.95.1-1
- bump to 1.95.1
- correct license tag (now under perl license)
- add BR: perl(ExtUtils::MakeMaker)

* Fri Jul 20 2007 Robin Norwood <rnorwood@redhat.com> - 1.94-6.fc8
- Bring fixes from EPEL build into F8
- Fix minor specfile issues
- Package the docs as well

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.94-5.2.1
- rebuild

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.94-5.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Thu Apr 21 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.94-5
- #155620
- Bring up to date with current Fedora.Extras perl spec template.

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 1.94-4
- rebuild

* Tue Feb 17 2004 Chip Turner <cturner@redhat.com> 1.94-2
- fix rm to not be interactive (bz115997)

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 1.94-1
- update to 1.94

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Sat Jul 20 2002 Chip Turner <cturner@localhost.localdomain>
- remove Text::Balanced modules since they are now in core perl

* Thu Jun 27 2002 Chip Turner <cturner@redhat.com>
- description update

* Fri Jun 07 2002 cturner@redhat.com
- Specfile autogenerated
