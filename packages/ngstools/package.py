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
#     spack install ngstools
#
# You can edit this file again by typing:
#
#     spack edit ngstools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ngstools(Package):
    """Programs to analyse NGS data for population genetics purposes."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/mfumagalli/ngsTools"
    git      = "https://github.com/mfumagalli/ngsTools.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('develop', branch='master', submodules=True)
    version('2019-06-24', commit='634599fc729ad6385a83bf6071d6aeb48d51bd28', submodules=True)

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('angsd')
    depends_on('gsl')
    depends_on('htslib')
    depends_on('zlib')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        mkdirp(prefix.bin)
        with working_dir('ngsDist'):
            make()
            install('ngsDist', prefix.bin)
        with working_dir('ngsF'):
            make()
            install('ngsF', prefix.bin)
        with working_dir('ngsF-HMM'):
            make()
            install('ngsF-HMM', prefix.bin)
        with working_dir('ngsLD'):
            make()
            install('ngsLD', prefix.bin)
        with working_dir('ngsPopGen'):
            make()
            for pack in [ 'ngs2dSFS', 'ngsCovar', 'ngsFST', 'ngsStat'] :
                install(pack, prefix.bin)
        with working_dir('ngsSim'):
            make()
            install('ngsSim', prefix.bin)
        with working_dir('ngsUtils'):
            make()
            for pack in [ 'GetSubSim', 'GetSubGeno', 'GetSwitchedGeno', 'GetMergedGeno' ] :
                install(pack, prefix.bin)
