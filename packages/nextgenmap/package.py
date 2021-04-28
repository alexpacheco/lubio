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
#     spack install nextgenmap
#
# You can edit this file again by typing:
#
#     spack edit nextgenmap
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Nextgenmap(CMakePackage):
    """NextGenMap is a flexible highly sensitive short read mapping tool that 
       handles much higher mismatch rates than comparable algorithms while 
       still outperforming them in terms of runtime. """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/Cibiv/NextGenMap/wiki"
    url      = "https://github.com/Cibiv/NextGenMap/archive/v0.5.5.tar.gz"

    version('0.5.5',  sha256='c205e6cb312d2f495106435f10fb446e6fb073dd1474f4f74ab5980ba9803661')
    version('0.5.4',  sha256='8e698f1797ed8b1fe6296b0ed6b76e5ed0ee21b7ceb52ac566b7cc73ccfa6b5a')
    version('0.5.3',  sha256='cc4d28f72221e522bde969093dad06cde37a82f37e774e62d0e4a72f9f2f2f60')
    version('0.5.2',  sha256='cf06432f7444eeb2b44c274c65aaad71fd977cc077f0618582dee1ede5f12c1c')
    version('0.4.12', sha256='92150130b858629778908ece1ef5ba95063d582ae8b8aa94e22f91dc8923e2f0')
    version('0.4.11', sha256='e7352bb97b191d77491b7be104c5fc2896615e777693becf374ba2a22cc3da31')
    version('0.4.10', sha256='d2fb555febdb4239b8551111975bfe7d9b3907677cd250f938776e509f5b0947')

    # FIXME: Add dependencies if required.
#    depends_on('cmake', type='build')
    depends_on('cuda', type='build')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
#        args = []
#        return args
        spec = self.spec
        return [
            # OpenCL support
            '-DCMAKE_PREFIX_PATH={0}'.format(spec['cuda'].libs.joined(";"))
        ]

#    def 
