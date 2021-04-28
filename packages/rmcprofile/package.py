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
#     spack install rmcprofile-v6
#
# You can edit this file again by typing:
#
#     spack edit rmcprofile-v6
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class Rmcprofile(Package):
    """RMCProfile is based on the original code for RMC, but significantly amended 
       and extended to give new capabilities and to take account of more recent 
       programming and informatics standards."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.rmcprofile.org/Main_Page"
    url      = "https://sourceforge.net/projects/rmcprofile/files/Version_6.7.9/RMCProfile_V6.7.9_Linux_64.tgz/download"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('6.7.9', sha256='0a0641cbedf4fd8014cd718391b3ec5d3ef3749056dc9d57566e27207a8c07d6',
            url='file://{0}/RMCProfile_V6.7.9_Linux_64.tgz'.format(os.getcwd()))

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix.bin)
        env.prepend_path('PGPLOT_DIR', os.path.join(self.spec.prefix.bin,'libs'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.spec.prefix.bin,'libs'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.spec.prefix.bin,'libs'))

    def install(self, spec, prefix):
        mkdirp(prefix.sbin)
        install('RMCProfile_setup', prefix.sbin)
        install('RMCProfile_setup_no_term', prefix.sbin)
        install_tree('exe', prefix.bin)
        install_tree('tutorial', prefix.example)
