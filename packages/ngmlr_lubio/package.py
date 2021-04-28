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
#     spack install ngmlr
#
# You can edit this file again by typing:
#
#     spack edit ngmlr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class NgmlrLubio(Package):
    """NGMLR is a long-read mapper designed to align PacBio or Oxford Nanopore (standard and ultra-long) to a reference genome with a focus on reads that span structural variations"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/philres/ngmlr"
    url      = "https://github.com/philres/ngmlr/releases/download/v0.2.7/ngmlr-0.2.7-linux-x86_64.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.2.7',      sha256='a4fd68bae0a05b072834ee604af20cb9cf3a653073bee9689fa7057a348dd977')
    version('0.2.6-beta', sha256='3dab2f6ab910833e81d82455aa309fb8ac4fe4bce1437e502952f2491477552f')
    version('0.2.5-beta', sha256='576de0fc7ef8c2787d1cc0319096341b684a1c953cee746e5635178c4a86b7f0')
    version('0.2.4-beta', sha256='76ea991e3482d7dd06a3d89d0bfe7bf15bed57011ad019f03ba60d7b2b509365')
    version('0.2.3-beta', sha256='52941fd2059f43584a4c4c77e9c86e984a1847ceeabb064cbf0a996584bb209b')
    version('0.2.2-beta', sha256='c12727ba58a9a8d40ff440eb28541accc16ec38740600cf8163ffb0d5cb472a5')
    version('0.2.1-beta', sha256='2501692ca1afb8af0568419b3a07b7bb6ac2854a873eacea3ba34201d564f449')
    version('0.1.6-beta', sha256='c79760b0b2c823c03e82b83884a5dc619e9e039c0c3d1b422109476f72df98af')
    version('0.1.5',      sha256='66e2c0964f2df4bc1bb2f9ee3959234e819dc24f8725008ba7391678b2ced253')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('ngmlr', prefix.bin)
