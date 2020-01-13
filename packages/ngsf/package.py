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
#     spack install ngsf
#
# You can edit this file again by typing:
#
#     spack edit ngsf
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ngsf(Package):
    """Estimation of per-individual inbreeding coefficients under a probabilistic framework."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/fgvieira/ngsF.git"
    git      = "https://github.com/fgvieira/ngsF"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('develop', branch='master')
    version('2019-10-29', commit='b84acdeaed65122daa2712b4124bbd2e709e9c58')
    version('2018-05-11', commit='b5388c42d4f134f32022dae810cf5bd8434efa73')
    version('1.2.0', tag='v1.2.0')
    version('1.1.0', tag='v1.1.0')
    version('1.0.0', tag='v1.0.0')

    # FIXME: Add dependencies if required.
    depends_on('gsl')
    depends_on('htslib')
    depends_on('zlib')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('test')
        mkdirp(prefix.bin)
        install('ngsF', prefix.bin)
