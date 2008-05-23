# TODO:
# - subpackages
# - update desc and summary
%define 	eclipse_ver	3.3
%define		rev		20080402
Summary:	mylyn
Summary(pl.UTF-8):	mylyn
Name:		eclipse-plugin-mylyn
Version:	2.3.2
Release:	0.%{rev}.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/features/org.eclipse.mylyn_feature_%{version}.v%{rev}-2100.jar
# Source0-md5:	996dd16052196debbd9b9806deccbb2f
Source1:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/features/org.eclipse.mylyn.context_feature_%{version}.v%{rev}-2100.jar
# Source1-md5:	58e5fd875f673733b63f9bfb656d129c
Source2:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/features/org.eclipse.mylyn.ide_feature_%{version}.v%{rev}-2100.jar
# Source2-md5:	0579b45bb8e6c6a313eb703b93f04c72
Source3:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/features/org.eclipse.mylyn.java_feature_%{version}.v%{rev}-2100.jar
# Source3-md5:	455528d87fb1ab9d2ff842d7285a8458
Source4:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/features/org.eclipse.mylyn.pde_feature_%{version}.v%{rev}-2100.jar
# Source4-md5:	b6d022a8e643acb5bb0e5452caf58c1f
Source5:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/features/org.eclipse.mylyn.bugzilla_feature_%{version}.v%{rev}-2100.jar
# Source5-md5:	248453e013cdf8305e364b12624a5a13
Source6:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/features/org.eclipse.mylyn.trac_feature_%{version}.v%{rev}-2100.jar
# Source6-md5:	0af24272969792346f712f51982298dc
URL:		http://www.eclipse.org/mylyn/
Requires:	eclipse >= %{eclipse_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
Mylyn.

% description -l pl.UTF-8
Mylyn.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

install %{SOURCE0} $RPM_BUILD_ROOT%{_eclipsedir}/plugins
install %{SOURCE1} $RPM_BUILD_ROOT%{_eclipsedir}/plugins
install %{SOURCE2} $RPM_BUILD_ROOT%{_eclipsedir}/plugins
install %{SOURCE3} $RPM_BUILD_ROOT%{_eclipsedir}/plugins
install %{SOURCE4} $RPM_BUILD_ROOT%{_eclipsedir}/plugins
install %{SOURCE5} $RPM_BUILD_ROOT%{_eclipsedir}/plugins
install %{SOURCE6} $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/plugins/*
