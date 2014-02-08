# revision 19660
# category Package
# catalog-ctan /macros/latex/contrib/acronym
# catalog-date 2010-09-10 01:16:09 +0200
# catalog-license lppl
# catalog-version 1.36
Name:		texlive-acronym
Version:	1.36
Release:	3
Summary:	Expand acronyms at least once
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/acronym
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package ensures that all acronyms used in the text are
spelled out in full at least once. It also provides an
environment to build a list of acronyms used. The package is
compatible with pdf bookmarks. The package requires the suffix
package, which in turn requires that it runs under e-TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/acronym/acronym.sty
%doc %{_texmfdistdir}/doc/latex/acronym/README
%doc %{_texmfdistdir}/doc/latex/acronym/acronym.pdf
%doc %{_texmfdistdir}/doc/latex/acronym/acrotest.tex
#- source
%doc %{_texmfdistdir}/source/latex/acronym/acronym.dtx
%doc %{_texmfdistdir}/source/latex/acronym/acronym.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.36-2
+ Revision: 749081
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.36-1
+ Revision: 717789
- texlive-acronym
- texlive-acronym
- texlive-acronym
- texlive-acronym
- texlive-acronym

