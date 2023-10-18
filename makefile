# Makefile to install the ZBar module

PYTHON = python
PIP = pip

install:
    $(PIP) install zbar

.PHONY: install
