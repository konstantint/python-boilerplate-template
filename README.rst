===========================
Python Boilerplate Template
===========================

This is a `PasteScript <http://pythonpaste.org/script/>`_ template for generating a Python project. It provides simple starting points for using some of the popular best-practices:

  * Proper `setuptools <https://pypi.python.org/pypi/setuptools>`_-compatible package layout.
  * `py.test <http://pytest.org/>`_-based tests.
  * `buildout <http://www.buildout.org/>`_ for managing development tools or developing multiple-package projects
  * Usage of the `Travis-CI <https://travis-ci.org/>`_ continuous integration service.

Installation
------------

The easiest way to install the package is via ``easy_install`` or ``pip``::

    $ easy_install python_boilerplate_template
    
Note that the package is a plugin to the ``paster`` tool. The ``paster`` tool is provided by the ``PasteScript`` package (it will be installed automatically with ``python_boilerplate_template``). The ``paster`` executable should appear in your Python's ``bin/`` (in Windows ``Scripts/``) directory. You might need to add that directory to your ``PATH`` to run the executable.

Usage
-----

To initialize a directory layout for a new project, ensure that ``paster`` is in your path and run::

    $ paster create -t python_boilerplate <project_name>
    
After asking some basic questions, the tool will create the following project layout for you::

   <project_name>/
     |
     +-- .gitignore           # Git configuration
     +-- .travis.yml          # Travis-CI configuration    
     +-- bootstrap.py         # Buildout bootstrap-script
     +-- buildout.cfg         # Buildout project configuration
     +-- setup.cfg            # Configuration for py.test and other tools
     +-- README.md            # Information on how to use the project
     +-- src/                 # Directory for keeping (possible multiple) project eggs
         |
         +- <egg_name>/       # First egg of the project
            |
            +-- package/      # Python source files
            +-- tests/        # Tests
            +-- .gitignore    # Git configuration
            +-- .travis.yml   # Travis-CI configuration
            +-- setup.cfg     # Configuration for py.test and other tools
            +-- setup.py      # Package metadata
            +-- MANIFEST.in   # Files to include in the package
            +-- README.rst    # Package description
            +-- LICENSE.txt   # License
            +-- CHANGELOG.txt # Changelog

This structure suggests you develop your project as a collection of eggs, with each egg having its separate subdirectory within ``src/``. Each egg uses the standard setuptools layout, and the whole project relies on buildout to organize the parts.

Project preparation
-------------------

The next thing to do after having created the project layout is to add the code to a version control repository. There are two common options for you to choose from:

  1. For smaller single-package projects you might want to keep only the Python's package code (i.e. ``src/<egg_name>``) under version control, and consider the rest (the ``buildout.cfg`` and all that comes with it) to be your local development environment.
  2. For larger projects you should consider keeping the whole development environment (including ``buildout.cfg``, perhaps several eggs under ``src``, docs in ``doc``, etc) under version control.

**If you decided in favor of Option 1**:

  - Create a version control repository under ``src/<egg_name>``. Here is an example with Git::

        > cd src/<egg_name>
        > git init
        > git add .
        > git commit -m "Initial package structure"
    
    If you are using Github, proceed by creating a `<your-project>` repository on the Github website, and then doing::

        > git remote add origin https://github.com/<username>/<your-project>.git
        > git push origin master

  - You can safely delete the ``.travis.yml`` file in the root of the project (but leave the one within the ``src/<egg_name>`` directory).

**If you decided in favor of Option 2**:

  - Create a version control repository under the project root. The Git/Github example above applies, except for the first ``cd`` line.
  - Drop ``.travis.yml`` from the ``src/<egg_name>`` directory (leave the one in the project root).

Before you begin developing your code, you may wish to tune the ``src/<egg_name>/README.rst`` file. This file should contain a detailed description of what your package is supposed to do. In particular, when you submit your package to PyPI, the contents of this file will be shown on the package index page. 

In addition, the ``LICENSE.txt`` included with the boilerplate code is a copy of the ``MIT`` license. If you project uses a different license, replace this file to match.

Eventually, you will also want to edit the ``README.md`` to reflect the development instructions that apply to your project.

Finally, review the settings in ``src/<egg_name>/setup.py`` (e.g., the ``classifiers`` parameter might require tuning).

Once you are done with the preparation, you can start developing by running ``python bootstrap.py`` and then ``buildout``. See next section.

Common development tasks
------------------------

  * **Setting up the development environment before first use**::
  
        > python bootstrap.py
        > export PATH=$PWD/bin:$PATH  
            (in Windows: set PATH=%CD%\bin;%PATH%)
        > buildout
       
  * |  **Running tests**
    |  Tests are kept in the `tests` directory and are run using:

    ::

        > py.test
    
  * **Creating Sphinx documentation**::
  
        > sphinx-quickstart
        (Fill in the values, edit documentation, add it to version control)
        (Generate documentation by something like "cd docs; make html")
        
    (See `this guide <http://sphinx-doc.org/tutorial.html>`_ for more details)
    
  * |  **Specifying dependencies for your package**:
    |  Edit the ``install_requires`` line in ``src/<egg_name>/setup.py`` by listing all the dependent packages.

  * |  **Producing executable scripts**:
    |  Edit the ``console_scripts`` section of ``entry_points`` in ``src/<egg_name>/setup.py``. Then run ``buildout``. The corresponding scripts will be created in the ``bin/`` subdirectory. Note that the boilerplate project already contains one dummy script as an example.

  * |  **Debugging the code manually**:   
    |  Simply run ``bin/python``. This generated interpreter script has the project package included in the path.
    
  * **Publishing the package on Pypi**::
  
         > cd src/<egg_name>
         > python setup.py register sdist upload
       
  * **Creating an egg or a windows installer for the package**::
  
         > cd src/<egg_name>
         > python setup.py bdist_egg
          or
         > python setup.py bdist_wininst
       
  * |  **Travis-CI integration**:
    |  To use the Travis-CI continuous integration service, follow the instructions at the `Travis-CI website <https://travis-ci.org/>`_ to register an account and connect your Github repository to Travis. The boilerplate code contains a minimal ``.travis.yml`` configuration file that might help you get started.

  * | **Other tools**:
    | The initial ``buildout.cfg`` includes several useful code-checking tools under the ``[tools]`` section. Adapt this list to your needs (remember to run ``buildout`` each time you change ``buildout.cfg``).

  * |  **Working with setup.py**:
    |  If you are working on a small project you might prefer to drop the whole ``buildout`` business completely and only work from within the package directory (i.e. make ``src\<egg_name>`` your project root). In this case you should know that you can use

    ::
    
         > python setup.py develop
         
    to include the package into the system-wide Python path. Once this is done, you can run tests via::
    
         > python setup.py test
         
    Finally, to remove the package from the system-wide Python path, run::
    
         > python setup.py develop -u

  * |  **Developing multi-package projects**:
    |  Sometimes you might need to split your project into several packages, or use a customized version of some package in your project. In this case, put additional packages as subdirectories of ``src/`` alongside the original ``src/<egg_name>``, and register them in ``buildout.cfg``. For example, if you want to add a new package to your project, do

    ::
    
         > cd src/
         > cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
           or
         > paster create <new_package_name>
         
    Then add ``src/<new_package_name>`` to version control and add the directory ``src/<new_package_name>`` to the ``develop`` list in ``buildout.cfg``. Also, if necessary, add ``<new_package_name>`` to the ``[main]`` part of ``buildout.cfg`` and mention it in the ``[pytest]`` configuration section of ``setup.cfg``.

References
----------

  * PyPI Page: http://pypi.python.org/pypi/python_boilerplate_template
  * Github: https://github.com/konstantint/python-boilerplate-template
  * Blog post: http://fouryears.eu/2014/03/19/structure-of-a-python-project/
  * Useful reading
     - http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
  * Related projects: `[1] <https://pypi.python.org/pypi/modern-package-template>`_, `[2] <https://pypi.python.org/pypi/python-package-template/>`_, `[3] <https://github.com/vital-fadeev/python-package-template>`_, `[4] <http://pydanny.com/cookie-project-templates-made-easy.html>`_.


Copyright & License
-------------------

Copyright (c) 2014, `Konstantin Tretyakov <http://kt.era.ee/>`_. MIT License.