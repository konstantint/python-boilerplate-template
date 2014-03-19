'''
Python boilerplate template: Main module.

Copyright 2014, Konstantin Tretyakov

Licensed under MIT.
'''

from paste.script.templates import Template, var
from paste.util.template import paste_script_template_renderer
import datetime

class PythonBoilerplateTemplate(Template):

    _template_dir = 'template'
    summary = "A buildout/py.test/travis-enabled Python project with support for one or more setuptools-enabled packages."
    vars = [
        var('version', 'Version (like 0.1)', default='0.1'),
        var('description', 'One-line description of the package'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name', default='MIT'),
        var('install_requires', 'Dependencies (space-separated list of package names)'),
        var('zip_safe', 'True/False: if the package can be distributed as a .zip file', default=False),
        ]

    template_renderer = staticmethod(paste_script_template_renderer)

    def pre(self, command, output_dir, vars):
        vars['year'] = datetime.datetime.now().year
