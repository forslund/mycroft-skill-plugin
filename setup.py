#!/usr/bin/env python3
from os.path import join, basename, abspath, dirname
from setuptools import setup


PLUGIN_ENTRY_POINT = ('plugin_skill = '
                      'plugin_skill')

setup(
    name='PluginSkill',
    version='0.1',
    description='A Skill plugin for Mycroft-core',
    url='http://github.com/forslund/plugin-skill',
    author='Åke Forslund',
    author_email='',
    license='Apache-2.0',
    packages=['plugin_skill'],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: STT',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='mycroft plugin stt',
    entry_points={'mycroft.plugin.skill': PLUGIN_ENTRY_POINT}
)
