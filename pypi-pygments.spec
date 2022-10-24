#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pygments
Version  : 2.13.0
Release  : 95
URL      : https://files.pythonhosted.org/packages/e0/ef/5905cd3642f2337d44143529c941cc3a02e5af16f0f65f81cbef7af452bb/Pygments-2.13.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e0/ef/5905cd3642f2337d44143529c941cc3a02e5af16f0f65f81cbef7af452bb/Pygments-2.13.0.tar.gz
Summary  : Pygments is a syntax highlighting package written in Python.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-pygments-bin = %{version}-%{release}
Requires: pypi-pygments-license = %{version}-%{release}
Requires: pypi-pygments-python = %{version}-%{release}
Requires: pypi-pygments-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Welcome to Pygments
===================
This is the source of Pygments.  It is a **generic syntax highlighter** written
in Python that supports over 500 languages and text formats, for use in code
hosting, forums, wikis or other applications that need to prettify source code.

%package bin
Summary: bin components for the pypi-pygments package.
Group: Binaries
Requires: pypi-pygments-license = %{version}-%{release}

%description bin
bin components for the pypi-pygments package.


%package license
Summary: license components for the pypi-pygments package.
Group: Default

%description license
license components for the pypi-pygments package.


%package python
Summary: python components for the pypi-pygments package.
Group: Default
Requires: pypi-pygments-python3 = %{version}-%{release}

%description python
python components for the pypi-pygments package.


%package python3
Summary: python3 components for the pypi-pygments package.
Group: Default
Requires: python3-core
Provides: pypi(pygments)

%description python3
python3 components for the pypi-pygments package.


%prep
%setup -q -n Pygments-2.13.0
cd %{_builddir}/Pygments-2.13.0
pushd ..
cp -a Pygments-2.13.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664210185
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pygments
cp %{_builddir}/Pygments-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pygments/0c271aeb0199762f47e124c8960b830ad5a97ce0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pygmentize

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pygments/0c271aeb0199762f47e124c8960b830ad5a97ce0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
