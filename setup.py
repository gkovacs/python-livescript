from setuptools import setup

import io

long_description = io.open('README.rst', encoding='utf8').read()

setup(
  name='livescript',
  version='1.0.0',
  description='Call LiveScript from Python',
  author='Geza Kovacs',
  author_email='geza0kovacs@gmail.com',
  packages=['livescript'],
  package_dir={'livescript': 'livescript'},
  package_data={'livescript': ['livescript.js']},
  long_description=long_description,
  url='https://github.com/gkovacs/python-livescript',
  download_url='https://github.com/gkovacs/python-livescript',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: JavaScript',
    ],
    install_requires=['PyExecJS'],
)