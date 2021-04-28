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
#     spack install bayestraits
#
# You can edit this file again by typing:
#
#     spack edit bayestraits
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bayestraits(Package):
    """BayesTraits is a computer package for performing analyses of trait evolution among groups of species for which a phylogeny or sample of phylogenies is available."""

    homepage = "http://www.evolution.rdg.ac.uk/BayesTraitsV3.0.2/BayesTraitsV3.0.2.html"
    url      = "http://www.evolution.rdg.ac.uk/BayesTraitsV3.0.2/Files/BayesTraitsV3.0.2-Linux.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['alexpacheco']

    version('3.0.2', sha256='8b4dbd48583f970d3a4e363685940a9c99d412be1b2e96eb682294f751b4fa51')
    version('3.0.1', sha256='a99b8aba77151517f655ff9cd44f317d56104fe4f9bfce3990eab12af2bd9852')

    def url_for_version(self, version):
        url = "http://www.evolution.rdg.ac.uk/BayesTraitsV{0}/Files/BayesTraitsV{0}-Linux.tar.gz"
        return url.format(version.up_to(3), version)

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        mkdir(prefix.bin)
        mkdir(prefix.examples)
             
        install('BayesTraitsV3', prefix.bin)
        install('*txt', prefix.examples)
        install('*trees', prefix.examples)
