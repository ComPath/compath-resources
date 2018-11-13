# -*- coding: utf-8 -*-

"""Parsers for ComPath's resources."""

import pandas as pd

from compath_resources.constants import (
    KEGG_REACTOME_URL, KEGG_WIKIPATHWAYS_URL, REACTOME_HIERARCHICAL_MAPPINGS_URL,
    SPECIAL_MAPPINGS_URL, WIKIPATHWAYS_REACTOME_URL,
)

__all__ = [
    'get_df',
]


def get_df() -> pd.DataFrame:
    """Get all data in a frame."""
    return pd.concat([
        pd.read_csv(KEGG_WIKIPATHWAYS_URL),
        pd.read_csv(KEGG_REACTOME_URL),
        pd.read_csv(WIKIPATHWAYS_REACTOME_URL),
        pd.read_csv(SPECIAL_MAPPINGS_URL, usecols=list(range(7))),
        pd.read_csv(REACTOME_HIERARCHICAL_MAPPINGS_URL),
    ])
