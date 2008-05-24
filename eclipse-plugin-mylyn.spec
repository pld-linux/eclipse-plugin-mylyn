# TODO:
# - subpackages
# - pl desc and summary
%define 	eclipse_ver	3.3
%define		rev		20080402
Summary:	Task-Focused Interface for Eclipse
Name:		eclipse-plugin-mylyn
Version:	2.3.2
Release:	0.%{rev}.3
License:	EPL v1.0
Group:		Development/Tools
Source0:	http://download.eclipse.org/tools/mylyn/update/e%{eclipse_ver}/mylyn-%{version}.v%{rev}-2100-e%{eclipse_ver}.zip
# Source0-md5:	3edce47988a6758efffd792324e45e1c
URL:		http://www.eclipse.org/mylyn/
BuildRequires:	unzip
Requires:	eclipse >= %{eclipse_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
Mylyn is a Task-Focused Interface for Eclipse that reduces information
overload and makes multi-tasking easy. It does this by making tasks a
first class part of Eclipse, and integrating rich and offline editing
for repositories such as Bugzilla, Trac, and JIRA. Once your tasks are
integrated, Mylyn monitors your work activity to identify information
relevant to the task-at-hand, and uses this task context to focus the
Eclipse UI on the interesting information, hide the uninteresting, and
automatically find what's related. This puts the information you need
to get work done at your fingertips and improves productivity by
reducing searching, scrolling, and navigation. By making task context
explicit Mylyn also facilitates multitasking, planning, reusing past
efforts, and sharing expertise.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -a features/* $RPM_BUILD_ROOT%{_eclipsedir}/features
cp -a plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/plugins/*.jar
%{_eclipsedir}/features/*.jar
