'''
PasteScript template for initializing a Python project.
Provides default configuration for bootstrap, py.test, setuptools and travis-ci.

Copyright 2014, Konstantin Tretyakov.
Licensed under MIT.
'''
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


version = '1.0'

setup(name='python_boilerplate_template',
      version=version,
      description="PasteScript template for initializing a new buildout/pytest/travis/setuptools-enabled Python project",
      long_description=open("README.rst").read(),
      classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Framework :: Paste',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Environment :: Plugins',
      ],
      keywords='pastescript template package', # Separate with spaces
      author='Konstantin Tretyakov',
      author_email='kt@ut.ee',
      url='http://kt.era.ee/',
      license='MIT',
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      
      install_requires=['PasteScript', 'Paste'],
      entry_points={
        'paste.paster_create_template': 
            'python_boilerplate = python_boilerplate_template:PythonBoilerplateTemplate'
      }
)
