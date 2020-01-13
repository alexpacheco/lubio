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
#     spack install ngsf-hmm
#
# You can edit this file again by typing:
#
#     spack edit ngsf-hmm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class NgsfHmm(Package):
    """Estimation of per-individual inbreeding tracts under a probabilistic framework."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/fgvieira/ngsF-HMM"
    git      = "https://github.com/fgvieira/ngsF-HMM.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('devel', branch='master')
    version('2019-11-20', commit='eeee71f25a13073797c260da9de28ac856631015')
    version('2019-04-12', commit='4837a6cd9d7d0dbf06b9ddcfc4f1ae768f3b182d')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('gsl')
    depends_on('zlib')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        mkdirp(prefix.bin)
        install('ngsF-HMM', prefix.bin)
