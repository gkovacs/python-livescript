python-livescript
====================
`python-livescript` lets you call LiveScript code from Python

Example
-------
::

  >>> from livescript import lseval
  >>> print lseval('''
        require! 'fs'
        return fs.readdirSync('.')
      ''')


Installation
------------
::

  $ pip install livescript

Returning values
----------------

Returning will pass back the output back to Python. Any datatype supported by JSON can be passed back. If you want to return the last statement, you can omit the return statement.

NPM modules
-----------

To use modules, simply install them with `npm` and ensure that the `node_modules` directory they are installed to is your current working directory. You can use them as usual with require.

License
-------

MIT


