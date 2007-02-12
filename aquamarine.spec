Summary:	Themeable window decorator and compositing manager for beryl
Summary(pl.UTF-8):   Dekorator okien dla beryla używający motywów
Name:		aquamarine
Version:	0.1.9999.1
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	aeb3fb74c880c7caa3e789b7248174bd
Patch0:		%{name}-ac260-lt.patch
Patch1:		%{name}-include.patch
Patch2:		kde-ac260-lt.patch
URL:		http://www.beryl-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.5
BuildRequires:	beryl-core-devel >= 1:0.1.3
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-regex-devel
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
Requires:	beryl-core >= 1:0.1.3
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
%patch0 -p1
%patch1 -p0
%patch2 -p1

mv -f po/{ca_ES,ca}.po
mv -f po/{es_ES,es}.po
mv -f po/{hu_HU,hu}.po
mv -f po/{it_IT,it}.po
mv -f po/{ko_KR,ko}.po
mv -f po/{pl_PL,pl}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{ru_RU,ru}.po
mv -f po/{sv_SE,sv}.po
mv -f po/{uk_UA,uk}.po
rm -r po/ru_UA.po # I dont know whot's that

# NOTE: check the list after any upgrade!
cat > po/LINGUAS <<EOF
ca
es
es_AR
fr
hu
it
ko
pl
pt_BR
pt
ru
sv
uk
zh_CN
zh_HK
zh_TW
EOF

%build
# can't libtoolize with KDE mess
#%{__aclocal}
%{__autoconf}
%{__autoheader}
#%{__automake}
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
%{_prefix}/lib/beryl/backends/libkconfig.la
%attr(755,root,root) %{_prefix}/lib/beryl/backends/libkconfig.so
%{_prefix}/lib/kde3/kcm_beryl.la
%attr(755,root,root) %{_prefix}/lib/kde3/kcm_beryl.so
%{_desktopdir}/kde/beryl.desktop
%{_datadir}/config.kcfg/aquamarine.kcfg
