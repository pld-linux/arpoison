# TODO: optflags
Summary:	Arpoison - sending custom ARP packets
Summary(pl.UTF-8):	Arpoison - narzędzie do wysyłania własnych pakietów ARP
Name:		arpoison
Version:	0.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/arpoison/%{name}-%{version}.tar.gz
# Source0-md5:	ba36ec51a4b84240057a96a693e46f97
URL:		http://arpoison.sourceforge.net/	
BuildRequires:	libnet-devel >= 1:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A program to send custom ARP packets.

%description -l pl.UTF-8
Program do wysyłania własnych pakietów ARP.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install arpoison $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(754,root,root) %{_sbindir}/*
