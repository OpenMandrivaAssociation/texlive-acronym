Name:		texlive-acronym
Version:	1.36
Release:	1
Summary:	Expand acronyms at least once
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/acronym
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acronym.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package ensures that all acronyms used in the text are
spelled out in full at least once. It also provides an
environment to build a list of acronyms used. The package is
compatible with pdf bookmarks. The package requires the suffix
package, which in turn requires that it runs under e-TeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
