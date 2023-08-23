from setuptools import setup, find_packages
import os
import sys

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

# Setting up
setup(
    name="pandoraPlugintools",
    version="1.0.0",
    author="PandoraFMS projects department",
    author_email="<projects@pandorafms.com>",
    description="A plugin tool set of functions for pandorafms",
    long_description=readme,
    long_description_content_type='text/markdown',
    url = 'https://github.com/projects-pandorafms/pandoraPlugintools',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['datetime', 'cryptography==3', 'requests', 'requests_ntlm','pycrypto==2.6.1','easysnmp==0.2.6','pysnmp==4.4.12'],
    keywords=['python', 'pandora', 'pandorafms', 'plugintool', 'plugintools'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)
