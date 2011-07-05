%define name    gitbuster
%define version 2.1
%define beta	b5
%define release %mkrel 0.%beta.1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Python Qt4 frontend for git filter-branch and git cherry-pick
License:	GPLv3
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/gitbuster/
Source0: 	http://pypi.python.org/packages/source/g/gitbuster/gitbuster-%{version}%{beta}.tar.gz
Requires:       python-gitpython
Requires:       python-gfbi_core
BuildRequires:  python-qt4-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
" If there's something strange / In your history / Who you gonna call ? /
GitBuster! "

%prep
%setup -q -n %{name}-%{version}%{beta}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS.txt CHANGELOG LICENSE.txt README.rst
%{_bindir}/gitbuster
%{python_sitelib}/gitbuster
%{python_sitelib}/gitbuster-%{version}%{beta}-py%{pyver}.egg-info
