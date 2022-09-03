#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dreamerr
Version  : 1.2.3
Release  : 4
URL      : https://cran.r-project.org/src/contrib/dreamerr_1.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dreamerr_1.2.3.tar.gz
Summary  : Error Handling Made Easy
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Formula
BuildRequires : R-Formula
BuildRequires : buildreq-R

%description
The developer can easily describe the type of argument needed. If the user provides a wrong argument, then an informative error message is prompted with the requested type and the problem clearly stated--saving the user a lot of time in debugging.

%prep
%setup -q -c -n dreamerr
cd %{_builddir}/dreamerr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644254844

%install
export SOURCE_DATE_EPOCH=1644254844
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dreamerr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dreamerr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dreamerr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dreamerr || :


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
