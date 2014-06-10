import os
from nose.plugins import Plugin
from ConfigParser import ConfigParser

def set_options_from_config(config):
    if config.has_option('SELENIUM', 'ENVIRONMENT'):
	    os.environ['SELENV_ENVIRON'] = config.get('SELENIUM','ENVIRONMENT')
    else:
	    os.environ['SELENV_ENVIRON'] = 'develop'

    if config.has_option('SELENIUM', 'BROWSER'):
	    os.environ['SELENV_BROWSER'] = config.get('SELENIUM', 'BROWSER')
    else:
	    os.environ['SELENV_BROWSER'] = 'PHANTOMJS'

class SelEnv(Plugin):

    name = 'selenv'
    enabled = True

    def _stringify_options(self, list):
        string = ", ".join(list)
        return "[" + string + "]"

    def options(self, parser, env=os.environ):

        Plugin.options(self, parser, env)
        parser.add_option('--config-file',
                          action='store',
                          dest='config_file',
                          help='Load options from a config file instead of enter via the command line.'
        )
        valid_location_options = ['develop', 'staging', 'dogfood', 'production']
        parser.add_option('--env',
                          action='store',
                          choices=valid_location_options,
                          default=env.get('SELENV_ENVIRO', 'develop'),
                          dest='environment',
                          help='Run the browser in this location (default %default, options ' +
                               self._stringify_options(valid_location_options) +
                               ').' 
        )
        parser.add_option('--browser',
                          action='store',
                          default=env.get('SELENV_BROWSER', 'PHANTOMJS'),
                          dest='browser',
                          help="Select the type of browser you want Selenium to use. (default %default). "
        )

    def read_config_file(self, config_file):
        CONFIG = ConfigParser()
        CONFIG.read(config_file)
        set_options_from_config(CONFIG)

    def set_options(self, options):
	os.environ['SELENV_ENVIRON'] = options.environment
	os.environ['SELENV_BROWSER'] = options.browser

    def configure(self, options, conf):
        Plugin.configure(self, options, conf)
        if self.enabled:
            if options.config_file:
                self.read_config_file(options.config_file)
            else:
                self.set_options(options)
