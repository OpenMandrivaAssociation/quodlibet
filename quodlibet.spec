Summary: 	Advanced, elegant jukebox style music player
Name:		quodlibet
Version:	2.2.1
Release: 	%mkrel 1
License:	GPLv2+
Group:		Sound
URL:		http://code.google.com/p/quodlibet/
Source0:	http://quodlibet.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	pygtk2.0-devel
BuildRequires:	pyvorbis
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gstreamer0.10-python
BuildRequires:	mutagen
BuildRequires:	python-dbus
BuildRequires:	liboil-devel
BuildRequires:	python-feedparser
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
Requires:	python-dbus
Requires:	python-feedparser
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%build
export CFLAGS="%{optflags}"

python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --prefix=%{_prefix}

# (tpg) install icons
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 build/lib/quodlibet/images/exfalso.png %{buildroot}%{_datadir}/pixmaps
install -m 644 build/lib/quodlibet/images/%{name}.png %{buildroot}%{_datadir}/pixmaps

# (tpg) get rid of extension
sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*
sed -i -e 's/^Icon=exfalso.png$/Icon=exfalso/g' %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

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
%doc NEWS README HACKING
%{_bindir}/%{name}
%{_bindir}/exfalso
%{py_sitedir}/%{name}
%{py_sitedir}/%{name}*.egg-info
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
