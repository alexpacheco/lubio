# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
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
#     spack install bartender
#
# You can edit this file again by typing:
#
#     spack edit bartender
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bartender(Package):
    """A fast and accurate clustering algorithm to count barcode reads."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/LaoZZZZZ/bartender-1.1"
    git      = "https://github.com/LaoZZZZZ/bartender-1.1.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.1', commit='ddfb2e52bdf92258dd837ab8ee34306e9fb45b81')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        #make('install')
        mkdirp(prefix.bin)
        for package in ['bartender_single','bartender_extractor',
                        'bartender_combiner','bartender_single_com',
                         'bartender_extractor_com','bartender_combiner_com']:
            install(package, prefix.bin)
