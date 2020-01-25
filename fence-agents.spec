# TODO:
#	- split into subpackages
Summary:	Reusable cluster fencing scripts
Summary(pl.UTF-8):	Skrypty barier klastrowych wielokrotnego użytku
Name:		fence-agents
Version:	4.0.24
Release:	1
License:	GPL v2+ (libraries), LGPL v2.1+ (applications)
Group:		Daemons
Source0:	https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.xz
# Source0-md5:	161195adb0c125bbbbc1440920a2ff28
Patch0:		%{name}-check.patch
URL:		https://fedorahosted.org/cluster/wiki/HomePage
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	perl-Net-Telnet
BuildRequires:	pkgconfig
BuildRequires:	python-openwsman
BuildRequires:	python-pexpect
BuildRequires:	python-pycurl
BuildRequires:	python-requests
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
# /usr/sbin/corosync-cmapctl tool
Suggests:	corosync
# /usr/bin/ipmitool
Suggests:	ipmitool
# /sbin/vgs
Suggests:	lvm2
# /sbin/mpathpersist
Suggests:	multipath-tools
# /usr/bin/snmpget, /usr/bin/snmpset, /usr/bin/snmpwalk
Suggests:	net-snmp-tools
Suggests:	openssh-clients
# /usr/bin/sg_persist, /usr/bin/sg_turs
Suggests:	sg3_utils
Suggests:	sudo
Suggests:	telnet
# [/usr]/sbin/sbd
Suggests:	cluster-sbd
# /usr/bin/nova - seems not used
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
%{__aclocal} -I make
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	SBD_PATH=/usr/sbin/sbd

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
%attr(755,root,root) %{_datadir}/cluster/fence_scsi_check
%attr(755,root,root) %{_datadir}/cluster/fence_scsi_check_hardreboot
%dir %{_datadir}/cluster/relaxng
%{_datadir}/cluster/relaxng/fence.rng.head
%{_datadir}/cluster/relaxng/fence.rng.tail
%{_datadir}/cluster/relaxng/fence2man.xsl
%{_datadir}/cluster/relaxng/fence2rng.xsl
%{_datadir}/cluster/relaxng/fence2wiki.xsl
%{_datadir}/cluster/relaxng/metadata.rng
%{_mandir}/man8/fence_*.8*
