#
# TODO:
#	- split into subpackages
%include	/usr/lib/rpm/macros.perl
Summary:	Reusable cluster fencing scripts
Summary(pl.UTF-8):	Skrypty barier klastrowych wielokrotnego użytku
Name:		fence-agents
Version:	4.0.8
Release:	1
License:	GPL v2+ (libraries), LGPL v2.1+ (applications)
Group:		Daemons
Source0:	https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.xz
# Source0-md5:	13334ea0477dfde9b876ddeee4b61aa8
Patch0:		%{name}-check.patch
URL:		https://fedorahosted.org/cluster/wiki/HomePage
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	perl-Net-Telnet
BuildRequires:	pkgconfig
BuildRequires:	python-pexpect
BuildRequires:	python-pycurl
BuildRequires:	python-suds
BuildRequires:	rpm-perlprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# /usr/bin/gnutls-cli tool
Requires:	gnutls
# XXX: is it proper dependency for cluster 4?
Requires:	resource-agents >= 3.9
# /usr/bin/amttool
Suggests:	amtterm
# /usr/bin/ipmitool
Suggests:	ipmitool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scripts providing fencing facilities for cluster nodes.

%description -l pl.UTF-8
Skrypty zapewniające funkcjonalność barier dla węzłów klastra.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rmdir $RPM_BUILD_ROOT/var/run/cluster

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/{COPYRIGHT,README.licence}
%attr(755,root,root) %{_sbindir}/fence_*
%attr(755,root,root) %{_libexecdir}/fence_kdump_send
%{_datadir}/fence
%{_datadir}/cluster/fence_scsi_check.pl
%dir %{_datadir}/cluster/relaxng
%{_datadir}/cluster/relaxng/fence.rng.head
%{_datadir}/cluster/relaxng/fence.rng.tail
%{_datadir}/cluster/relaxng/fence2man.xsl
%{_datadir}/cluster/relaxng/fence2rng.xsl
%{_datadir}/cluster/relaxng/metadata.rng
%{_mandir}/man8/fence_*.8*
