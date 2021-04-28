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
#     spack install bayescan
#
# You can edit this file again by typing:
#
#     spack edit bayescan
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bayescan(MakefilePackage):
    """BayeScan aims at identifying candidate loci under natural selection from genetic data, using differences in allele frequencies between populations. BayeScan is based on the multinomial-Dirichlet model."""

    homepage = "http://cmpg.unibe.ch/software/BayeScan"
    url      = "http://cmpg.unibe.ch/software/BayeScan/files/BayeScan2.1.zip"

    # notify when the package is updated.
    maintainers = ['alexpacheco']

    version('2.1', sha256='c6bbc52a5a6a30e895951faf2bd6291ca47fdccdc708e693fce02389548d5547')

    build_directory = 'source'
    def edit(self, spec, prefix):
        filter_file(r'-static ',  ' ',  'source/Makefile')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.Rscripts)
        install('source/bayescan_2.1', prefix.bin)
        install('R functions/AFLP_data_functions.r', prefix.Rscripts)
        install('R functions/plot_R.r', prefix.Rscripts)
