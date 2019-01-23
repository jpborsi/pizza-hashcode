#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='pizza_hashcode',
        version='0.0',
        description='Code for solving 2019 Google HashCode warm-up',
        author='John Borsi',
        author_email='jpborsi@gmail.com',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        package_data={'pizza_hashcode': ['input/*.in']},
        test_suite='test',
        entry_points = {'console_scripts':['solve=pizza_hashcode.solve:main']})
