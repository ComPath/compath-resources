# -*- coding: utf-8 -*-

"""Command line interface for ComPath's resources."""

import click

from compath_resources.manager import get_bel
from pybel import to_pickle


@click.command()
@click.option('-o', '--output', help='file path to write')
@click.option('-f', '--fmt', type=click.Choice(['bel', 'rdf']), default='bel')
def main(output, fmt):
    """Export ComPath resources."""
    if fmt == 'bel':
        graph = get_bel()
        graph.summarize()
        to_pickle(graph, output)

    elif fmt == 'rdf':
        click.echo('rdf export not implemented yet')


if __name__ == '__main__':
    main()
