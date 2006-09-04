%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Safe
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - strips down dangerous content
Summary(pl):	%{_pearname} - wycinanie niebezpiecznej tre¶ci
Name:		php-pear-%{_pearname}
Version:	0.9.9
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}beta.tgz
# Source0-md5:	8bbe8a4b78d1f0f4a08aa3a4f97b242b
URL:		http://pear.php.net/package/HTML_Safe/
BuildRequires:	php-pear-PEAR
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

%description -l pl
Ten parser wycina wszystkie potencjalne niebezpieczne tre¶ci z kodu
HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
