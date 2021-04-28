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
#     spack install porechop-git
#
# You can edit this file again by typing:
#
#     spack edit porechop-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPorechop(PythonPackage):
    """Porechop is a tool for finding and removing adapters from Oxford Nanopore reads."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/rrwick/Porechop"
    git      = "https://github.com/rrwick/Porechop.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('0.2.4', tag='v0.2.4')
    version('0.2.3', tag='v0.2.3')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('python@3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
