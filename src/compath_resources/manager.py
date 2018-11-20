# -*- coding: utf-8 -*-

"""Managerial and export functions for ComPath's resources."""

from bio2bel.manager.bel_manager import BELManagerMixin
from pybel import BELGraph
from pybel.dsl import BiologicalProcess

from compath_resources.parser import get_df

__all__ = [
    'Manager',
    'get_bel',
]


class Manager(BELManagerMixin):
    """Manager for ComPath resources."""

    def __init__(self, *args, **kwargs):
        pass

    def _get_connection(self):
        pass

    def to_bel(self) -> BELGraph:
        """Convert ComPath to BEL."""
        return get_bel()


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
