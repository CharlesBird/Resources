import logging
import logging.handlers
import sys
import os
from . import tools
_logger = logging.getLogger(__name__)

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, _NOTHING, DEFAULT = range(10)
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"
COLOR_PATTERN = "%s%s%%s%s" % (COLOR_SEQ, COLOR_SEQ, RESET_SEQ)
LEVEL_COLOR_MAPPING = {
    logging.DEBUG: (BLUE, DEFAULT),
    logging.INFO: (GREEN, DEFAULT),
    logging.WARNING: (YELLOW, DEFAULT),
    logging.ERROR: (RED, DEFAULT),
    logging.CRITICAL: (WHITE, RED),
}
_logger_init = False


class NormalFormatter(logging.Formatter):
    def format(self, record):
        record.pid = os.getpid()
        return logging.Formatter.format(self, record)


class ColoredFormatter(NormalFormatter):
    def format(self, record):
        fg_color, bg_color = LEVEL_COLOR_MAPPING.get(record.levelno, (GREEN, DEFAULT))
        record.levelname = COLOR_PATTERN % (30 + fg_color, 40 + bg_color, record.levelname)
        return NormalFormatter.format(self, record)


def init_logger():
    global _logger_init
    if _logger_init:
        return
    _logger_init = True

    # create a format for log messages and dates
    format = '%(asctime)s %(pid)s %(levelname)s %(name)s: %(message)s'
    # Normal Handler on stderr
    handler = logging.StreamHandler()

    if tools.config['logfile']:
        logf = tools.config['logfile']
        try:
            # We check we have the right location for the log files
            dirname = os.path.dirname(logf)
            if dirname and not os.path.isdir(dirname):
                os.makedirs(dirname)
            if tools.config['logrotate'] is not False:
                handler = logging.handlers.TimedRotatingFileHandler(filename=logf, when='D', interval=1, backupCount=30)
            elif os.name == 'posix':
                handler = logging.handlers.WatchedFileHandler(logf)
            else:
                handler = logging.FileHandler(logf)
        except Exception:
            sys.stderr.write("ERROR: couldn't create the logfile directory. Logging to the standard output.\n")

    def is_a_tty(stream):
        return hasattr(stream, 'fileno') and os.isatty(stream.fileno())

    if os.name == 'posix' and isinstance(handler, logging.StreamHandler) and is_a_tty(handler.stream):
        formatter = ColoredFormatter(format)
    else:
        formatter = NormalFormatter(format)
    handler.setFormatter(formatter)

    logging.getLogger().addHandler(handler)
    logger = logging.getLogger()
    logger.setLevel(tools.config['log_level'].upper())

    _logger.debug('logger level set: "%s"', tools.config['log_level'])