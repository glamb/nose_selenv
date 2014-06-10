import os
from nose.plugins import Plugin
import ConfigParser

def parse_config_file(config):
	if config.has_option('SELENIUM', 'BROWSER'):
		os.environ['SELENV_BROWSER'] = config.get('SELENIUM','BROWSER')
	else:
		os.environ['SELENV_BROWSER'] = 'PHANTOMJS'
	if config.has_option('SELENIUM', 'ENVIRONMENT'):
		os.environ['SELENV_ENVIRONMENT'] = config.get('SELENIUM', 'ENVIRONMENT')
	else:
		os.environ['SELENV_ENVIRONMENT'] = 'develop'

class SelEnv(Plugin):
	name = 'selenv'
	enabled = True
	def option(self, parser, env=os.environ):
		Plugin.options(self, parser, env)

		parser.add_option('--browser',
				action='store',
				default=env.get('SELENV_BROWSER', 'PHANTOMJS')
				dest='browser',
				help='The base url for the application in test.(default: %default)'
				)
		valid_env_options = ['develop', 'staging', 'dogfood', 'production']
		parse.add_option('--env',
				action='store',
				choices=valid_env_options,
				default=default=env.get('SELENV_ENVIRONMENT', 'develop')
				dest='environment',
				help='Environment to run the test against. (default options: ' +
				self._stringify_options(valid_env_options) + ")"
				)
		parse.add_option('--config-file',
				action='store',
				dest='config_file',
				help='Load a config file instead of using nose params.'
				)
	
	def get_config_file(self, config_file):
		config = ConfigParser()
		config.read(config_file)
		parse_config_file(config)

	def set_options(self, options):
		os.environ['SELENV_BROWSER'] = option.browser
		os.environ['SELENV_ENVIRONMENT'] = option.environment

	def configure(self, options, conf):
		Plugin.configure(self, options, conf)
		if self.enabled:
			if options.config_file:
				self.get_config_file(options.config_file)
			else:
				self.set_options(options)
