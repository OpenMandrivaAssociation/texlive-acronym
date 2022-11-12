Name:		texlive-acronym
Version:	54758
Release:	1
Summary:	Expand acronyms at least once
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/acronym
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.source.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/acronym/CHANGES
%doc %{_texmfdistdir}/doc/latex/acronym/README
%doc %{_texmfdistdir}/doc/latex/acronym/acronym.pdf
%doc %{_texmfdistdir}/doc/latex/acronym/acrotest.tex
#- source
%doc %{_texmfdistdir}/source/latex/acronym/acronym.dtx
%doc %{_texmfdistdir}/source/latex/acronym/acronym.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
