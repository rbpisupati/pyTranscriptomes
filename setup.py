from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytranscript',
    version='0.0.1',
    description='transcriptomes functions',
    long_description=long_description,
    url='https://github.com/rbpisupati/pyTranscriptomes.git',
    author=['Rahul Pisupati'],
    author_email='rahul.bharadwaj.p@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='genomics',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        "numpy",
        "scipy",
    ],
    entry_points={
        'console_scripts': [
            'pytranscript=core:main'
        ],
    },
)
