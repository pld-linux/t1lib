#
# Conditional build:
%bcond_without	doc	# do not build documentation with LaTeX
#
Summary:	A library for character- and string-glyphs from Adobe Type 1 fonts
Summary(pl.UTF-8):	Biblioteka znakowych i łańcuchowych glifów z fontów Adobe Type 1
Summary(pt_BR.UTF-8):	Rasterizador de fontes Type 1
Summary(ru.UTF-8):	Растеризатор шрифтов Type 1
Summary(uk.UTF-8):	Растеризатор шрифтів Type 1
Name:		t1lib
Version:	5.1.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
# Source0-md5:	b1b86b5014364d92ab3b7cee6c81e29d
Source1:	%{name}-fonts.Fontmap
Source2:	%{name}-fonts.fonts.scale
Source3:	%{name}config
Source4:	%{name}config.8
Patch0:		%{name}-doc.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-KernMapSize.patch
Patch3:		%{name}-man.patch
Patch4:		%{name}-xglyph.patch
Patch5:		%{name}-aclocal.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel
%if %{with doc}
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-latex
BuildRequires:	tetex-makeindex
BuildRequires:	tetex-tex-babel
%endif
Requires(post):	fontpostinst >= 0.1-6
Obsoletes:	libt1lib1.3.1
Obsoletes:	libt1lib1.3.1-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_t1fontsdir	%{_fontsdir}/Type1
%define		_t1afmdir	%{_t1fontsdir}/afm
%define		_datadir	/etc
%define		specflags_ia32	 -fomit-frame-pointer

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

%description -l pl.UTF-8
t1lib jest wypuszczoną na LGPL biblioteką do generowania znakowych i
łańcuchowych glifów z fontów Adobe Type 1. t1lib używa większości kodu
rasteryzera X11 (wspomaganego przez IBM), ale niektóre wady tego
rasteryzera zostały usunięte. Niektóre cechy t1lib:
- całkowita niezależność od X11 (tylko program dostarczony do testów
  wymaga X11)
- fonty są znane bibliotece poprzez dodanie do pliku z bazą danych o
  fontach - w czasie uruchamiania
- ścieżki wyszukiwania wszystkich plików wejściowych są konfigurowalne
  w czasie uruchamiania
- znaki są rasteryzowane kiedy są potrzebne
- znaki i całkowite łańcuchy mogą być zrasteryzowane prostym
  wywołaniem funkcji
- przy rasteryzacji łańcuchów opcjonalnie mogą być brane pod uwagę
  informacje o kerningu z plików .afm
- interfejs do informacji o ligaturach z plików .afm
- dołączony program do generowania plików .afm z fontów Type 1
- obroty o dowolny kąt
- wsparcie do rozszerzania i pochylania znaków
- wsparcie dla podkreślania, nadkreślania, przekreślania
- nowe wektory kodowania mogą być wczytane w czasie działania i fonty
  mogą być ponownie zakodowane przy użyciu tych wektorów
- antyaliasing zaimplementowany przy użyciu trzech stopni szarości
  pomiędzy czernią a bielą
- interaktywny program testowy xglyph - w osobnym pakiecie (wymaga X).

%description -l pt_BR.UTF-8
Rasterizador de fontes Type 1 da Adobe.

%description -l ru.UTF-8
T1lib - это библиотека для создания глифов символов и цепочек символов
из шрифтов Adobe Type 1. T1lib использует код растеризатора для X11
подаренного фирмой IBM проекту X11. Но некоторые недостатки
включенного в X11 растеризатора были устранены. T1lib включает также
поддержку антиалиасинга.

%description -l uk.UTF-8
T1lib - це бібліотека для створенння гліфів символів та ланцюжків
символів з шрифтів Adobe Type 1. T1lib використовує код растеризатора
для X11 подарованого фірмою IBM проекту X11. Але деякі недоліки
включеного в X11 растеризатора були прибрані. T1lib також включає
підтримку антиаліасинга.

%package fonts
Summary:	Type 1 fonts
Summary(pl.UTF-8):	Fonty Type 1
Group:		Fonts
Requires(post,postun):	fontpostinst >= 0.1-6
Requires:	%{_fontsdir}/Type1

%description fonts
Type 1 fonts.

%description fonts -l pl.UTF-8
Zestaw fontów Type 1.

%package devel
Summary:	Development files for t1lib
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki dla t1lib
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para o desenvolvimento com a T1lib
Summary(ru.UTF-8):	Растеризатор шрифтов Type 1 - файлы для разработки программ
Summary(uk.UTF-8):	Растеризатор шрифтів Type 1 - файли для розробки програм
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libt1lib1.3.1-devel

%description devel
The files needed for developing applications using t1lib.

%description devel -l pl.UTF-8
Pliki niezbędne do tworzenia aplikacji z wykorzystaniem t1lib.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas para o desenvolvimento de programas
t1lib.

%description devel -l ru.UTF-8
Файлы необходимые для компиляции использующих t1lib пакетов.

%description devel -l uk.UTF-8
Файли потрібні для компіляції пакетів, що використовують t1lib.

%package static
Summary:	Static libraries for t1lib
Summary(pl.UTF-8):	Biblioteki statyczne dla t1lib
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com t1lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for t1lib.

%description static -l pl.UTF-8
Biblioteki statyczne dla t1lib.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com t1lib

%description static -l ru.UTF-8
Статическая библиотека для программирования с t1lib.

%description static -l uk.UTF-8
Статична бібліотека для програмування з t1lib.

%package xglyph
Summary:	Test program for t1lib with X11 interface
Summary(pl.UTF-8):	Program testowy dla t1lib z interfejsem X11
Group:		X11/Applications
Requires:	%{name}-devel = %{version}-%{release}

%description xglyph
Test program for t1lib with X11 interface.

%description xglyph -l pl.UTF-8
Program testowy dla t1lib z interfejsem X11.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

rm -f ac-tools/aclocal.m4

%build
%{__libtoolize}
%{__aclocal} -I ac-tools
%{__autoconf}
%configure

%{__make} %{!?with_doc:without_doc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_datadir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_t1fontsdir},%{_t1afmdir}} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,5,8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a Fonts/enc $RPM_BUILD_ROOT%{_datadir}/%{name}
install Fonts/afm/*.afm $RPM_BUILD_ROOT%{_t1afmdir}
install Fonts/type1/*.pfb $RPM_BUILD_ROOT%{_t1fontsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_t1fontsdir}/Fontmap.%{name}-fonts
install %{SOURCE2} $RPM_BUILD_ROOT%{_t1fontsdir}/fonts.scale.%{name}-fonts

install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}

> $RPM_BUILD_ROOT%{_datadir}/%{name}/FontDatabase

for sec in 1 5; do
	install debian/*.${sec} $RPM_BUILD_ROOT%{_mandir}/man${sec}
done
install %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
fontpostinst Type1

%postun -p /sbin/ldconfig

%post fonts
fontpostinst Type1

%postun fonts
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc Changes README.t1*
%if %{with doc}
%doc doc/*.dvi
%endif
%doc doc/*.{tex,eps,fig}

%attr(755,root,root) %{_bindir}/type1afm
%attr(755,root,root) %{_bindir}/t1libconfig
%attr(755,root,root) %{_libdir}/*.so.*.*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/enc

%ghost %{_datadir}/%{name}/t1lib.config
%ghost %{_datadir}/%{name}/FontDatabase

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
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files xglyph
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xglyph
%{_mandir}/man1/xglyph.1*
