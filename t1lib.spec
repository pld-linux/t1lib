Summary:	A library for character- and string-glyphs from Adobe Type 1 fonts.
Name:		t1lib
Version:	0.9
Release:	1
Group:		Libraries
Copyright:	GPL
Vendor:		«unknown»
Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
Patch0:		t1lib-0.7.1-beta-config.patch
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
Require:	%{name} = %{version}

%description devel
The files needed for developing applications using t1lib.

%prep
%setup -n T1-%{version}
%patch0 -p1

%build
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/{lib,share,bin,include}
make prefix=$RPM_BUILD_ROOT/usr install
cp -fr Fonts/* $RPM_BUILD_ROOT/usr/share/t1lib-0.8
CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr --with-static-lib
make

%clean
rm -r $RPM_BUILD_ROOT

%files
%doc Changes LGPL LICENSE README.t1lib-0.8-beta doc/*
%attr(-,root,root) /usr/bin/*
%attr(-,root,root) /usr/lib/*.so.*
%attr(-,root,root) %dir /usr/share/t1lib-0.8
%attr(-,root,root) %config /usr/share/t1lib-0.8/t1lib.config
%attr(-,root,root) %dir /usr/share/t1lib-0.8/enc
%attr(-,root,root) /usr/share/t1lib-0.8/enc/*
%attr(-,root,root) %dir /usr/share/t1lib-0.8/afm
%attr(-,root,root) /usr/share/t1lib-0.8/afm/*
%attr(-,root,root) %dir /usr/share/t1lib-0.8/type1
%attr(-,root,root) /usr/share/t1lib-0.8/type1/*
%attr(-,root,root) %dir /usr/share/t1lib-0.8/doc
%attr(-,root,root) %doc /usr/share/t1lib-0.8/doc/*

%files devel
%attr(-,root,root) /usr/include/*
%attr(-,root,root) /usr/lib/*.a
%attr(-,root,root) /usr/lib/*.so

%changelog
* Tue Jul 21 1998 Kjetil Wiekhorst Jørgensen <jorgens@pvv.org>
- Initial relaese as RPM.
