import setuptools
from shutil import copyfile
# import os

copyfile('readme.md', 'structjour/readme.md')


with open('structjour/readme.md', 'r') as fh:
    long_description = fh.read()


thePackages = setuptools.find_packages(exclude=['test'])

setuptools.setup(
    name='structjour',
    version='0.9.95-Alpha.001',
    author='Mike Petersen',
    author_email='pentsok@zerosubstance.org',
    description='A structured daily journal for day traders.',
    license='GPL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MikePia/structjour',
    packages=thePackages,
    keywords='DayTrading journal',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft :: Windows'
    ],
    install_requires=[
        'requests==2.25.1',
        'Pillow==8.2.0',
        'numpy==1.20.1',
        'pandas==1.2.2',
        'matplotlib==3.3.4',
        'SQLAlchemy==1.3.23',
        'PyQtWebEngine==5.15.2',
        'PyQt5==5.15.2',
        'PyQt5-sip==12.8.1',
        'openpyxl==3.0.6',
        'beautifulsoup4==4.9.3',
        'mplfinance'
    ],
    include_package_data=True,

    # data_files=[('', ['Disciplined.xlsx']),('',['readme.md'])],
    entry_points={'console_scripts': 'structjour=structjour.view.runtrade:main'},
    python_requires='>=3.6'
)
