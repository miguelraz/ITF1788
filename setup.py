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
    author              = "Maximilian Kiesner, Marco Nehmeier, Oliver Heimlich",
    author_email        = "nehmeier@informatik.uni-wuerzburg.de",
    description         = "Interval Test Framework for IEEE Std 1788-2015",
    keywords            = "interval arithmetic, source code generation, unit test, test-driven development, domain-specific language, IEEE Std 1788-2015",
    url                 = "https://github.com/nehmeier/ITF1788",
    packages            = ['itf1788'],
    package_data        = {'itf1788':
                            [
                                # language callbacks
                                'plugins/*/callbacks.py',
                                # language specifications
                                'plugins/*/lang.yaml',
                                # library specifications (per language)
                                'plugins/*/arith/*/arith.yaml',
                                # test framework specifications (per language)
                                'plugins/*/test/*/test.yaml',
                            ]},
    # The package is not zip-safe because plugins are located using the file system
    zip_safe            = False,
    long_description    = description_long,
    classifiers         = [
                            "Development Status :: 4 - Beta",
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
