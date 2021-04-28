# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install pear
#
# You can edit this file again by typing:
#
#     spack edit pear
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Pear(AutotoolsPackage):
    """Paired-End reAd mergeR (PEAR) is an ultrafast, memory-efficient and highly accurate pair-end read 
       merger. It is fully parallelized and can run with as low as just a few kilobytes of memory.

       PEAR evaluates all possible paired-end read overlaps and without requiring the target fragment size 
       as input. In addition, it implements a statistical test for minimizing false-positive results. 
       Together with a highly optimized implementation, it can merge millions of paired end reads within a 
       couple of minutes on a standard desktop computer."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://cme.h-its.org/exelixis/web/software/pear/"
    url      = "file:///share/Apps/source/spackmirror/pear/pear-0.9.11.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.9.11', sha256='94f4a1835cd75ec6fab83405c2545ddba6b6bb1644579222e9cc2ad57a59d654')

    depends_on('autoconf', type='build')
    depends_on('automake@1.14.1', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')

    def autoreconf(self, spec, prefix):
        autoreconf = which('autoreconf')
        with working_dir(self.configure_directory):
            autoreconf('-ivf')


