#
# TODO:
#	- split into subpackages

Summary:	Reusable cluster fencing scripts
Name:		fence-agents
Version:	3.1.8
Release:	1
License:	GPL v2+; LGPL v2.1+
Group:		Daemons
URL:		https://fedorahosted.org/cluster/wiki/HomePage
Source0:	https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.xz
# Source0-md5:	2dbdd6d820a126478eb7600c3be1b075
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl(Net::Telnet)
BuildRequires:	python-pycurl
BuildRequires:	python-suds
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scripts providing fencing facilities for cluster nodes.

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

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

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
%{_mandir}/man8/fence_*
