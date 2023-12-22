#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-dreamerr
Version  : 1.4.0
Release  : 11
URL      : https://cran.r-project.org/src/contrib/dreamerr_1.4.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dreamerr_1.4.0.tar.gz
Summary  : Error Handling Made Easy
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Formula
Requires: R-stringmagic
BuildRequires : R-Formula
BuildRequires : R-stringmagic
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The developer can easily describe the type of argument needed. If the user provides a wrong argument, then an informative error message is prompted with the requested type and the problem clearly stated--saving the user a lot of time in debugging.

%prep
%setup -q -n dreamerr
pushd ..
cp -a dreamerr buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703260292

%install
export SOURCE_DATE_EPOCH=1703260292
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dreamerr/DESCRIPTION
/usr/lib64/R/library/dreamerr/INDEX
/usr/lib64/R/library/dreamerr/Meta/Rd.rds
/usr/lib64/R/library/dreamerr/Meta/features.rds
/usr/lib64/R/library/dreamerr/Meta/hsearch.rds
/usr/lib64/R/library/dreamerr/Meta/links.rds
/usr/lib64/R/library/dreamerr/Meta/nsInfo.rds
/usr/lib64/R/library/dreamerr/Meta/package.rds
/usr/lib64/R/library/dreamerr/Meta/vignette.rds
/usr/lib64/R/library/dreamerr/NAMESPACE
/usr/lib64/R/library/dreamerr/NEWS.md
/usr/lib64/R/library/dreamerr/R/dreamerr
/usr/lib64/R/library/dreamerr/R/dreamerr.rdb
/usr/lib64/R/library/dreamerr/R/dreamerr.rdx
/usr/lib64/R/library/dreamerr/doc/dreamerr_introduction.R
/usr/lib64/R/library/dreamerr/doc/dreamerr_introduction.Rmd
/usr/lib64/R/library/dreamerr/doc/dreamerr_introduction.html
/usr/lib64/R/library/dreamerr/doc/index.html
/usr/lib64/R/library/dreamerr/help/AnIndex
/usr/lib64/R/library/dreamerr/help/aliases.rds
/usr/lib64/R/library/dreamerr/help/dreamerr.rdb
/usr/lib64/R/library/dreamerr/help/dreamerr.rdx
/usr/lib64/R/library/dreamerr/help/paths.rds
/usr/lib64/R/library/dreamerr/html/00Index.html
/usr/lib64/R/library/dreamerr/html/R.css
/usr/lib64/R/library/dreamerr/tests/tests_dreamerr.R
