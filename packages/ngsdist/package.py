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
#     spack install ngsdist
#
# You can edit this file again by typing:
#
#     spack edit ngsdist
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ngsdist(Package):
    """Estimation of pairwise distances under a probabilistic framework."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/fgvieira/ngsDist.git"
    git      = "https://github.com/fgvieira/ngsDist"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('develop', branch='master')
    version('2019-11-18', commit='bd04e2c1ccbe3e111fff0c53974a068aacd33db3')
    version('2018-07-20', commit='5d966d38dd30933ff5418fc484ba6fc4ce991786')

    # FIXME: Add dependencies if required.
    depends_on('gsl')
    depends_on('zlib')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        mkdirp(prefix.bin)
        install('ngsDist', prefix.bin)
