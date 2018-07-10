import configparser
import optparse
import os
from ..log_format import init_logger
from ..version import version


class MyOption (optparse.Option, object):
    """ optparse Option with two additional attributes.

    The list of command line options (getopt.Option) is used to create the
    list of the configuration file options. When reading the file, and then
    reading the command line arguments, we don't want optparse.parse results
    to override the configuration file values. But if we provide default
    values to optparse, optparse will return them and we can't know if they
    were really provided by the user or not. A solution is to not use
    optparse's default attribute, but use a custom one (that will be copied
    to create the default values of the configuration file).

    """
    def __init__(self, *opts, **attrs):
        self.my_default = attrs.pop('my_default', None)
        super(MyOption, self).__init__(*opts, **attrs)


class ConfigManager(object):
    """读取配置文件类"""
    def __init__(self, fname=None):
        self.options = {}

        self.config_file = fname

        self.casts = {}

        self.parser = parser = optparse.OptionParser(version=version, option_class=MyOption)

        # 启动脚本参数
        group = optparse.OptionGroup(parser, "Base options")
        group.add_option("-f", "--file", dest="config", help="specify alternate config file")
        parser.add_option_group(group)

        # Logging Group
        group = optparse.OptionGroup(parser, "Logging Configuration")
        group.add_option("--logfile", dest="logfile", help="file where the server log will be stored")
        group.add_option("--logrotate", dest="logrotate", action="store_true", my_default=False,
                         help="enable logfile rotation")
        levels = [
            'info', 'warn', 'error', 'debug'
        ]
        group.add_option('--log-level', dest='log_level', type='choice',
                         choices=levels, my_default='info',
                         help='specify the level of the logging. Accepted values: %s.' % (levels,))

        parser.add_option_group(group)

        # DB Group
        group = optparse.OptionGroup(parser, "Database related options")
        group.add_option("-d", "--database", dest="db_name", my_default=False,
                         help="specify the database name")
        group.add_option("-r", "--db_user", dest="db_user", my_default=False,
                         help="specify the database user name")
        group.add_option("-w", "--db_password", dest="db_password", my_default=False,
                         help="specify the database password")
        group.add_option("--db_host", dest="db_host", my_default=False,
                         help="specify the database host")
        group.add_option("--db_port", dest="db_port", my_default=False,
                         help="specify the database port", type="int")
        group.add_option("--db_coll", dest="db_coll", my_default=False,
                         help="specify the database collection")
        parser.add_option_group(group)

        # Copy all optparse options (i.e. MyOption) into self.options.
        for group in parser.option_groups:
            for option in group.option_list:
                if option.dest not in self.options:
                    self.options[option.dest] = option.my_default
                    self.casts[option.dest] = option
        self._parse_config()

    def parse_config(self):
        self._parse_config()
        init_logger()

    def _parse_config(self):
        opt, args = self.parser.parse_args()

        self.rcfile = os.path.abspath(self.config_file or opt.config)
        self.load()

    def load(self):
        p = configparser.ConfigParser()
        try:
            p.read([self.rcfile])
            for (name, value) in p.items('options'):
                if value == 'True' or value == 'true':
                    value = True
                if value == 'False' or value == 'false':
                    value = False
                self.options[name] = value
        except IOError:
            pass
        except configparser.NoSectionError:
            pass

    def __setitem__(self, key, value):
        self.options[key] = value
        if key in self.options and isinstance(self.options[key], str) and \
                        key in self.casts and self.casts[key].type in optparse.Option.TYPE_CHECKER:
            self.options[key] = optparse.Option.TYPE_CHECKER[self.casts[key].type](self.casts[key], key,
                                                                                   self.options[key])

    def __getitem__(self, key):
        return self.options[key]


config = ConfigManager()