Summary:	Video editor
Name:		pitivi
Version:	0.91
Release:	0.2
License:	LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/0.91/%{name}-%{version}.tar.xz
# Source0-md5:	30f520587885d231aeb9a7ddb2585e45
URL:		http://www.pitivi.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	rpm-pythonprov
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	clutter
Requires:	gobject-introspection
Requires:	gstreamer-editing-services
Requires:	gstreamer-gnonlin
Requires:	gstreamer-plugins-good
Requires:	gtk+3
Requires:	python-numpy
Requires:	python-pygobject3
Requires:	python-pyxdg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PiTiVi is a program for video editing based on the GStreamer.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_mime_database
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pitivi
%attr(755,root,root) %{_libdir}/pitivi/python/pitivi/timeline/renderer.so
%dir %{_libdir}/pitivi
%dir %{_libdir}/pitivi/python
%dir %{_libdir}/pitivi/python/pitivi
%dir %{_libdir}/pitivi/python/pitivi/dialogs
%dir %{_libdir}/pitivi/python/pitivi/timeline
%dir %{_libdir}/pitivi/python/pitivi/undo
%dir %{_libdir}/pitivi/python/pitivi/utils
%{_libdir}/pitivi/python/pitivi/*.py*
%{_libdir}/pitivi/python/pitivi/dialogs/*.py*
%{_libdir}/pitivi/python/pitivi/timeline/*.py*
%{_libdir}/pitivi/python/pitivi/undo/*.py*
%{_libdir}/pitivi/python/pitivi/utils/*.py*

%{_datadir}/mime/packages/pitivi.xml
%{_datadir}/pitivi
%{_desktopdir}/pitivi.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/%{name}.1*

