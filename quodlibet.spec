%define	debug_package	%nil

Summary: 	Advanced, elegant jukebox style music player
Name:		quodlibet
Version:	4.2.1
Release: 	1
License:	GPLv2+
Group:		Sound
URL:		https://quodlibet.readthedocs.io/
Source0:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	gtk+3.0
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	mutagen
BuildRequires:	python-dbus
BuildRequires:	pkgconfig(xtst)
Requires:	python-gi-cairo
Requires:	python-feedparser
Requires:	mutagen
Requires: zsh
# for Replay Gain plugin
Requires:       vorbisgain
# for CDDB plugin
Requires:       python-CDDB
Requires:	python-dbus
Recommends: zeitgeist
Recommends: python-pyinotify


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


%package -n exfalso
Summary:    Tag editor for musical files
Group:      Sound/Utilities
Requires:   python3
Requires:   pythonegg(3)(mutagen)
Requires:   quodlibet >= %{version}
# for musicbrainz plugin
Requires:   pythonegg(3)(musicbrainzngs)
Conflicts:  exfaslo < %{version}

%description -n exfalso
Ex Falso is a program that uses the same tag editing backend as Quod Libet,
but isn't connected to an audio player. If you're perfectly happy with your
favorite player and just want something that can handle tagging, Ex Falso
is for you.

%package gstbe
Summary:    GStreamer backend for quodlibet
Group:      Sound/Utilities
Requires:   quodlibet >= %{version}
Recommends: gstreamer1.0-plugins-good
Recommends: gstreamer1.0-plugins-bad
Provides:   quodlibet-be = %{version}

%description gstbe
This meta package installs neccessary packages to provide gstreamer backend support.

%package xinebe
Summary:    Xine backend for quodlibet
Group:      Sound/Utilities
Requires:   quodlibet >= %{version}
Requires:   xine1.2-common
Provides:   quodlibet-be = %{version}

%description xinebe
This meta package installs neccessary packages to provide xine backend support.

%prep
%setup -q
%autopatch -p1

%build
%py3_build

%install
%py3_install

%find_lang %{name}

# move zsh-completion files
mkdir %{buildroot}%{_datadir}/zsh/site-functions/
mv %{buildroot}%{_datadir}/zsh/vendor-completions/_quodlibet %{buildroot}%{_datadir}/zsh/site-functions/


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
