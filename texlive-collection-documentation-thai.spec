# revision 13822
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-thai
Epoch:		1
Version:	20120224
Release:	2
Summary:	Thai documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-thai.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-lshort-thai
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-thai package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780275
- Update to latest release.
- Import texlive-collection-documentation-thai
- Import texlive-collection-documentation-thai

