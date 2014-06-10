from setuptools import setup

setup(
		name='nose_selenv',
		version='0.1',
		author='Gregg Lamb',
		author_email='glamb@wetpaint-inc.com',
		description='Nose plugin for wetpaint web qa',
		py_modules=['nose_selenv'],
		entry_points= {
			'nose.plugins.0.10': [
				'nose_selenv = nose_selenv:SelEnv'
				]
			},
		)
