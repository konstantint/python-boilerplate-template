'''
Python boilerplate template: Smoke test.

Copyright 2014, Konstantin Tretyakov
Licensed under MIT
'''
from subprocess import check_call
import sys, os, shutil
import os.path

def test_smoke():
    if os.path.exists('tmp'):
        shutil.rmtree('tmp')
    os.mkdir('tmp')
    os.chdir('tmp')
    check_call("paster create -t python_boilerplate --config=../tests/smoke_test_config.cfg --no-interactive python-boilerplate-test".split())
    assert(os.path.exists('python-boilerplate-test/src/python_boilerplate_test/pythonboilerplatetest/__init__.py'))
    os.chdir('python-boilerplate-test')
    check_call("python bootstrap.py".split())
    check_call("bin/buildout")
    if os.path.exists("bin/py.test.exe"):
        check_call("bin/py.test.exe")
    else:
        check_call("bin/py.test")
    os.chdir('../..')
