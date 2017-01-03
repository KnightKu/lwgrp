ACLOCAL_AMFLAGS = -I m4

SUBDIRS = src
EXTRA_DIST = 

dist_pkgdata_DATA = README LICENSE.TXT

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = liblwgrp.pc
BUILD_DIRS = BUILD BUILDROOT RPMS SOURCES SPECS SRPMS
$(BUILD_DIRS):
	mkdir $@
rpm: dist $(BUILD_DIRS)
	mv $(distdir).tar.gz $(top_builddir)/SOURCES
	rpmbuild -ba --define="_topdir `pwd`" lwgrp.spec
