import os
from nose.plugins import Plugin
from ConfigParser import ConfigParser

def set_options_from_config(config):
    if config.has_option('SELENIUM', 'ENVIRONMENT'):
        os.environ['SELENV_ENVIRON'] = config.get('SELENIUM','ENVIRONMENT')

    if config.has_option('SELENIUM', 'BASEURL'):
        os.environ['SELENV_BASEURL'] = config.get('SELENIUM', 'BASEURL')

    if config.has_option('SELENIUM', 'TIMEOUT'):
        os.environ['SELENV_TIMEOUT'] = config.get('SELENIUM', 'TIMEOUT')

    if config.has_option('SELENIUM', 'BROWSER'):
        os.environ['SELENV_BROWSER'] = config.get('SELENIUM', 'BROWSER')

    if config.has_option('SELENIUM', 'FBUSER'):
        os.environ['SELENV_FBUSER'] = config.get('SELENIUM', 'FBUSER')

    if config.has_option('SELENIUM', 'FBPASS'):
        os.environ['SELENV_FBPASS'] = config.get('SELENIUM', 'FBPASS')

    if config.has_option('SELENIUM', 'LOGGING'):
        os.environ['SELENV_LOGGING'] = config.get('SELENIUM', 'LOGGING')

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
                dest='environment',
                help='Run the browser in this location (options ' +
                self._stringify_options(valid_location_options) + ').' 
                )
        parser.add_option('--browser',
                action='store',
                dest='browser',
                help='Select the type of browser you want Selenium to use.'
                )
        parser.add_option('--baseurl',
                action='store',
                dest='base_url',
                help='base url of the application in test.'
                )
        parser.add_option('--timeout',
                action='store',
                dest='timeout',
                type='str',
                help='Change the timeout on the fly.'
                )
        parser.add_option('--fbuser',
                action='store',
                dest='fb_user',
                help='Facebook username'
                )
        parser.add_option('--fbpass',
                action='store',
                dest='fb_pass',
                help='Facebook password'
                )
        parser.add_option('--logging',
                action='store',
                dest='logging',
                help='Set logging level (debug, info, warn, error, critical). Disabled by default.'
                )

    def read_config_file(self, config_file):
        CONFIG = ConfigParser()
        CONFIG.read(config_file)
        set_options_from_config(CONFIG)

    def set_options(self, options):
        if options.environment:
            os.environ['SELENV_ENVIRON'] = options.environment
        if options.browser:
            os.environ['SELENV_BROWSER'] = options.browser
        if options.base_url:
            os.environ['SELENV_BASEURL'] = options.base_url
        if options.timeout:
            os.environ['SELENV_TIMEOUT'] = options.timeout
        if options.fb_user:
            os.environ['SELENV_FBUSER'] = options.fb_user
        if options.fb_pass:
            os.environ['SELENV_FBPASS'] = options.fb_pass
        if options.logging:
            os.environ['SELENV_LOGGING'] = options.logging

    def configure(self, options, conf):
        Plugin.configure(self, options, conf)
        if self.enabled:
            if options.config_file:
                self.read_config_file(options.config_file)
            else:
                self.set_options(options)
