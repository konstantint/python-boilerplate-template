'''
Python boilerplate template:
Test that assures that the cookiecutter template at
https://github.com/konstantint/cookiecutter-python-boilerplate
produces an equivalent setup.

Copyright 2014, Konstantin Tretyakov
Licensed under MIT
'''
from subprocess import check_call
import sys, os, shutil
import os.path


import os
import os.path
from filecmp import dircmp

def assert_equal_files(a, b):
    '''Compares two text files for equality, ignoring newline characters at the end of lines.'''
    print "Checking files %s, %s" % (a, b)
    a_lns = open(a, 'r').readlines()
    b_lns = open(b, 'r').readlines()
    print "%d, %d" % (len(a_lns), len(b_lns))
    assert len(a_lns) == len(b_lns)
    for (aln, bln) in zip(a_lns, b_lns):
        if aln.replace('\n','') != bln.replace('\n',''):
            print repr(aln)
            print repr(bln)
        assert aln.replace('\n','') == bln.replace('\n','')

def assert_equal_dirs(a, b):
    '''Compares two directories for equality, checking subdirectories recursively'''
    d = dircmp(a, b)
    assert d.left_only == []
    assert d.right_only == []
    for f in d.common_files:
        assert_equal_files(os.path.join(a, f), os.path.join(b, f))
    for f in d.common_dirs:
        assert_equal_dirs(os.path.join(a, f), os.path.join(b, f))

def test_cookiecutter():
    if os.path.exists('tmp'):
        shutil.rmtree('tmp')
    os.mkdir('tmp')
    os.chdir('tmp')
    check_call("cookiecutter --no-input https://github.com/konstantint/cookiecutter-python-boilerplate".split())
    assert(os.path.exists('Boilerplate-project/src/Boilerplate_project/boilerplateproject/__init__.py'))
    os.rename('Boilerplate-project', 'a')
    assert(not os.path.exists('Boilerplate-project'))
    check_call("paster create -t python_boilerplate --config=../tests/cookiecutter_test.cfg --no-interactive Boilerplate-project".split())
    assert(os.path.exists('Boilerplate-project/src/Boilerplate_project/boilerplateproject/__init__.py'))
    os.rename('Boilerplate-project', 'b')
    assert(not os.path.exists('Boilerplate-project'))
    assert_equal_dirs('a', 'b')
    os.chdir('..')
