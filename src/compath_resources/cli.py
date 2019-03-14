# -*- coding: utf-8 -*-

"""Command line interface for ComPath's resources."""

from .manager import Manager

main = Manager.get_cli()

if __name__ == '__main__':
    main()
