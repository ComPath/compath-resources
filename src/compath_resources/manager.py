# -*- coding: utf-8 -*-

"""Managerial and export functions for ComPath's resources."""

from bio2bel.manager.bel_manager import BELManagerMixin
from bio2bel.manager.cli_manager import CliMixin
from compath_resources.parser import get_df
from pybel import BELGraph
from pybel.dsl import BiologicalProcess

__all__ = [
    'Manager',
    'get_bel',
]


class Manager(BELManagerMixin, CliMixin):
    """Pathway-pathway equivalences and hierarchies."""

    module_name = 'compath'

    def __init__(self, *args, **kwargs):  # noqa: D107
        self.graph = get_bel()

    @classmethod
    def _get_connection(cls):
        pass

    def is_populated(self) -> bool:
        return True

    def summarize(self):
        return dict(
            pathways=self.graph.number_of_nodes(),
            mappings=self.graph.number_of_edges(),
        )

    def count_relations(self) -> int:
        """Count the numebr of ComPath mappings."""
        return self.graph.number_of_edges()

    def to_bel(self) -> BELGraph:
        """Convert ComPath to BEL."""
        return self.graph


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
