Summary:	A library for character- and string-glyphs from Adobe Type 1 fonts
Summary(pl):	Biblioteka znakowych i ³añcuchowych glifów z fontów Adobe Type 1
Summary(pt_BR):	Rasterizador de fontes Type 1
Summary(ru):	òÁÓÔÅÒÉÚÁÔÏÒ ÛÒÉÆÔÏ× Type 1
Summary(uk):	òÁÓÔÅÒÉÚÁÔÏÒ ÛÒÉÆÔ¦× Type 1
Name:		t1lib
Version:	1.3.1
Release:	4
License:	LGPL
Group:		Libraries
Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
Source1:	%{name}-fonts.Fontmap
Source2:	%{name}-fonts.fonts.scale
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-dontprint.patch
Patch4:		%{name}-KernMapSize.patch
Patch5:		%{name}-man.patch
Patch6:		%{name}-%{name}config.patch
Patch7:		%{name}-xglyph.patch
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%{!?_without_doc:BuildRequires:	tetex-dvips}
%{!?_without_doc:BuildRequires:	tetex-latex}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libt1lib1.3.1
Obsoletes:	libt1lib1.3.1-progs

%define		_xbindir	/usr/X11R6/bin
%define		_t1fontsdir	%{_fontsdir}/Type1
%define		_t1afmdir	%{_t1fontsdir}/afm
%define		_datadir	/etc

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
  distribution (as separate package). This program allows to test all of
  the features of the library. It requires X11.

%description -l pl
t1lib jest wypuszczon± na LGPL bibliotek± do generowania znakowych i
³añcuchowych glifów z fontów Adobe Type 1. t1lib u¿ywa wiêkszo¶ci kodu
rasteryzera X11 (wspomaganego przez IBM), ale niektóre wady tego
rasteryzera zosta³y usuniête. Niektóre cechy t1lib:
- ca³kowita niezale¿no¶æ od X11 (tylko program dostarczony do testów
  wymaga X11)
- fonty s± znane bibliotece poprzez dodanie do pliku z baz± danych o
  fontach - w czasie uruchamiania
- ¶cie¿ki wyszukiwania wszystkich plików wej¶ciowych s± konfigurowalne
  w czasie uruchamiania
- znaki s± rasteryzowane kiedy s± potrzebne
- znaki i ca³kowite ³añcuchy mog± byæ zrasteryzowane prostym
  wywo³aniem funkcji
- przy rasteryzacji ³añcuchów opcjonalnie mog± byæ brane pod uwagê
  informacje o kerningu z plików .afm
- interfejs do informacji o ligaturach z plików .afm
- do³±czony program do generowania plików .afm z fontów Type 1
- obroty o dowolny k±t
- wsparcie do rozszerzania i pochylania znaków
- wsparcie dla podkre¶lania, nadkre¶lania, przekre¶lania
- nowe wektory kodowania mog± byæ wczytane w czasie dzia³ania i fonty
  mog± byæ ponownie zakodowane przy u¿yciu tych wektorów
- antyaliasing zaimplementowany przy u¿yciu trzech stopni szaaro¶ci
  pomiêdzy czerni± a biel±
- interaktywny program testowy xglyph - w osobnym pakiecie (wymaga X).

%description -l pt_BR
Rasterizador de fontes Type 1 da Adobe.

%description -l ru
T1lib - ÜÔÏ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÓÏÚÄÁÎÉÑ ÇÌÉÆÏ× ÓÉÍ×ÏÌÏ× É ÃÅÐÏÞÅË ÓÉÍ×ÏÌÏ×
ÉÚ ÛÒÉÆÔÏ× Adobe Type 1. T1lib ÉÓÐÏÌØÚÕÅÔ ËÏÄ ÒÁÓÔÅÒÉÚÁÔÏÒÁ ÄÌÑ X11
ÐÏÄÁÒÅÎÎÏÇÏ ÆÉÒÍÏÊ IBM ÐÒÏÅËÔÕ X11. îÏ ÎÅËÏÔÏÒÙÅ ÎÅÄÏÓÔÁÔËÉ
×ËÌÀÞÅÎÎÏÇÏ × X11 ÒÁÓÔÅÒÉÚÁÔÏÒÁ ÂÙÌÉ ÕÓÔÒÁÎÅÎÙ. T1lib ×ËÌÀÞÁÅÔ ÔÁËÖÅ
ÐÏÄÄÅÒÖËÕ ÁÎÔÉÁÌÉÁÓÉÎÇÁ.

%description -l uk
T1lib - ÃÅ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÓÔ×ÏÒÅÎÎÎÑ ÇÌ¦Æ¦× ÓÉÍ×ÏÌ¦× ÔÁ ÌÁÎÃÀÖË¦×
ÓÉÍ×ÏÌ¦× Ú ÛÒÉÆÔ¦× Adobe Type 1. T1lib ×ÉËÏÒÉÓÔÏ×Õ¤ ËÏÄ ÒÁÓÔÅÒÉÚÁÔÏÒÁ
ÄÌÑ X11 ÐÏÄÁÒÏ×ÁÎÏÇÏ Æ¦ÒÍÏÀ IBM ÐÒÏÅËÔÕ X11. áÌÅ ÄÅÑË¦ ÎÅÄÏÌ¦ËÉ
×ËÌÀÞÅÎÏÇÏ × X11 ÒÁÓÔÅÒÉÚÁÔÏÒÁ ÂÕÌÉ ÐÒÉÂÒÁÎ¦. T1lib ÔÁËÏÖ ×ËÌÀÞÁ¤
Ð¦ÄÔÒÉÍËÕ ÁÎÔÉÁÌ¦ÁÓÉÎÇÁ.

%package fonts
Summary:	Type 1 fonts
Summary(pl):	Fonty Type 1
Group:		X11/Fonts
Requires(post,postun):fileutils
Requires(post,postun):sed
Requires(post,postun):textutils

%description fonts
Type 1 fonts.

%description fonts -l pl
Zestaw fontów Type 1.

%package devel
Summary:	Development files for t1lib
Summary(pl):	Pliki nag³ówkowe i biblioteki dla t1lib
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para o desenvolvimento com a T1lib
Summary(ru):	òÁÓÔÅÒÉÚÁÔÏÒ ÛÒÉÆÔÏ× Type 1 - ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ
Summary(uk):	òÁÓÔÅÒÉÚÁÔÏÒ ÛÒÉÆÔ¦× Type 1 - ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libt1lib1.3.1-devel

%description devel
The files needed for developing applications using t1lib.

%description devel -l pl
Pliki niezbêdne do tworzenia aplikacji z wykorzystaniem t1lib.

%description devel -l pt_BR
Arquivos de inclusão e bibliotecas para o desenvolvimento de programas
t1lib.

%description devel -l ru
æÁÊÌÙ ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ËÏÍÐÉÌÑÃÉÉ ÉÓÐÏÌØÚÕÀÝÉÈ t1lib ÐÁËÅÔÏ×.

%description devel -l uk
æÁÊÌÉ ÐÏÔÒ¦ÂÎ¦ ÄÌÑ ËÏÍÐ¦ÌÑÃ¦§ ÐÁËÅÔ¦×, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ t1lib.

%package static
Summary:	Static libraries for t1lib
Summary(pl):	Biblioteki statyczne dla t1lib
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com t1lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for t1lib.

%description static -l pl
Biblioteki statyczne dla t1lib.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com t1lib

%description static -l ru
óÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó t1lib.

%description static -l uk
óÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú t1lib.

%package xglyph
Summary:	Test program for t1lib with X11 interface
Summary:	Program testowy dla t1lib z interfejsem X11
Group:		X11/Applications
Requires:	%{name}-devel = %{version}

%description xglyph
Test program for t1lib with X11 interface.

%description xglyph -l pl
Program testowy dla t1lib z interfejsem X11.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__libtoolize}
%{__aclocal}
mv -f aclocal.m4 ac-tools
%{__autoconf}
%configure


%{__make} %{?_without_doc:without_doc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_includedir},%{_xbindir}} \
	$RPM_BUILD_ROOT{%{_t1fontsdir},%{_t1afmdir}} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,5,8}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a Fonts/enc $RPM_BUILD_ROOT%{_datadir}/%{name}
install Fonts/afm/*.afm $RPM_BUILD_ROOT%{_t1afmdir}
install Fonts/type1/*.pfb $RPM_BUILD_ROOT%{_t1fontsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}-fonts
install %{SOURCE2} $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}-fonts

install debian/t1libconfig $RPM_BUILD_ROOT/%{_bindir}/

touch $RPM_BUILD_ROOT/%{_datadir}/%{name}/FontDatabase

for sec in 1 5 8 ; do
	install debian/*.${sec} $RPM_BUILD_ROOT/%{_mandir}/man${sec}/
done

mv -f $RPM_BUILD_ROOT%{_bindir}/xglyph $RPM_BUILD_ROOT%{_xbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post fonts
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap

%postun fonts
cd %{_t1fontsdir}
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null

%files
%defattr(644,root,root,755)
%doc Changes README.t1*
%if %{?_without_doc:0}%{!?_without_doc:1}
%doc doc/*.dvi
%endif
%doc doc/*.{tex,eps,fig}

%attr(755,root,root) %{_bindir}/type1afm
%attr(755,root,root) %{_bindir}/t1libconfig
%attr(755,root,root) %{_libdir}/*.so.*.*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/enc

%config(noreplace) %{_datadir}/%{name}/t1lib.config
%config(noreplace) %{_datadir}/%{name}/FontDatabase

%{_mandir}/man[58]/*
%{_mandir}/man1/type1afm.1*

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
%{_mandir}/man1/xglyph.1*
