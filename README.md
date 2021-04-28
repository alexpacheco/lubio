# [Spack](https://github.com/spack/spack) package repo for software packaging on Lehigh's HPC clusters

This holds a set of Spack packages for Bioinformatics software such as 
NGS Tools that are not available in spack. It relies on Spack and the 
builtin Spack packages, some of which are overridden by this repo.

## Getting started

Initial setup like:

```bash
cd /path/to/big/disk
git clone https://github.com/spack/spack.git
cd spack/var/spack/repos
git clone https://github.com/alexpacheco/lubio.git
cd -
./spack/bin/spack compiler add /usr/bin/gcc
./spack/bin/spack repo add spack/var/spack/repos/lubio
```

To not have to type a full path to `spack` and to gain some other shell-level features do

```bash
$ source spack/share/spack/setup-env.sh
```
