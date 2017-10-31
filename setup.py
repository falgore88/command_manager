# coding=utf-8

import os
import re

from setuptools import setup

try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')
except ImportError:
    def read_md(f):
        return open(f, 'r').read()


def get_packages(package):
    return [dirpath.replace(os.path.sep, ".")
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]
    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    print filepaths
    return {package: filepaths}


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('command_manager')


setup(
    name='command_manager',
    description="Entry point for Python scripts",
    long_description=read_md('README.md'),
    version=version,
    download_url='https://github.com/falgore88/command_manager/tarball/v{}'.format(version),
    license='BSD',
    url='https://github.com/falgore88/command_manager/',
    packages=get_packages('command_manager'),
    author='Evgeniy Titov',
    author_email='falgore88@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: X11 Applications',
        'Environment :: Console',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
