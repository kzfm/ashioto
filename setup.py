from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ashioto',
      version=version,
      description="DJing utils",
      long_description="""\
DJing utils""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='DJ Traktor',
      author='kzfm',
      author_email='kerolinq@gmail.com',
      url='http://blog.kzfmix.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
