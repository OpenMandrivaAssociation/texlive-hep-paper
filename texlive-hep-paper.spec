Name:		texlive-hep-paper
Version:	67632
Release:	1
Summary:	Publications in High Energy Physics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-paper
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-paper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-paper.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-paper.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package aims to provide a single style file containing
most configurations and macros necessary to write appealing
publications in High Energy Physics. Instead of reinventing the
wheel by introducing newly created macros, hep-paper preferably
loads third party packages as long as they are light-weight
enough. For usual publications it suffices to load the
hep-paper package, without optional arguments, in addition to
the article class.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-paper
%{_texmfdistdir}/tex/latex/hep-paper
%doc %{_texmfdistdir}/doc/latex/hep-paper

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
