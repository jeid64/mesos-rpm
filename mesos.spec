%global commit      eb170184412cb2b7d2aa99c331a3c4f7cfbe14b0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mesos
Version:        0.12.1
Release:        1-rc1.%{shortcommit}%{?dist}
Summary:        

License:        
URL:            http://mesos.apache.org/
# Temporary our fork
Source0:        https://github.com/timothysc/mesos/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  automake
BuildRequires:  leveldb-devel
#TODO: drop bundled libraries
#Requires:       

%description
Apache Mesos is a cluster manager that provides efficient resource
isolation and sharing across distributed applications, or frameworks.
It can run Hadoop, MPI, Hypertable, Spark, and other applications on
a dynamically shared pool of nodes.

%prep
%setup -q

%build
autoreconf -vfi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc

%changelog
* Thu Aug  1 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.12.1-rc1.eb17018
- Initial release
