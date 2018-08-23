"""
importhook
==============
"""
from setuptools import find_packages, setup


def get_long_description():
    with open('README.rst') as f:
        rv = f.read()
    return rv


setup(
    name='importhook',
    version='1.0.0',
    url='https://github.com/brettlangdon/importhook',
    license='MIT',
    author='Brett Langdon',
    author_email='me@brett.is',
    description='Execute code when certain modules are imported',
    long_description=get_long_description(),
    py_modules=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ]
)