Summary:	A library for character- and string-glyphs from Adobe Type 1 fonts
Name:		t1lib
Version:	1.1.0
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
Source1:	%{name}-fonts.Fontmap
Source2:	%{name}-fonts.fonts.scale
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-config.patch
URL:		http://www.windowmaker.org/
BuildRequires:	XFree86-devel
BuildRequires:	tetex
BuildRequires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin
%define		_t1fontsdir	%{_fontsdir}/Type1
%define		_t1afmdir	%{_t1fontsdir}/afm

%description
t1lib is a library distributed under the GNU General Public Library
License for generating character- and string-glyphs from Adobe Type 1
fonts under UNIX. t1lib uses most of the code of the X11 rasterizer
donated by IBM to the X11-project. But some disadvantages of the
rasterizer being included in X11 have been eliminated. Here are some
of the features:
- t1lib is completely independent of X11 (although the program
  provided for testing the library needs X11)
- fonts are made known to library by means of a font database file at
  runtime
- searchpaths for all types of input files are configured by means of
  a configuration file at runtime
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
- antialiasing is implemented using three gray-levels between black
  and white
- An interactive test program called "xglyph" is included in the
  distribution. This program allows to test all of the features of the
  library. It requires X11.

%package fonts
Summary:	Type 1 fonts
Summary(pl):	Fonty Type 1
Group:		X11/Fonts
Group(de):	X11/Fonts
Group(pl):	X11/Fonty
Requires:	%{name} = %{version}
Prereq:		textutils

%description fonts
Type 1 fonts.

%description fonts -l pl
Zestaw fontów Type 1.

%package devel
Summary:	Development files for t1lib
Summary(pl):	Pliki nag³ówkowe i biblioteki dla t1lib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
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
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for t1lib.

%description static -l pl
Biblioteki statyczne dla t1lib.

%package xglyph
Summary:	Test program for t1lib with X11 interface
Summary:	Program testowy dla t1lib z interfejsem X11
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name}-devel = %{version}

%description xglyph
Test program for t1lib with X11 interface.

%description xglyph -l pl
Program testowy dla t1lib z interfejsem X11.

%prep
%setup -q -n T1-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_includedir},%{_xbindir}} \
	$RPM_BUILD_ROOT{%{_t1fontsdir},%{_t1afmdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a Fonts/enc $RPM_BUILD_ROOT%{_datadir}/%{name}
install Fonts/afm/*.afm $RPM_BUILD_ROOT%{_t1afmdir}
install Fonts/type1/*.pfb $RPM_BUILD_ROOT%{_t1fontsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}-fonts
install %{SOURCE2} $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}-fonts

mv -f $RPM_BUILD_ROOT%{_bindir}/xglyph $RPM_BUILD_ROOT%{_xbindir}

gzip -9nf Changes README.t1* doc/*.dvi

%clean
rm -rf $RPM_BUILD_ROOT

%post 	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post fonts
cd %{_t1fontsdir}
cat fonts.scale.* | sort -u > fonts.scale.tmp
wc -l fonts.scale.tmp > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap

%postun fonts
cd %{_t1fontsdir}
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
wc -l fonts.scale.tmp > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null

%files
%defattr(644,root,root,755)
%doc {Changes,README.t1*,doc/*.dvi}.gz 
%doc doc/*.{tex,eps,fig}

%attr(755,root,root) %{_bindir}/type1afm
%attr(755,root,root) %{_libdir}/*.so.*.*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/enc

%config(noreplace) %{_datadir}/%{name}/t1lib.config

%files fonts
%defattr(644,root,root,755)
%{_t1fontsdir}/*.pfb
%{_t1afmdir}/*.afm
%{_t1fontsdir}/*.%{name}-fonts

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files xglyph
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/xglyph
