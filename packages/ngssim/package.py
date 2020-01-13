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
#     spack install ngssim
#
# You can edit this file again by typing:
#
#     spack edit ngssim
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ngssim(Package):
    """NGS data simulator."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/mfumagalli/ngsSim"
    git      = "https://github.com/mfumagalli/ngsSim.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('develop', branch='master')
    version('2018-05-11', commit='dd2007221866ded8827bf1d9744d1b7d57db9b6f')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('zlib')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        mkdirp(prefix.bin)
        install('ngsSim', prefix.bin)
       
