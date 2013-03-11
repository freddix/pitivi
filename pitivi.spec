Summary:	Video editor
Name:		pitivi
Version:	0.15.2
Release:	2
License:	LGPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pitivi/0.15/%{name}-%{version}.tar.xz
# Source0-md5:	a5cb84f3bae7b8d12a31742461b428f4
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
Requires:	gstreamer010-gnonlin
Requires:	gstreamer010-plugins-good
Requires:	python-gstreamer010
Requires:	python-pycairo
Requires:	python-pygoocanvas
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
Requires:	python-pyxdg
Requires:	python-setuptools
Requires:	zope-interface
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PiTiVi is a program for video editing based on the GStreamer.

%prep
%setup -q

%build
%configure
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
%{_libdir}/pitivi
%{_datadir}/mime/packages/pitivi.xml
%{_datadir}/pitivi
%{_desktopdir}/pitivi.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/%{name}.1*

