from Cython.Distutils import build_ext
from distutils.core import setup, Extension

setup(
    name='fuzzy',
    version="0.3",
    ext_modules=[
        Extension('fuzzy', ['src/fuzzy.pyx', 'src/double_metaphone.c'])
    ],
    description="Fast Python phonetic algorithms",
    maintainer="YouGov, Plc.",
    maintainer_email="dev@yougov.com",
    url="https://bitbucket.org/yougov/fuzzy",
    cmdclass={'build_ext': build_ext},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Artistic License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    long_description=open('README.rst').read(),
)
