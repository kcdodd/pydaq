import argparse

arg_parser = argparse.ArgumentParser(description='PyDAQuri client/server')

arg_parser.add_argument(
  '-s',
  '--server',
  action='store_true',
  help='run as a PyDAQuri server instance')
