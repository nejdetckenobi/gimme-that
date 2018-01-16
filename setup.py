from distutils.core import setup

setup(
    name='GimmeThat',
    version='0.1.0',
    description='A file transfer tool',
    url='https://github.com/nejdetckenobi/gimme-that',
    long_description=open('README.md').read(),
    author='nejdetckenobi',
    author_email='nejdetyucesoy@gmail.com',
    license='GPL',
    packages=['gimmethat'],
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_bootstrap',
        'netifaces'
    ],
    scripts=[
        'bin/gimme',
    ],
    include_package_data=True
)
