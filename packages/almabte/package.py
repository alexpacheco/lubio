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
#     spack install almabte
#
# You can edit this file again by typing:
#
#     spack edit almabte
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Almabte(CMakePackage):
    """almaBTE is a software package that solves the space- and time-dependent 
       Boltzmann transport equation for phonons, using only ab-initio calculated quantities as inputs."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://almabte.bitbucket.io/"
    url      = "https://almabte.bitbucket.io/downloads/almabte-v1.3.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('1.3.2', 'b466bca2344e8be25952e432a876fece')

    # FIXME: Add dependencies if required.
    depends_on('cmake@3.1.0:', type='build')
    depends_on('mpi')
    depends_on('boost+mpi')
    depends_on('hdf5+mpi')

    build_targets = ['all']
    build_directory = 'build'

    def cmake_args(self):
        cmake_args = [
             '-DCMAKE_C_COMPILER=%s' % spack_cc,
             '-DCMAKE_CXX_COMPILER=%s' % spack_cxx,
             '-DCMAKE_Fortran_COMPILER=%s' % spack_fc
         ]
        return cmake_args

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.test)
        mkdirp(prefix.external)
        install_tree('build/src/', prefix.bin)
        install_tree('build/test', prefix.test)
        install_tree('build/external', prefix.external)
