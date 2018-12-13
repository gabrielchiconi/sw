import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name='sshw',
    version='1.0.0',
    author='Gabriel Chiconi',
    author_email='gabriel.chiconi@gmail.com',
    description='SSH Wallet for your personal computer!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielchiconi/sw',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
    ],
    scripts=['bin/sw'],
)
