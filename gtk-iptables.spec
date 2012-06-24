Summary:	Gtk-IPTables is a gtk-based frontend for iptables
Summary(pl):	GTK-IPTables jest nak�adk� gtk na iptables.
Name:		gtk-iptables
Version:	0.4.21
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/gtk-iptables/%{name}-%{version}.tar.gz
# Source0-md5:	3328a211b6936802ae5a0bf263a269d7
URL:		http://gtk-iptables.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.10
Requires:	iptables
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk-IPTables is a gtk-based frontend for iptables. It's just a GUI so
if you don't have iptables it doesn't work. It's written in C and
developed on GNU/Linux.

%description -l pl
Gtk-IPTables jest bazuj�cymna na gtk interfejsem dla iptables. To jest
tylko GUI(graficzny interfejs) wi�c je�li nie masz zainstalowanego
iptables, nie b�dzie dzia�a�. Jest napisany w C i rozwijany dla
GNU/Linux.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README INSTALL
%attr(755,root,root) %{_bindir}/*
