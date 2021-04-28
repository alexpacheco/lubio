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
#     spack install xcrysden-1-6-2-linux-x86-64-shared
#
# You can edit this file again by typing:
#
#     spack edit xcrysden-1-6-2-linux-x86-64-shared
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os.path 

from spack import *


class Xcrysden(Package):
    """XCrySDen is a crystalline and molecular structure visualisation program aiming at display of isosurfaces and contours, which can be superimposed on crystalline structures and interactively rotated and manipulated."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.xcrysden.org"
    url      = "http://www.xcrysden.org/download/xcrysden-1.6.2-linux_x86_64-shared.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('1.6.2',  sha256='72c9ca6263da73e7c3006924c6a07438fa2e4f8506aa6e070f560d760f3f99d0')
    version('1.6.1',  sha256='21c392b2f26cc3b7e0fe5d888a9b7de6564b4032c29e9aff746549d18552b0a1')
    version('1.6.0',  sha256='ffc36561ffc61b97388756d4a1120ef77d6987e015d2a8d0c404c4ff37ab9aa5')
    version('1.5.60', sha256='e6677f5523919ac4ce6a29490810f56678bc037450af69c8274baa6b0be8d5d2')

    def url_for_version(self, version):
        url = "http://www.xcrysden.org/download/xcrysden-{0}-linux_x86_64-shared.tar.gz"
        return url.format(version)

    # FIXME: Add dependencies if required.
    depends_on('tcl', type='link')
    depends_on('tk', type='run')
    depends_on('togl', type='run')
    depends_on('fftw ~mpi', type='run')

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix)
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.spec['togl'].prefix.lib, 'Togl2.0'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.spec['togl'].prefix.lib, 'Togl2.0'))
       

    def install(self, spec, prefix):
        install_tree('Awk', prefix.Awk)
        install_tree('bin', prefix.bin)
        install_tree('contrib', prefix.contrib)
        install_tree('docs', prefix.docs)
        install_tree('examples', prefix.examples)
        install_tree('external', prefix.external)
        install_tree('images', prefix.images)
        install_tree('otherLICENSES', prefix.otherLICENSES)
        install_tree('scripts', prefix.scripts)
        install_tree('Tcl', prefix.Tcl)
        install_tree('tests', prefix.tests)
        install_tree('util', prefix.util)
        install('xcrysden',prefix)
        install('usage',prefix)
