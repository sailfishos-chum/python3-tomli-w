# Adapted for SaifishOS
# + Disable check by default
# + Remove redundant python-tomli-w package

Name:           python3-tomli-w
Version:        1.0.0
Release:        1
Summary:        A Python library for writing TOML

License:        MIT
URL:            https://github.com/hukkin/tomli-w
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)
#BuildRequires:  python3dist(packaging)

%description
Tomli-W is a Python library for writing TOML. It is a write-only counterpart
to Tomli, which is a read-only TOML parser. Tomli-W is fully compatible
with TOML v1.0.0.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream


#%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tomli_w


%check
%if %{with check}
%tox
%endif


%files -n python3-tomli-w -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE
