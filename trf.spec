Summary:	Trf is a tarifficator for dial-up connections
Summary(pl):	Trf jest taryfikatorem dla po³aczeñ dial-up
Name:		trf
Version:	0.4
Release:	0.1
Epoch:		0
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.ceti.pl/~eaquer/trf/%{name}-%{version}.tar.gz
# Source0-md5:	d2eacc3e9112603d705a27077d8e7b78
Patch0:		%{name}-Makefile.patch
URL:		http://www.ceti.pl/~eaquer/trf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trf is a tarifficator for dial-up connections. It's designed to work
with most popular Polish ISP - TP S.A.. It supports lump sum (pol -
ryczalt).

%description -l pl
Trf jest taryfikatorem dla po³aczeñ dial-up. Jest zaprojektowany do
pracy z najpopularniejszym polskim IPS - TP S.A.. Wspiera Rycza³ty
Internetowe TP S.A..

%prep
%setup -q
%patch0 -p0

%build
%{__make} linux \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install trfs $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
