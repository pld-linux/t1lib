Summary:	A library for character- and string-glyphs from Adobe Type 1 fonts.
Name:		t1lib
Version:	0.9.2
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
License:	LGPL
Source:		ftp://sunsite.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
Patch0:		t1lib-DESTDIR.patch
Patch1:		t1lib-doc.patch
Patch2:		t1lib-datadir.patch
Patch3:		t1lib-config.patch
URL:		http://www.windowmaker.org/
BuildRequires:	XFree86-devel
BuildRequires:	tetex
BuildRequires:	tetex-latex
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_fontdir	/usr/share/fonts

%description
t1lib is a library distributed under the GNU General Public Library License
for generating character- and string-glyphs from Adobe Type 1 fonts under
UNIX. t1lib uses most of the code of the X11 rasterizer donated by IBM to
the X11-project. But some disadvantages of the rasterizer being included in
X11 have been eliminated. Here are some of the features:
- t1lib is completely independent of X11 (although the program provided for
  testing the library needs X11)
- fonts are made known to library by means of a font database file at
  runtime
- searchpaths for all types of input files are configured by means of a
  configuration file at runtime
- characters are rastered as they are needed
- characters and complete strings may be rastered by a simple function
  call
- when rastering strings, pairwise kerning information from .afm-files
  may optionally be taken into account
- an interface to ligature-information of afm-files is provided
- a program to generate afm-files from Type 1 font files is included
- rotation is supported at any angles
- there's support for extending and slanting fonts
- underlining, overlining and overstriking is supported
- new encoding vectors may be loaded at runtime and fonts may be
  reencoded using these encoding vectors 
- antialiasing is implemented using three gray-levels between black and
  white
- An interactive test program called "xglyph" is included in the
  distribution. This program allows to test all of the features of the
  library. It requires X11.

%package fonts
Summary:	Type 1 fonts
Summary(pl):	Fonty Type 1
Group:		X11/Fonts
Group(pl):	X11/Fonty
Requires:	%{name} = %{version}
Requires:	type1inst >= 0.6.1

%description fonts
Type 1 fonts.

%description fonts -l pl
Zestaw fontów Type 1.

%package devel
Summary:	Development files for t1lib
Summary(pl):	Pliki nag³ówkowe i biblioteki dla t1lib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The files needed for developing applications using t1lib.

%description devel -l pl
Pliki niezbêdne do tworzenia aplikacji z wykorzystaniem t1lib.

%package static
Summary:	Static libraries for t1lib
Summary(pl):	Biblioteki statyczne dla t1lib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for t1lib.

%description devel -l pl
Biblioteki statyczne dla t1lib.

%prep
%setup -q -n T1-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_includedir},%{_fontdir}/Type1/afm}

make install DESTDIR=$RPM_BUILD_ROOT

install Fonts/afm/*.afm		$RPM_BUILD_ROOT%{_fontdir}/Type1/afm
install Fonts/type1/*.pfb	$RPM_BUILD_ROOT%{_fontdir}/Type1
cp -a Fonts/enc			$RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf Changes README.t1* doc/*.dvi


%post 	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post fonts
cd %{_fontdir}/Type1
/usr/bin/type1inst -nogs -nolog

%postun fonts
cd %{_fontdir}/Type1
/usr/bin/type1inst -nogs -nolog

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README.t1*,doc/*.dvi}.gz 
%doc doc/*.{tex,eps,fig}

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/enc

%config(noreplace) %{_datadir}/%{name}/t1lib.config

%files fonts
%defattr(644,root,root,755)
%{_fontdir}/Type1/afm/*
%{_fontdir}/Type1/*.pfb

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
