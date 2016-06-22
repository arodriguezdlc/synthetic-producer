Name:    synthetic-producer
Version: %{__version}
Release: %{__release}%{?dist}

License: GNU AGPLv3
URL: https://github.com/redBorder/synthetic-producer
Source0: %{name}-%{version}.tar.gz

BuildRequires: maven java-devel

Summary: Get monitor events from kafka and send them to aws cloudwatch service. 
Group:   Services/Monitoring
Requires: java

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build
mvn clean package

%install
mkdir -p %{buildroot}/usr/share/%{name}
mkdir -p %{buildroot}/etc/%{name}
install -D -m 644 src/main/resources/config.json %{buildroot}/etc/%{name}/config.json
install -D -m 644 target/synthetic-producer-*-selfcontained.jar %{buildroot}/usr/share/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root)
/usr/share/%{name}
%defattr(644,root,root)
/etc/%{name}/config.json

%changelog
* Fri Jun 10 2016 Alberto Rodriguez <arodriguez@redborder.com> - 1.1-1
- first spec version
