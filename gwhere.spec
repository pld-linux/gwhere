# TODO:
# - is langs.patch still needed?
Summary:	Removable media catalog managment
Summary(de.UTF-8):	Katalog-Verwaltung für Wechselmedien
Summary(es.UTF-8):	Administración de catálogos de medios removibles
Summary(fr.UTF-8):	Gestionnaire de catalogues de media amovibles
Summary(pl.UTF-8):	Zarządzanie katalogiem mediów
Summary(pt.UTF-8):	Gestor de catálogos de media removivel
Name:		gwhere
Version:	0.2.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gwhere.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	73b4ca918a61460758951318acd5eda8
Patch0:		%{name}-langs.patch
Patch1:		%{name}-am_fix.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.gwhere.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Obsoletes:	GWhere
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GWhere allows to manage a database of yours CDs and others removable
media (hard disks, floppy drive, Zip drive, CD-ROM, etc...). With
GWhere it's easy to browse yours CDs or to make quick search without
need to insert yours CDs in the drive at each once.

%description -l de.UTF-8
GWhere erlaubt die Verwaltung einer Datenbank Ihrer CDs und anderer
Wechselmedien (Festplatten, Floppies, Zip-Disketten, CD-ROM usw. ...).
Mit GWhere ist es sehr einfach, Ihre CDs zu durchsuchen oder eine
Schnellsuche durchzuführen ohne jedesmal die CD ins Laufwerk zu
stecken.

%description -l es.UTF-8
GWhere permite administrar una base de datos de tus CDs y otros medios
removibles (disco duros, diskettes, discos Zip, CD-ROMs, etc...). Con
GWhere es fácil navegar tus CDs o realizar búsquedas sin la necesidad
de insertar los CDs en la lectora de a uno por vez.

%description -l fr.UTF-8
GWhere permet de gérer une base de données de vos CD et autres media
amovibles (disques durs, disquettes, disquettes Zip, CD-ROM, etc...).
Avec GWhere il est facile de parcourir vos CDs ou de faire une
recherche rapide sans avoir besoin d'insérer vos CDs dans le lecteur à
chaque fois.

%description -l pl.UTF-8
GWhere to program zarządzający bazą płyt CD oraz innych mediów (takich
jak twarde dyski, dyskietki, dyski Zip itp.). Dzięki GWhere w łatwy
sposób można przeglądać swoje płyty CD i szybko znaleźć potrzebny plik
bez konieczności ciągłego wkładania płyt do napędu.

%description -l pt.UTF-8
O GWhere permite gerir uma base de dados dos seus CDs ou outros tipos
de media removível (discos rígidos, disquetes, drives ZIP, CD-ROM,
etc...). Com o GWhere é fácil explorar os seus CDs ou fazer rápidas
pesquisas sem a necessidade de inserir cada um dos seus CDs na drive.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
chmod +w * -R
#mv po/ar.po po/es.po
#mv po/ar.gmo po/es.gmo
%{__sed} -i "s@gwhere_LDFLAGS = .@gwhere_LDFLAGS =@" src/Makefile.am

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake} 
%configure
%{__sed} -i "s@MSGMERGE_UPDATE =.*@MSGMERGE_UPDATE =echo @g" po/Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/cs-windows-1250

mv -f $RPM_BUILD_ROOT/usr/share/applnk/Applications/gwhere.desktop \
      $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwhere
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
