#!/usr/bin/env python
# md5: 736465ea6fa3990f31943bf4b973ad30
# coding: utf-8

#!/usr/bin/env python3

from __future__ import division, unicode_literals, print_function

# Copyright (c) 2015 Geza Kovacs https://github.com/gkovacs
# Released under the MIT license.

"""
Python LiveScript lets you execute LiveScript code from Python

  >>> from livescript import lseval
  >>> print lseval('''
        require! 'fs'
        return fs.readdirSync('.')
      ''')
"""

__license__ = str('MIT License')

__version__ = str('1.0.0')

__author__ = str('Geza Kovacs')

__all__ = str('''
  lseval
''').split()

import os
import io
import execjs
import textwrap

node = execjs.get('Node')

#livescript_context = node.compile('''
#(function() {
#path = require('path')
#realrequire = require
#require = function(x) {
#  return realrequire(path.join(process.cwd(), 'node_modules', x))
#}
#LiveScript = require('LiveScript')
#})()
#''')

try:
  livescript_filepath = os.path.join(os.path.dirname(__file__), 'livescript.js')
except:
  livescript_filepath = os.path.join(os.getcwd(), 'livescript.js')
livescript_context = node.compile('''
(function() {
''' + io.open(livescript_filepath, encoding='utf8').read() + '''
LiveScript = require('LiveScript')
})()
''')

exec_context = node.compile('''
(function() {
var path = require('path')
var fs = require('fs')
var realrequire = require
var cached_requires = {}
require = function(x) {
  if (cached_requires[x] != null) return cached_requires[x]
  var module_path = path.join(process.cwd(), 'node_modules', x)
  if (fs.existsSync(module_path))
    cached_requires[x] = realrequire(module_path)
  else
    cached_requires[x] = realrequire(x)
  return cached_requires[x]
}
})()
''')

def remove_trailing_semicolon(program):
  if program[-1] == ';':
    return program[:-1]
  return program

def wrap_do_statement(program):
  lines = textwrap.dedent(program).split('\n')
  output = []
  output.append('do ->')
  for line in lines:
    output.append('  ' + line)
  return '\n'.join(output)

def lscompile_real(program, options):
  return livescript_context.call('LiveScript.compile', program, options)

def lscompile(program):
  return remove_trailing_semicolon(lscompile_real(wrap_do_statement(program), {'bare': True, 'header': False}))

def lseval(program):
  compiled = lscompile(program)
  return exec_context.eval(compiled)

def eval(program):
  compiled = lscompile(program)
  return exec_context.eval(compiled)


