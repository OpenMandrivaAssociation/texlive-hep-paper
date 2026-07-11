%global tl_name hep-paper
%global tl_revision 76220

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Publications in High Energy Physics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-paper
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-paper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-paper.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-paper.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package aims to provide a single style file containing most
configurations and macros necessary to write appealing publications in
High Energy Physics. Instead of reinventing the wheel by introducing
newly created macros, hep-paper preferably loads third party packages as
long as they are light-weight enough. For usual publications it suffices
to load the hep-paper package, without optional arguments, in addition
to the article class.

