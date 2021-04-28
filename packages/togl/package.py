# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install togl
#
# You can edit this file again by typing:
#
#     spack edit togl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os.path

from spack import *


class Togl(Package):
    """Togl provides a platform independent Tk widget for using OpenGL rendering contexts."""

    homepage = "https://sourceforge.net/projects/togl"
    url      = "https://sourceforge.net/projects/togl/files/Togl/2.0/Togl2.0-8.4-Linux.tar.gz"

    version('2.0-8.4', sha256='ef10acb5ebc9cc2827deb15f1bfc8ade95e4990a942a6e6f181b3b248fd504d3')

#    def setup_run_environment(self, env):
#        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib', 'Togl2.0'))

    def install(self, spec, prefix):
        install_tree('lib', prefix.lib)
        install_tree('include', prefix.include)
        install_tree('doc', prefix.doc)
