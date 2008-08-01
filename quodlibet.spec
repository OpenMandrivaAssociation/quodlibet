%define name	quodlibet
%define version	1.0
%define release %mkrel 6

Name: 	 	%{name}
Summary: 	Advanced, elegant jukebox style music player
Version: 	%{version}
Release: 	%{release}

Source:		http://www.sacredchao.net/~piman/software/%{name}-%{version}.tar.bz2
URL:		http://www.sacredchao.net/quodlibet/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	python
BuildRequires:	pygtk2.0-devel
BuildRequires:	pyvorbis
BuildRequires:	gtk2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gstreamer0.10-python
BuildRequires:	mutagen
Requires:	python >= 2.5
Requires:	pygtk2.0
Requires:	python-ctypes
Requires:	pyvorbis
Requires:	gstreamer0.10-python
Requires:	python-feedparser
Requires:	mutagen
# for Replay Gain plugin
Requires:       vorbisgain
# for iPod device support
Requires:       python-gpod
# for CDDB plugin
Requires:       python-CDDB

%description
Quod Libet is a GTK+-based audio player written in Python. It's designed
around the idea that you know better than we do how to organize your music.
It lets you make playlists based on regular expressions (don't worry,
regular searches work too). It lets you display and edit any tags you want
in the file.

It supports Ogg Vorbis and MP3 by default, but other formats (FLAC, Musepack,
Wavepack, MPEG-4/AAC and MOD are available through gstreamer0.10 plugins.

Quod Libet easily scales to libraries of thousands of songs. It also supports
most of the features you expect from a modern media player, like Unicode
support, gapless playback, multimedia keys, and an OSD. 

%prep
%setup -q
perl -pi -e 's/lib\/quodlibet/%{_lib}\/quodlibet/' Makefile
perl -pi -e 's/^-intltool-merge.*//' Makefile
perl -pi -e 's/usr\/local/usr/g' Makefile

%build
pushd mmkeys
make mmkeyspy.c
CFLAGS="%{optflags}" %{__python} setup.py build
cp build/lib*/mmkeys.so ../_mmkeys.so
popd

%make
%make extensions

%install
rm -rf $RPM_BUILD_ROOT
export PATH=/usr/bin:/usr/sbin:/bin:/sbin
#DESTDIR=%buildroot make install
%ifarch x86_64 ppc64
make install PREFIX=/usr TODEP=lib64/quodlibet DESTDIR=%{buildroot}
%else
make install PREFIX=/usr TODEP=lib/quodlibet DESTDIR=%{buildroot}
%endif

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="AudioPlayer" \
  --add-category="AudioVideo;Audio;Player" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
convert -size 48x48 exfalso.png $RPM_BUILD_ROOT/%_liconsdir/exfalso.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
convert -size 32x32 exfalso.png $RPM_BUILD_ROOT/%_iconsdir/exfalso.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png
convert -size 16x16 exfalso.png $RPM_BUILD_ROOT/%_miconsdir/exfalso.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README
%{_bindir}/%name
%{_bindir}/exfalso
%{_datadir}/%name
%{_mandir}/man1/*
%{_libdir}/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_liconsdir}/%name.png
%{_liconsdir}/exfalso.png
%{_iconsdir}/%name.png
%{_iconsdir}/exfalso.png
%{_miconsdir}/%name.png
%{_miconsdir}/exfalso.png


