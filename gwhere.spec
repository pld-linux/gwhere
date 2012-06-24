Summary:	Removable media catalog managment
Summary(de):	Katalog-Verwaltung f�r Wechselmedien
Summary(es):	Administraci�n de cat�logos de medios removibles
Summary(fr):	Gestionnaire de catalogues de media amovibles
Summary(pl):	Zarz�dzanie katalogiem medi�w
Summary(pt):	Gestor de cat�logos de media removivel
Name:		gwhere
Version:	0.1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gwhere.org/download/source/%{name}-%{version}.tar.gz
Patch0:		%{name}-langs.patch
URL:		http://www.gwhere.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	zlib-devel
Obsoletes:	GWhere
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GWhere allows to manage a database of yours CDs and others removable
media (hard disks, floppy drive, Zip drive, CD-ROM, etc...). With
GWhere it's easy to browse yours CDs or to make quick search without
need to insert yours CDs in the drive at each once.

%description -l de
GWhere erlaubt die Verwaltung einer Datenbank Ihrer CDs und anderer
Wechselmedien (Festplatten, Floppies, Zip-Disketten, CD-ROM usw. ...).
Mit GWhere ist es sehr einfach, Ihre CDs zu durchsuchen oder eine
Schnellsuche durchzuf�hren ohne jedesmal die CD ins Laufwerk zu
stecken.

%description -l es
GWhere permite administrar una base de datos de tus CDs y otros medios
removibles (disco duros, diskettes, discos Zip, CD-ROMs, etc...). Con
GWhere es f�cil navegar tus CDs o realizar b�squedas sin la necesidad
de insertar los CDs en la lectora de a uno por vez.

%description -l fr
GWhere permet de g�rer une base de donn�es de vos CD et autres media
amovibles (disques durs, disquettes, disquettes Zip, CD-ROM, etc...).
Avec GWhere il est facile de parcourir vos CDs ou de faire une
recherche rapide sans avoir besoin d'ins�rer vos CDs dans le lecteur �
chaque fois.

%description -l pl
GWhere to program zarz�dzaj�cy baz� p�yt CD oraz innych medi�w (takich
jak twarde dyski, dyskietki, dyski Zip itp.). Dzi�ki GWhere w �atwy
spos�b mo�na przegl�da� swoje p�yty CD i szybko znale�� potrzebny plik
bez konieczno�ci ci�g�ego wk�adania p�yt do nap�du.

%description -l pt
O GWhere permite gerir uma base de dados dos seus CDs ou outros tipos
de media remov�vel (discos r�gidos, disquetes, drives ZIP, CD-ROM,
etc...). Com o GWhere � f�cil explorar os seus CDs ou fazer r�pidas
pesquisas sem a necessidade de inserir cada um dos seus CDs na drive.

%prep
%setup -q
%patch0 -p1
chmod +w * -R
#mv po/ar.po po/es.po
#mv po/ar.gmo po/es.gmo

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} 
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%{_applnkdir}/Applications/%{name}.desktop
