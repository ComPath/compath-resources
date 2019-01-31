# -*- coding: utf-8 -*-

"""Command line interface for ComPath's resources."""

import sys
from typing import Optional, TextIO

import click
from compath_resources.manager import get_bel
from pybel import to_pickle


@click.command()
@click.option('-o', '--output', help='file path to write')
@click.option('-f', '--fmt', type=click.Choice(['bel', 'rdf']))
def main(output: Optional[TextIO], fmt: str):
    """Export ComPath resources."""
    graph = get_bel()
    graph.summarize()

    if output is None:
        sys.exit(0)

    if fmt is None or fmt == 'bel':
        to_pickle(graph, output)
    elif fmt == 'rdf':
        click.echo('rdf export not implemented yet')


if __name__ == '__main__':
    main()
