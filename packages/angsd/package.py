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
#     spack install angsd
#
# You can edit this file again by typing:
#
#     spack edit angsd
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Angsd(Package):
    """Angsd is a program for analysing NGS data. The software can handle a
       number of different input types from mapped reads to imputed genotype
       probabilities. Most methods take genotype uncertainty into account
       instead of basing the analysis on called genotypes. This is especially
       useful for low and medium depth data."""

    homepage = "https://github.com/ANGSD/angsd"
    git      = "https://github.com/ANGSD/angsd.git"

    version('master',  branch='master')
    version('2019-11-05', commit='d22308aa5a3f3b5a1e1759c5770b5a0c7c95a226')
    version('0.921', sha256='8892d279ce1804f9e17fe2fc65a47e5498e78fc1c1cb84d2ca2527fd5c198772')
    version('0.919', sha256='c2ea718ca5a5427109f4c3415e963dcb4da9afa1b856034e25c59c003d21822a')

    depends_on('htslib')
    conflicts('^htslib@1.6:', when='@0.919')

    def setup_run_environment(self, env):
        env.set('R_LIBS', self.prefix.R)

    def edit(self, spec, prefix):
       makefile = FileFilter('Makefile')
       makefile.filter('HTS_INCDIR=$(realpath $(HTSSRC))', 'HTS_INCDIR=$(realpath $(HTSSRC))/include')
       makefile.filter('HTS_LIBDIR=$(realpath $(HTSSRC))', 'HTS_LIBDIR=$(realpath $(HTSSRC))/lib')

    def install(self, spec, prefix):
        make()
        mkdirp(prefix.bin)
        install('angsd', join_path(prefix.bin))
        install_tree('R', prefix.R)
        install_tree('RES', prefix.RES)
        install_tree('scripts', prefix.scripts)
