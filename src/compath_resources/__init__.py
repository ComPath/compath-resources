# -*- coding: utf-8 -*-

"""Export functions for ComPath's resources."""

import os

import click
import pandas as pd

from pybel import BELGraph, to_pickle
from pybel.dsl import BiologicalProcess

__all__ = [
    'get_df',
    'get_bel',
]

HERE = os.path.abspath(os.path.dirname(__file__))

MAPPINGS_FOLDER = os.path.join(HERE, 'mappings')
KEGG_WIKIPATHWAYS = os.path.abspath(os.path.join(MAPPINGS_FOLDER, 'kegg_wikipathways.csv'))
KEGG_REACTOME = os.path.abspath(os.path.join(MAPPINGS_FOLDER, 'kegg_reactome.csv'))
WIKIPATHWAYS_REACTOME = os.path.abspath(os.path.join(MAPPINGS_FOLDER, 'wikipathways_reactome.csv'))


def get_df() -> pd.DataFrame:
    """Get all data in a frame."""
    return pd.concat([
        pd.read_csv(KEGG_WIKIPATHWAYS),
        pd.read_csv(KEGG_REACTOME),
        pd.read_csv(WIKIPATHWAYS_REACTOME),
    ])


def get_bel() -> BELGraph:
    """Get the ComPath mappings as BEL."""
    graph = BELGraph(
        name='ComPath Mappings',
        version='1.0.0',
        description='Hierarchical and equivalence relations between entries in KEGG, Reactome, and WikiPathways.'
    )
    df = get_df()
    for i, (source_ns, source_id, source_name, relation, target_ns, target_id, target_name) in df.iterrows():
        source = BiologicalProcess(
            namespace=source_ns,
            identifier=source_id,
            name=source_name,
        )
        target = BiologicalProcess(
            namespace=target_ns,
            identifier=target_id,
            name=target_name,
        )
        if relation == 'isPartOf':
            graph.add_part_of(source, target)
        elif relation == 'equivalentTo':
            graph.add_equivalence(source, target)
        else:
            raise ValueError(f'invalid mapping type in row {i}: {relation}')

    return graph


@click.command()
@click.option('-o', '--output', type=click.File('w'), help='lol')
@click.option('-f', '--fmt', type=click.Choice(['bel', 'rdf']))
def main(output, fmt):
    """"""
    if fmt == 'bel':
        graph = get_bel()
        to_pickle(graph, output)

    elif fmt == 'rdf':
        click.echo('rdf export not implemented yet')


if __name__ == '__main__':
    main()
