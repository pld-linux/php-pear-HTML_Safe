%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Safe
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - strips down dangerous content
Summary(pl.UTF-8):	%{_pearname} - wycinanie niebezpiecznej treści
Name:		php-pear-%{_pearname}
Version:	0.10.1
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c544f2a49e7313c00c8bc77e79768e68
URL:		http://pear.php.net/package/HTML_Safe/
BuildRequires:	php-pear-PEAR >= 1:1.6
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-XML_HTMLSax3 >= 3.0.0-0.RC1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This parser strips down all potentially dangerous content within HTML.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten parser wycina wszystkie potencjalne niebezpieczne treści z kodu
HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
