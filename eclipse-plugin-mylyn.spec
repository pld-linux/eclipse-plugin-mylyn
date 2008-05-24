# TODO:
# - subpackages
# - update desc and summary
%define 	eclipse_ver	3.3
%define		rev		20080402
Summary:	mylyn
Summary(pl.UTF-8):	mylyn
Name:		eclipse-plugin-mylyn
Version:	2.3.2
Release:	0.%{rev}.2
License:	GPL v2
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/mylyn-%{version}.v%{rev}-2100-e%{eclipse_ver}.zip
# Source0-md5:	3edce47988a6758efffd792324e45e1c
URL:		http://www.eclipse.org/mylyn/
BuildRequires:	unzip
Requires:	eclipse >= %{eclipse_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
Mylyn.

% description -l pl.UTF-8
Mylyn.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r * $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/plugins/*.jar
%{_eclipsedir}/features/*.jar
