# SolidScaffold/setup.py
from setuptools import setup

requires = ['pyramid']

entry_points = """
      [pyramid.scaffold]
      solid=solidscaffold:SolidTemplate
      """

setup(name='SolidScaffold',
      description='My personal Pyramid scaffold.',
      long_description='',
      install_requires=requires,
      packages=['solidscaffold'],
      entry_points=entry_points
      )
