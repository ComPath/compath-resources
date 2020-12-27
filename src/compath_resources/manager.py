# -*- coding: utf-8 -*-

"""Managerial and export functions for ComPath's resources."""

from bio2bel.manager.bel_manager import BELManagerMixin
from bio2bel.manager.cli_manager import CliMixin
from pybel import BELGraph
from .exporters import get_bel

__all__ = [
    'Manager',
]


class Manager(BELManagerMixin, CliMixin):
    """Pathway-pathway equivalences and hierarchies."""

    module_name = 'compath'

    def __init__(self, *args, **kwargs):  # noqa: D107
        self.graph = get_bel()

    @classmethod
    def _get_connection(cls):
        pass

    def is_populated(self) -> bool:  # noqa:D102
        return True

    def summarize(self):  # noqa:D102
        return dict(
            pathways=self.graph.number_of_nodes(),
            mappings=self.graph.number_of_edges(),
        )

    def count_relations(self) -> int:
        """Count the number of ComPath mappings."""
        return self.graph.number_of_edges()

    def to_bel(self) -> BELGraph:
        """Convert ComPath to BEL."""
        return self.graph
