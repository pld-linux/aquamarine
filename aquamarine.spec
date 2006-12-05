%define         _snap   20061203
Summary:	Themeable window decorator and compositing manager for Beryl
Summary(pl):	Dekorator okien dla Beryla u¿ywaj±cy motywów
Name:		aquamarine
Version:	0.1.3
Release:	0.%{_snap}.1
License:	GPL v2+
Group:		Themes
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	ff567dcd75dede824fe66ab1955d2f21
Patch0:		kde-ac260-lt.patch
URL:		http://www.beryl-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.5.0
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aquamarine is themeable window decorator and compositing manager for
Beryl. Aquamarine is intended for use with KDE.

%description -l pl
Aquamarine jest dekoratorem okien dla Beryla u¿ywaj±cym motywów. Jest
przeznaczony do u¿ywania wraz z KDE.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -f admin/Makefile.common svn
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
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
