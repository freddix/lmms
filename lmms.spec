Summary:	Linux MultiMedia studio
Name:		lmms
Version:	0.4.13
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/lmms/%{name}-%{version}.tar.bz2
# Source0-md5:	80db0dc5263041d443f474220410991f
Patch0:		%{name}-include.patch
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	fluidsynth-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	qt-build
BuildRequires:	wine-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LMMS aims to be a free alternative to popular (but commercial and
closed-source) programs like FruityLoops, Cubase and Logic giving you
the ability of producing music with your computer by
creating/synthesizing sounds, arranging samples, using effects,
playing live with keyboard and much more...

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT{%{_libdir}/%{name}/*.la,%{_includedir}}

install -D data/themes/default/icon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/lmms.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/ladspa
%attr(755,root,root) %{_libdir}/lmms/*.so
%attr(755,root,root) %{_libdir}/lmms/ladspa/*.so
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/lmms/RemoteVstPlugin
%endif
%attr(755,root,root) %{_libdir}/lmms/RemoteZynAddSubFx
%{_datadir}/%{name}
%{_datadir}/mime/packages/lmms.xml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/lmms.1*

