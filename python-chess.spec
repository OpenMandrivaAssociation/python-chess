Name:		python-chess
Version:	1.11.2
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/chess/chess-%{version}.tar.gz
Summary:	A chess library with move generation and validation, Polyglot opening book probing, PGN reading and writing, Gaviota tablebase probing, Syzygy tablebase probing, and XBoard/UCI engine communication.
URL:		https://pypi.org/project/chess/
License:	GPL-3.0+
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A chess library with move generation and validation, Polyglot opening book probing, PGN reading and writing, Gaviota tablebase probing, Syzygy tablebase probing, and XBoard/UCI engine communication.

%files
%{py_sitedir}/chess
%{py_sitedir}/chess-*.*-info
