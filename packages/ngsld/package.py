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
#     spack install ngsld
#
# You can edit this file again by typing:
#
#     spack edit ngsld
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ngsld(Package):
    """Calculation of pairwise Linkage Disequilibrium (LD) under a probabilistic framework."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/fgvieira/ngsLD"
    git      = "https://github.com/fgvieira/ngsLD.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('develop', branch='master')
    version('2019-11-08', commit='f5f8d8e3edf89f9bb14ce62278bae6ca795b3613')
    version('2019-04-12', commit='9bcb0ffc61dc12770a78877af1dcba37ef17aab7')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('gsl')
    depends_on('zlib')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        mkdirp(prefix.bin)
        install('ngsLD', prefix.bin)
