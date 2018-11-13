# -*- coding: utf-8 -*-

"""Export functions for ComPath's resources."""

import sys

import click
import pandas as pd

from pybel import BELGraph, to_pickle
from pybel.dsl import BiologicalProcess

__all__ = [
    'get_df',
    'get_bel',
]

KEGG_WIKIPATHWAYS_URL = 'https://raw.githubusercontent.com/ComPath/resources/master/mappings/kegg_wikipathways.csv'
KEGG_REACTOME_URL = 'https://raw.githubusercontent.com/ComPath/resources/master/mappings/kegg_reactome.csv'
WIKIPATHWAYS_REACTOME_URL = 'https://raw.githubusercontent.com/ComPath/resources/master/mappings/wikipathways_reactome.csv'
SPECIAL_MAPPINGS_URL = 'https://raw.githubusercontent.com/ComPath/resources/master/mappings/special_mappings.csv'


def get_df() -> pd.DataFrame:
    """Get all data in a frame."""
    return pd.concat([
        pd.read_csv(KEGG_WIKIPATHWAYS_URL),
        pd.read_csv(KEGG_REACTOME_URL),
        pd.read_csv(WIKIPATHWAYS_REACTOME_URL),
        pd.read_csv(SPECIAL_MAPPINGS_URL, usecols=list(range(7))),
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
@click.option('-o', '--output', help='file path to write', required=True)
@click.option('-f', '--fmt', type=click.Choice(['bel', 'rdf']), default='bel')
def main(output, fmt):
    """"""
    if fmt == 'bel':
        graph = get_bel()
        graph.summarize()
        to_pickle(graph, output)

    elif fmt == 'rdf':
        click.echo('rdf export not implemented yet')


if __name__ == '__main__':
    main()
