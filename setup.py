from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-comments',
	version=version,
	description="Internal commenting system for CKAN.",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='David Megginson',
	author_email='david.megginson@megginson.com',
	url='http://www.megginson.com',
	license='Public domain',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.comments'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
        comments=ckanext.comments.plugin:CommentsPlugin
	""",
)
