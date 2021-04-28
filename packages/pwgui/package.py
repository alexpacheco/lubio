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
#     spack install pwgui
#
# You can edit this file again by typing:
#
#     spack edit pwgui
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Pwgui(Package):
    """PWgui is a GUI for PWscf based programs from Quantum-ESPRESSO integrated suite of codes 
     for electronic structure calculations and materials modeling at the nanoscale."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www-k3.ijs.si/kokalj/pwgui/pwgui.html"
    url      = "http://www-k3.ijs.si/kokalj/pwgui/download/pwgui-6.1-linux-x86_64.tgz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('6.1',    sha256='c397571ccac07bf8f4b237b37a1f629b2283ec3edb3c308f12c0654dcb94b5d7')
    version('5.1.1',  sha256='a60d5d7ce65cffde51797e1f4a6f5335664dce36ca4dbc521136bfa3743584c1')
    version('5.0.2',  sha256='c436b29f6097088fcc15e3c7a2021d0a5c9c5b811460a9dd6ff27f62fc2bc405')
    version('5.0svn', sha256='5a804f5e7208a45e85b7bb7f45944e909c3e14f813dc7056f9ecf4db0cd180c2')
    version('4.3',    sha256='a1428745a9be73141fe37e59992326f1b1c24d9abf34b753a5d690b73353e053')
    version('4.2',    sha256='749a5cd4bff52f47d8492952c54532c9a718a9826d8215dc95c8e8689524d3f6')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('pwgui', prefix.bin)
