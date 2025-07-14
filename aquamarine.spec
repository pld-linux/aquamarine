Summary:	Themeable window decorator and compositing manager for beryl
Summary(pl.UTF-8):	Dekorator okien dla beryla używający motywów
Name:		aquamarine
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	186826182dc2cefb3aaa09b7af938bec
Patch0:		%{name}-include.patch
Patch1:		kde-ac260-lt.patch
URL:		http://www.beryl-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	kdebase-devel >= 9:3.5.0
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXft-devel
Requires:	beryl-core >= 1:%{version}
Obsoletes:	compiz-quinnstorm-kde-decorator
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aquamarine is themeable window decorator and compositing manager for
beryl. Aquamarine is intended for use with KDE.

%description -l pl.UTF-8
Aquamarine jest dekoratorem okien dla beryla używającym motywów. Jest
przeznaczony do używania wraz z KDE.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1

mv -f po/{es_ES,es}.po
mv -f po/{hu_HU,hu}.po
mv -f po/{pl_PL,pl}.po
mv -f po/{sv_SE,sv}.po
mv -f po/{uk_UA,uk}.po
rm -f po/it_IT.po # it.po is newer then it_IT.po
rm -f po/ru_RU.po # ru.po is newer
rm -f po/ru_UA.po # same as ru_RU.po

# NOTE: check the list after any upgrade!
cat > po/LINGUAS <<EOF
ca
de
es
es_AR
hu
it
ja
ko
nl
pl
pt
ru
sv
uk
zh_CN
zh_HK
zh_TW
EOF

%build
%{__autoconf}
%{__autoheader}
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

%find_lang %{name}
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/aquamarine
%{_libdir}/beryl/backends/libkconfig.la
%attr(755,root,root) %{_libdir}/beryl/backends/libkconfig.so
%{_libdir}/kde3/kcm_beryl.la
%attr(755,root,root) %{_libdir}/kde3/kcm_beryl.so
%{_desktopdir}/kde/beryl.desktop
%{_datadir}/config.kcfg/aquamarine.kcfg
