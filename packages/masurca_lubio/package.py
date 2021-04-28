# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class MasurcaLubio(Package):
    """MaSuRCA is whole genome assembly software. It combines the efficiency
       of the de Bruijn graph and Overlap-Layout-Consensus (OLC)
       approaches."""

    homepage = "http://www.genome.umd.edu/masurca.html"
    url = "https://github.com/alekseyzimin/masurca/releases/download/v3.3.1/MaSuRCA-3.3.1.tar.gz"

    version('3.4.0', sha256='5e2cb7e69b9bae9c8062a3ad3842dba7154bb8d2fc84b4b01bc475b448132c33')
    version('3.3.9', sha256='a784f820c499ef7d7186b54f8656daa4a6a30cc3237a7fdf117b3961c8223938')
    version('3.3.8', sha256='9e0113a79c36227de95b5bba5afaf9773b742315cae8fe25c374c221a6ff6ba3')
    version('3.3.7', sha256='52e1b60387d704544151e81bfa3c5ad16f2bd6997f55156aaa6047414b5b14ce')
    version('3.3.6', sha256='374558244ef17df8d1a86462a131c1237fdeec4a82a9aa5bd59da349e1be8095')
    version('3.3.5', sha256='1c8beede2692a8cd5b3f59af332fe96dbc6d009268d40232e102778672ef6182')
    version('3.3.4', sha256='181887e8ef0c513d1f272956b10dd8f2e7268c3d0b66541c24b8e44f7bcf2e6a')
    version('3.3.3', sha256='55516b7ed971a9f9a59d298893da16f441792a7ffedfe2bbc97dc6c0931abc6a')
    version('3.3.2', sha256='c39b25d3f2e31fab9ccf9a922622ce7558179baf81fcacf1e4d126ec9210261d')
    version('3.3.1', sha256='587d0ee2c6b9fbd3436ca2a9001e19f251b677757fe5e88e7f94a0664231e020')
    version('3.2.9', sha256='795ad4bd42e15cf3ef2e5329aa7e4f2cdeb7e186ce2e350a45127e319db2904b')

    depends_on('perl', type=('build', 'run'))
    depends_on('boost')
    depends_on('zlib')
    patch('arm.patch', when='target=aarch64:')

    def patch(self):
        if self.spec.target.family == 'aarch64':
            for makefile in 'Makefile.am', 'Makefile.in':
                m = join_path('global-1', 'prepare', makefile)
                filter_file('-minline-all-stringops', '', m)
                m = join_path('global-1', makefile)
                filter_file('-minline-all-stringops', '', m)

    def install(self, spec, prefix):
        installer = Executable('./install.sh')
        installer()
        install_tree('.', prefix)
