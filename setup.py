from setuptools import setup
from os import path

BASE_DIR = path.abspath(path.dirname(__file__))
with open(path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# based on https://packaging.python.org/guides/single-sourcing-package-version/
def get_version():
    version_file = path.join(BASE_DIR, 'pyhanko', 'version.py')
    with open(version_file, encoding='utf-8') as f:
        for line in f:
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        raise RuntimeError("Unable to find version string.")


setup(
    name='pyHanko',
    version=get_version(),
    packages=['pyhanko', 'pyhanko.pdf_utils', 'pyhanko.sign'],
    url='https://github.com/MatthiasValvekens/pyHanko',
    license='MIT',
    author='Matthias Valvekens',
    author_email='dev@mvalvekens.be',
    description='Tools for stamping and signing PDF files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        "console_scripts": [
            "pyhanko = pyhanko.__main__:launch"
        ]
    },
    install_requires=[
        'asn1crypto>=1.4.0',
        'pytz>=2020.1',
        'qrcode>=6.1',
        'tzlocal>=2.1',
        'python-pkcs11>=0.6.0',
        'pyhanko-certvalidator==0.12.1',
        'fonttools>=4.13.0',
        'click>=7.1.2',
        'requests>=2.24.0',
        'python-barcode>=0.13.1',
        'Pillow>=8.0.1',
        'pyyaml>=5.3.1',
        'cryptography>=3.3.1'
    ],
    setup_requires=[
        'wheel', 'pytest-runner'
    ],
    extras_require={
        'extra_pubkey_algs': ['oscrypto>=1.2.1']
    },
    tests_require=[
        'pytest>=6.1.1',
        'requests-mock>=1.8.0',
        'ocspbuilder>=0.10.2',
        'freezegun',
    ],
    keywords="signature pdf pades digital-signature pkcs11"
)
