#!/usr/bin/env python

from setuptools import setup

setup(
      name='fortigateconf',
      version='0.1',
      description='Python modules to interact with Fortigate configuration api',
      install_requires=['requests','json','logging'],
      author='Nicolas Thomas',
      author_email='nthomas@fortinet.com',
      url='https://fndn.fortinet.net',
      packages=['fortigateconf'],
      )
