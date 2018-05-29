from setuptools import setup

setup(
    name='GimmeThat',
    version='2.0',
    description='A file transfer tool',
    url='https://github.com/nejdetckenobi/gimme-that',
    author='nejdetckenobi',
    author_email='nejdetyucesoy@gmail.com',
    license='GPL',
    packages=['gimmethat'],
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_bootstrap',
        'netifaces',
        'clamd',
        'gunicorn'
    ],
    scripts=[
        'bin/gimme',
        'bin/gimmeconf'
    ],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :'
        ': GNU General Public License v3 or later (GPLv3+)',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'Topic :: Communications :: File Sharing',
        'Topic :: Utilities'
    ]
)
