import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='pck',
    version='0.1',
    packages=['pck'],
    url='https://github.com/hirokiky/pck',
    license='MIT',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='A package development framework',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Topic :: Software Development",
    ],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "pck=pck.commands:main",
        ]
    }
)
