#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-hunspell
Version  : 2.9
Release  : 4
URL      : https://cran.r-project.org/src/contrib/hunspell_2.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/hunspell_2.9.tar.gz
Summary  : High-Performance Stemmer, Tokenizer, and Spell Checker
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MPL-1.1
Requires: R-hunspell-lib
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers

%description
# hunspell
##### *High-Performance Stemmer, Tokenizer, and Spell Checker for R*
[![Build Status](https://travis-ci.org/ropensci/hunspell.svg?branch=master)](https://travis-ci.org/ropensci/hunspell)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/ropensci/hunspell?branch=master&svg=true)](https://ci.appveyor.com/project/jeroen/hunspell)
[![Coverage Status](https://codecov.io/github/ropensci/hunspell/coverage.svg?branch=master)](https://codecov.io/github/ropensci/hunspell?branch=master)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/hunspell)](https://cran.r-project.org/package=hunspell)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/hunspell)](https://cran.r-project.org/package=hunspell)
[![Github Stars](https://img.shields.io/github/stars/ropensci/hunspell.svg?style=social&label=Github)](https://github.com/ropensci/hunspell)

%package lib
Summary: lib components for the R-hunspell package.
Group: Libraries

%description lib
lib components for the R-hunspell package.


%prep
%setup -q -c -n hunspell

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523745808

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523745808
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hunspell
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hunspell
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hunspell
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library hunspell|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/hunspell/AUTHORS
/usr/lib64/R/library/hunspell/DESCRIPTION
/usr/lib64/R/library/hunspell/INDEX
/usr/lib64/R/library/hunspell/Meta/Rd.rds
/usr/lib64/R/library/hunspell/Meta/features.rds
/usr/lib64/R/library/hunspell/Meta/hsearch.rds
/usr/lib64/R/library/hunspell/Meta/links.rds
/usr/lib64/R/library/hunspell/Meta/nsInfo.rds
/usr/lib64/R/library/hunspell/Meta/package.rds
/usr/lib64/R/library/hunspell/Meta/vignette.rds
/usr/lib64/R/library/hunspell/NAMESPACE
/usr/lib64/R/library/hunspell/NEWS
/usr/lib64/R/library/hunspell/R/hunspell
/usr/lib64/R/library/hunspell/R/hunspell.rdb
/usr/lib64/R/library/hunspell/R/hunspell.rdx
/usr/lib64/R/library/hunspell/WORDLIST
/usr/lib64/R/library/hunspell/dict/en_GB.aff
/usr/lib64/R/library/hunspell/dict/en_GB.dic
/usr/lib64/R/library/hunspell/dict/en_US.aff
/usr/lib64/R/library/hunspell/dict/en_US.dic
/usr/lib64/R/library/hunspell/dict/readme.txt
/usr/lib64/R/library/hunspell/doc/index.html
/usr/lib64/R/library/hunspell/doc/intro.R
/usr/lib64/R/library/hunspell/doc/intro.Rmd
/usr/lib64/R/library/hunspell/doc/intro.html
/usr/lib64/R/library/hunspell/help/AnIndex
/usr/lib64/R/library/hunspell/help/aliases.rds
/usr/lib64/R/library/hunspell/help/hunspell.rdb
/usr/lib64/R/library/hunspell/help/hunspell.rdx
/usr/lib64/R/library/hunspell/help/paths.rds
/usr/lib64/R/library/hunspell/html/00Index.html
/usr/lib64/R/library/hunspell/html/R.css
/usr/lib64/R/library/hunspell/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/hunspell/libs/hunspell.so
/usr/lib64/R/library/hunspell/libs/hunspell.so.avx2
/usr/lib64/R/library/hunspell/libs/hunspell.so.avx512
