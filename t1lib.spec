Summary:	A library for character- and string-glyphs from Adobe Type 1 fonts
Name:		t1lib
Version:	1.0.1
Release:	4
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
Patch0:		t1lib-DESTDIR.patch
Patch1:		t1lib-doc.patch
Patch2:		t1lib-config.patch
URL:		http://www.windowmaker.org/
BuildRequires:	XFree86-devel
BuildRequires:	tetex
BuildRequires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_fontdir	/usr/share/fonts

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
Group(pl):	X11/Fonty
Requires:	%{name} = %{version}
Prereq:		type1inst >= 0.6.1

%description fonts
Type 1 fonts.

%description fonts -l pl
Zestaw font�w Type 1.

%package devel
Summary:	Development files for t1lib
Summary(pl):	Pliki nag��wkowe i biblioteki dla t1lib
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The files needed for developing applications using t1lib.

%description devel -l pl
Pliki niezb�dne do tworzenia aplikacji z wykorzystaniem t1lib.

%package static
Summary:	Static libraries for t1lib
Summary(pl):	Biblioteki statyczne dla t1lib
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for t1lib.

%description devel -l pl
Biblioteki statyczne dla t1lib.

%package xglyph
Summary:	Test program for t1lib with X11 interface
Summary:	Program testowy dla t1lib z interfejsem X11
Group:		X11/Applications
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
LDFLAGS="-s"; export LDFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_includedir},%{_fontdir}/Type1/afm} \
	$RPM_BUILD_ROOT/usr/X11R6/bin

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install Fonts/afm/*.afm		$RPM_BUILD_ROOT%{_fontdir}/Type1/afm
install Fonts/type1/*.pfb	$RPM_BUILD_ROOT%{_fontdir}/Type1
cp -a Fonts/enc			$RPM_BUILD_ROOT%{_datadir}/%{name}

mv $RPM_BUILD_ROOT{%{_bindir}/xglyph,/usr/X11R6/bin}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so.*.*

gzip -9nf Changes README.t1* doc/*.dvi

%post 	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post fonts
cd %{_fontdir}/Type1
%{_bindir}/type1inst -nolog -q

%postun fonts
cd %{_fontdir}/Type1
%{_bindir}/type1inst -nolog -q

%clean
rm -r $RPM_BUILD_ROOT

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

%files xglyph
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/xglyph
