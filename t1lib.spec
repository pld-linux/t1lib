Summary:	A library for character- and string-glyphs from Adobe Type 1 fonts.
Name:		t1lib
Version:	0.9
Release:	1
Group:		Libraries
Copyright:	GPL
Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
URL:		http://www.windowmaker.org/
BuildRoot:	/tmp/%{name}-%{version}-root

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

%package devel
Summary:	Development files for t1lib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The files needed for developing applications using t1lib.

%package static
Summary:	Static library for t1lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The files needed for developing applications using t1lib.

%prep
%setup -n T1-%{version}
#%patch0 -p1

%build
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/{lib,share,bin,include}
make prefix=$RPM_BUILD_ROOT/usr install

cp -fr Fonts/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr --with-static-lib
make

gzip -9nf Changes README.%{name}-%{version} doc/*

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README.%{name}-%{version},doc/*}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/enc
%dir %{_datadir}/%{name}-%{version}/afm
%dir %{_datadir}/%{name}-%{version}/type1
%dir %{_datadir}/%{name}-%{version}/doc
%config %{_datadir}/%{name}-%{version}/t1lib.config
%{_datadir}/%{name}-%{version}/enc/*
%{_datadir}/%{name}-%{version}/afm/*
%{_datadir}/%{name}-%{version}/type1/*
%doc %{_datadir}/%{name}-%{version}/doc/*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
