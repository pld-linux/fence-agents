#
# TODO:
#	- split into subpackages
%include	/usr/lib/rpm/macros.perl
Summary:	Reusable cluster fencing scripts
Summary(pl.UTF-8):	Skrypty barier klastrowych wielokrotnego użytku
Name:		fence-agents
Version:	3.1.8
Release:	1
License:	GPL v2+; LGPL v2.1+
Group:		Daemons
Source0:	https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.xz
# Source0-md5:	2dbdd6d820a126478eb7600c3be1b075
URL:		https://fedorahosted.org/cluster/wiki/HomePage
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	perl-Net-Telnet
BuildRequires:	python-pexpect
BuildRequires:	python-pycurl
BuildRequires:	python-suds
BuildRequires:	rpm-perlprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cluster-fence >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scripts providing fencing facilities for cluster nodes.

%description -l pl.UTF-8
Skrypty zapewniające funkcjonalność barier dla węzłów klastra.

%prep
%setup -q

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
%doc doc/README.licence
%attr(755,root,root) %{_sbindir}/fence_*
%{_sysconfdir}/cluster/fence_na.conf
%{_datadir}/fence
%{_datadir}/cluster/fence_scsi_check.pl
%dir %{_datadir}/cluster/relaxng
%{_datadir}/cluster/relaxng/fence.rng.head
%{_datadir}/cluster/relaxng/fence.rng.tail
%{_datadir}/cluster/relaxng/fence2man.xsl
%{_datadir}/cluster/relaxng/fence2rng.xsl
%{_mandir}/man8/fence_*.8*
