#! /usr/bin/env python3
'''
paro: Easily create deployment shell scripts
'''
import argparse
import logging
from libs.dotdir import DotDir
from libs.profile import ParoFile
from libs import errors

VERSION = (0, 0, 1)
logger = logging.getLogger(__file__)

DESCRIPTION = '''
Paro lets you quickly create deploymet shell scripts for cloud
servers by providing modules for file transfer, software installation,
and more. It will automatically compress the output to better support
the size limits by many hosting providers.
'''


class Init():
    def __init__(self, args):
        self.args = args


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='paro', description=DESCRIPTION)

    # Subcommands
    sps = parser.add_subparsers(title='subcommands')

    sp_init = sps.add_parser('init', help='Initialize a new Paro project')
    sp_init.set_defaults(subcommand='init')

    sp_build = sps.add_parser('build', help='Build the shell script')
    sp_build.add_argument('--no-compress', action='store_true',
                          help='Do not attempt to compress output')
    sp_build.set_defaults(subcommand='build')

    sp_list = sps.add_parser('list', help='List current build instructions')
    sp_list.set_defaults(subcommand='list')

    sp_makefile = sps.add_parser('makefile', help='Create a makefile for Paro')
    sp_makefile.set_defaults(subcommand='makefile')

    sp_version = sps.add_parser('version', help='Display version information')
    sp_version.set_defaults(subcommand='version')

    # Log group
    group = parser.add_argument_group('Log Settings')
    group.add_argument('--info', action='store_true',
                       help='Display additional information')
    group.add_argument('--debug', action='store_true',
                       help='Display debug-level information')

    # Parse arguments
    args = parser.parse_args()

    # Initial setup
    if args.info:
        logger.setLevel(logging.INFO)
    if args.warning:
        logger.setLevel(logging.WARN)

    # Execute subcommand
    if args.subcommand == 'init':
        # Create .paro directory and paro.yaml file
        try:
            dotdir = DotDir()
            dotdir.create()
            logger.info('Created .paro directory at: %s' % dotdir.path)
        except errors.DotDirAlreadyExists:
            logger.error('The .paro directory already exists.')
            logger.error('Aborting!')
            exit(1)

        try:
            parofile = ParoFile()
            parofile.create()
            logger.info('Created paro.yaml file at: %s' % parofile.path)
        except errors.ParoFileAlreadyExists:
            logger.error('The paro.yaml file already exists.')
            logger.error('Aborting!')
            exit(1)

        print('Initialized empty paro project.')

    elif args.subcommand == 'list':
        # List current rules in paro.yaml
        pass

    elif args.subcommand == 'makefile':
        # Generate a makefile to trigger Paro
        pass

    elif args.subcommand == 'version':
        # Print the current version information
        print('Paro v%i.%i.%i' % VERSION)
