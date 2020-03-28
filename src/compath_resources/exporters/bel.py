# -*- coding: utf-8 -*-

"""Export ComPath resources as BEL."""

import pybel
from pybel.dsl import BiologicalProcess
from ..parser import get_df

__all__ = [
    'get_bel',
]


def get_bel() -> pybel.BELGraph:
    """Get the ComPath mappings as BEL."""
    graph = pybel.BELGraph(
        name='ComPath Mappings',
        version='1.1.0',
        description='Hierarchical and equivalence relations between entries in KEGG, Reactome, PathBank,'
                    ' and WikiPathways.'
    )
    df = get_df()
    for source_ns, source_id, source_name, relation, target_ns, target_id, target_name in df.values:
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
            raise ValueError(f'invalid mapping with relation: {relation}')

    return graph
