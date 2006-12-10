Summary:	Themeable window decorator and compositing manager for beryl
Summary(pl):	Dekorator okien dla beryla u¿ywaj±cy motywów
Name:		aquamarine
Version:	0.1.3
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	aeb1c42f907f08226c5d4ce48b8d209c
Patch0:		%{name}-ac260-lt.patch
URL:		http://www.beryl-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.5
BuildRequires:	beryl-core-devel >= 1:0.1.3
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	kdebase-devel >= 9:3.5.0
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xorg-lib-libXcomposite-devel
Requires:	beryl-core >= 1:0.1.3
Obsoletes:	compiz-quinnstorm-kde-decorator
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aquamarine is themeable window decorator and compositing manager for
beryl. Aquamarine is intended for use with KDE.

%description -l pl
Aquamarine jest dekoratorem okien dla beryla u¿ywaj±cym motywów. Jest
przeznaczony do u¿ywania wraz z KDE.

%prep
%setup -q
%patch0 -p1

%build
# can't libtoolize with KDE mess
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS 
%attr(755,root,root) %{_bindir}/aquamarine
