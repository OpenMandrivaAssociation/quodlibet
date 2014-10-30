%define	debug_package	%nil

Summary: 	Advanced, elegant jukebox style music player
Name:		quodlibet
Version:	3.2.2
Release: 	1
License:	GPLv2+
Group:		Sound
URL:		http://code.google.com/p/quodlibet/
Source0:	http://quodlibet.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	gtk+3.0
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	mutagen
BuildRequires:	python2-dbus
BuildRequires:	pkgconfig(xtst)
Requires:	python2-gi-cairo
Requires:	python2-feedparser
Requires:	mutagen
# for Replay Gain plugin
Requires:       vorbisgain
# for CDDB plugin
Requires:       python-CDDB
Requires:	python2-dbus
Requires:	python2-feedparser

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
%apply_patches

%build
export CFLAGS="%{optflags}"

python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}

# (tpg) install icons
#install -dm 755 %{buildroot}%{_datadir}/pixmaps
#install -m 644 build/lib/quodlibet/images/exfalso.png %{buildroot}%{_datadir}/pixmaps
#install -m 644 build/lib/quodlibet/images/%{name}.png %{buildroot}%{_datadir}/pixmaps

# (tpg) get rid of extension
sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*
sed -i -e 's/^Icon=exfalso.png$/Icon=exfalso/g' %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README
%{_bindir}/%{name}
%{_bindir}/exfalso
%{_bindir}/operon
%{py2_puresitedir}/%{name}
%{py2_puresitedir}/%{name}*.egg-info
%{_datadir}/appdata/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/dbus-1/services/net.sacredchao.QuodLibet.service
%{_datadir}/gnome-shell/search-providers/quodlibet-search-provider.ini
%{_mandir}/man1/*
