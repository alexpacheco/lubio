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
#     spack install ngspopgen
#
# You can edit this file again by typing:
#
#     spack edit ngspopgen
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ngspopgen(Package):
    """Population genetics analyses from NGS data."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/mfumagalli/ngsPopGen"
    git      = "https://github.com/mfumagalli/ngsPopGen.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('develop', branch='master')
    version('2018-08-14', commit='9ee3a6d5e733c1e248e81bfc21514b0527da967b')
    version('2018-03-20', commit='8ead2d469f42942f413f6c93664b568d2eb8a124')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('zlib')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        mkdirp(prefix.bin)
        for pack in [ 'ngs2dSFS', 'ngsCovar', 'ngsFST', 'ngsStat'] :
            install(pack, prefix.bin)
