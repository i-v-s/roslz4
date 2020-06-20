from distutils.core import setup, Extension
from catkin_pkg.python_setup import generate_distutils_setup

roslz4 = Extension(
    'roslz4._roslz4',
    include_dirs=['include'],
    libraries=['lz4'],
    library_dirs=['/usr/lib/x86_64-linux-gnu/'],
    sources=[
        'src/lz4s.c',
        'src/xxhash.c',
        'src/_roslz4module.c'
    ]
)

d = generate_distutils_setup(
    packages=['roslz4'],
    package_dir={'': 'src'},
    requires=[],
)

setup(name='roslz4', version=d['version'], ext_modules=[roslz4])
