# -*- coding: utf-8 -*-

"""Parsers for ComPath's resources."""

import pandas as pd

from .constants import (
    KEGG_REACTOME_URL, KEGG_WIKIPATHWAYS_URL, PATHBANK_KEGG_URL, PATHBANK_REACTOME_URL, PATHBANK_WIKIPATHWAYS_URL,
    REACTOME_HIERARCHICAL_MAPPINGS_URL, SPECIAL_MAPPINGS_URL, WIKIPATHWAYS_REACTOME_URL,
)

__all__ = [
    'get_df',
    # Inter-database
    'get_kegg_reactome_df',
    'get_kegg_wikipathways_df',
    'get_wikipathways_reactome_df',
    'get_pathbank_kegg_df',
    'get_pathbank_reactome_df',
    'get_pathbank_wikipathways_df',
    # Intra-database
    'get_reactome_hierarchy_df',
    'get_special_mappings_df',
]


def get_df(include_reactome_hierarchy: bool = False) -> pd.DataFrame:
    """Get all dataframes.

    :param include_reactome_hierarchy: include Reactome hiearchy?
    :return: dataframe with ComPath dataset
    """
    dfs = [
        get_kegg_wikipathways_df(),
        get_kegg_reactome_df(),
        get_wikipathways_reactome_df(),
        get_pathbank_kegg_df(),
        get_pathbank_reactome_df(),
        get_pathbank_reactome_df(),
        get_special_mappings_df(),
    ]

    if include_reactome_hierarchy:
        dfs.append(get_reactome_hierarchy_df())

    return pd.concat(dfs)


"""Inter-database mappings"""


def get_kegg_wikipathways_df() -> pd.DataFrame:
    """Get KEGG-WikiPathways data."""
    return pd.read_csv(KEGG_WIKIPATHWAYS_URL)


def get_kegg_reactome_df() -> pd.DataFrame:
    """Get KEGG-Reactome data."""
    return pd.read_csv(KEGG_REACTOME_URL)


def get_wikipathways_reactome_df() -> pd.DataFrame:
    """Get WikiPathways-Reactome data."""
    return pd.read_csv(WIKIPATHWAYS_REACTOME_URL)


def get_pathbank_kegg_df() -> pd.DataFrame:
    """Get PathBank-KEGG data."""
    return pd.read_csv(PATHBANK_KEGG_URL)


def get_pathbank_reactome_df() -> pd.DataFrame:
    """Get PathBank-Reactome data."""
    return pd.read_csv(PATHBANK_REACTOME_URL)


def get_pathbank_wikipathways_df() -> pd.DataFrame:
    """Get PathBank-WikiPathways data."""
    return pd.read_csv(PATHBANK_WIKIPATHWAYS_URL)


"""Intra-database mappings"""


def get_special_mappings_df() -> pd.DataFrame:
    """Get special mappings data."""
    return pd.read_csv(SPECIAL_MAPPINGS_URL, usecols=list(range(7)))


def get_reactome_hierarchy_df() -> pd.DataFrame:
    """Get reactome hierarchy data."""
    return pd.read_csv(REACTOME_HIERARCHICAL_MAPPINGS_URL)
