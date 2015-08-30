from setuptools import setup

description_long = '''
A unit test generator for interval arithmetic libraries.  Test cases can easily
be written and shared in a domain-specific language that is based on
IEEE Std 1788-2015, IEEE standard for interval arithmetic.

Support for additional programming languages, test frameworks and interval
arithmetic libraries be added via plugins.

'''

setup (
    name                = "ITF1788",
    version             = "0.0.1",
    author              = "Oliver Heimlich",
    author_email        = "oheim@posteo.de",
    description         = "Interval Test Framework for IEEE Std 1788-2015",
    license             = "Apache 2.0",
    keywords            = "interval arithmetic, source code generation, unit test, test-driven development, domain-specific language, IEEE Std 1788-2015",
    url                 = "https://github.com/oheim/ITF1788",
    packages            = ['itf1788'],
    package_dir         = {'itf1788': 'src'},
    package_data        = {'itf1788':
                            [
                                'plugins/*/*.py',
                                'plugins/*/*.yaml',
                                'plugins/*/arith/*/*.yaml',
                                'plugins/*/test/*/*.yaml',                                
                            ]},
    zip_safe            = False,
    long_description    = description_long,
    classifiers         = [
                            "Development Status :: 2 - Pre-Alpha",
                            "Intended Audience :: Developers",
                            "Intended Audience :: Science/Research",
                            "License :: OSI Approved :: Apache Software License",
                            "Topic :: Scientific/Engineering :: Mathematics",
                            "Topic :: Software Development :: Code Generators",
                            "Topic :: Software Development :: Testing",
                          ],
    install_requires    = [
                            "PLY>=3.4",
                            "PyYAML>=3.11",
                          ],
)
