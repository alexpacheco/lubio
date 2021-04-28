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
#     spack install bgc
#
# You can edit this file again by typing:
#
#     spack edit bgc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bgc(Package):
    """bgc  implements Bayesian estimation of genomic clines to quantify introgression at many loci. Models are available for linked loci, genotype uncertainty and sequence errors. """

    homepage = "https://sites.google.com/site/bgcsoftware/"
    url      = "https://sites.google.com/site/bgcsoftware/home/bgcdist1.03.tar.gz"

    # notify when the package is updated.
    maintainers = ['alexpacheco']

    version('1.03', sha256='94efdb9ad5917ff7abe70f4ffd10c6fe7feae62c8a7f000dfb4852ffa2ef8f16')

    depends_on('hdf5~mpi')
    depends_on('gsl')

    phases = ['edit', 'build', 'install']

    def edit(self, spec, prefix):
        config = [
            'CC           = h5c++',
            'CFLAGS       = -Wall -O2',
            'OBJS        = bgc_func_hdf5.o bgc_func_initialize.o bgc_func_linkage.o bgc_func_mcmc.o bgc_func_ngs.o bgc_func_readdata.o bgc_func_write.o bgc_main.o mvrandist.o',
            'LDFLAGS     = %s' % self.spec["gsl"].libs.ld_flags,
            'LDFLAGS     += %s' % self.spec["hdf5"].libs.ld_flags,
            'CPPFLAGS    = -I{0}'.format(spec['gsl'].prefix.include),
            'CPPFLAGS    += -I{0}'.format(spec['hdf5'].prefix.include),
            'LIBS        = -lgsl -lgslcblas',
            'EXEC        = bgc',

            '$(EXEC) : $(OBJS)',
            '\t$(CC) $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) $(LIBS) $(OBJS) -o $@',
            '%.o : %.c %.C',
            '\t@$(CC) $(CFLAGS) $(CPPFLAGS) -c –o $@ $<',
            'estpost: ',
            '\t$(CC) $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) $(LIBS) -o $@ estpost_h5.c',
            'clean :',
            '\trm $(EXEC) $(OBJS)'
        ]

        # Write configuration options to makefile
        with open('Makefile', 'w') as mfile:
            for var in config:
                mfile.write('{0}\n'.format(var))

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.example)
        mkdir(prefix.src)
        mkdir(prefix.docs)
        install('bgc', prefix.bin)
        install('*.C', prefix.src)
        install('Makefile', prefix.src)
        install_tree('CVS', prefix.src)
        install('bgc_manual.pdf', prefix.docs)
        install_tree('example', prefix.example)
