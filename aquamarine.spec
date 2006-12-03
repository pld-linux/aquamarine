%define         _snap   20061203
Summary:	Themeable window decorator and compositing manager for Beryl
Summary(pl):	Dekorator dla Beryla u¿ywaj±cy tematów
Name:		aquamarine
Version:	0.1.2_%{_snap}
Release:	1
License:	GPL
Group:		Themes
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	ff567dcd75dede824fe66ab1955d2f21
Source1:	admin.tar.gz
BuildRequires:	kdebase-devel >= 9:3.5.0
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aquamarine is themeable window decorator and compositing manager for
Beryl. Aquamarine is intended for use with KDE.

%description -l pl
Aquamarine jest dekoratorem okien dla beryla u¿ywaj±cym tematów. Jest
przeznaczony do u¿ywania wraz z kde.

%prep
%setup -q -n %{name}
%{__make} -f admin/Makefile.common svn

%build
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
%attr(755,root,root) %{_bindir}/aquamarine
