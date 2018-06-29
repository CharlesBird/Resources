import sys
import brent_oil


def main():
    args = sys.argv[1:]
    brent_oil.tools.config.parse_config(args)
    brent_oil.apps.brent_oil_real.main()