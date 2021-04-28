# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Openmolcas(CMakePackage):
    """OpenMolcas is a quantum chemistry software package.
       The key feature of OpenMolcas is the multiconfigurational approach to
       the electronic structure."""

    homepage = "https://gitlab.com/Molcas/OpenMolcas"
    url      = "https://github.com/Molcas/OpenMolcas/archive/v19.11.tar.gz"

    version('19.11', sha256='8ebd1dcce98fc3f554f96e54e34f1e8ad566c601196ee68153763b6c0a04c7b9')

    variant('mpi', default=True, description='Activate MPI support')

    depends_on('mpi', when='+mpi')
    depends_on('globalarrays', when='+mpi')

    depends_on('hdf5')
    depends_on('lapack')
    depends_on('blas')
    depends_on('openblas+ilp64', when='^openblas')
    depends_on('intel-mkl', when='^intel-mkl')
    depends_on('python@3.7:', type=('build', 'run'))
    depends_on('py-pyparsing', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))

    patch('CMakeLists.txt.patch', when='target=aarch64:')

    def setup_build_environment(self, env):
        env.set('MOLCAS', self.prefix)
        spec = self.spec
        if '+mpi' in spec:
            env.set('GAROOT', self.spec['globalarrays'].prefix)

    def setup_run_environment(self, env):
        env.set('MOLCAS', self.prefix)

#        return [, '-DMKLROOT=%s' % self.spec['intel-mkl'].prefix), '-DOPENBLASROOT=%s' % self.spec['openblas'].prefix)
#            '-DLINALG=OpenBLAS',
#            '-DOPENBLASROOT=%s' % self.spec['openblas'].prefix,
#            '-DPYTHON_EXECUTABLE=%s' % self.spec['python'].command.path,
#        ]
    def cmake_args(self):
        spec = self.spec

        args = ['-DPYTHON_EXECUTABLE=%s' % self.spec['python'].command.path,]
        if '^intel-mkl' in spec:
            args.append( '-DLINALG=MKL')
            args.append( '-DMKLROOT=%s' % self.spec['intel-mkl'].prefix)
        elif '^openblas' in spec:
            args.append( '-DLINALG=OpenBLAS')
            args.append( '-DOPENBLASROOT=%s' % self.spec['openblas'].prefix)

        if '+mpi' in spec:
            args.append('-DMPI=ON')
            args.append('-DGA=ON')
            args.append('-DGA_INCLUDE_PATH=%s' % self.spec['globalarrays'].prefix)

        return args

