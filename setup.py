from setuptools import setup

setup(
        name='nose_selenv',
        version='0.4',
        author='Gregg Lamb',
        author_email='glamb@wetpaint-inc.com',
        url='https://github.com/glamb/nose_selenv',
        description='Nose plugin to setup environment variables used for automation frameworks',
        py_modules=['nose_selenv'],
        license='Mozilla Public License 2.0 (MPL 2.0)',
        entry_points= {'nose.plugins.0.10': ['nose_selenv = nose_selenv:SelEnv']},
        classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Quality Assurance',
            'Topic :: Software Development :: Testing',
            'Topic :: Utilities'],
        install_requires=['nose'],
        )
