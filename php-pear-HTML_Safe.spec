%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Safe
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - strips down dangerous content
Summary(pl):	%{_pearname} - wycinanie niebezpiecznej tre¶ci
Name:		php-pear-%{_pearname}
Version:	0.3.5
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	577357f384abfda65a0b50b04b8d07dd
URL:		http://pear.php.net/package/HTML_Safe/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This parser strips down all potentially dangerous content within HTML.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten parser wycina wszystkie potencjalne niebezpieczne tre¶ci z kodu
HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
