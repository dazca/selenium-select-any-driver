#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:57:21 2021

@author: danney
"""

from distutils.core import setup

__version__ = "0.1"

setup(name='Obtain Selenium Driver',
      version=__version__,
      description='Automatically selects any driver available for selenium',
      author='Dani Azemar',
      author_email='dani.azemar@gmail.com',
      packages=['any_driver_selenium'],
      required_packages=['selenium', 'webdriver_manager']
     )
