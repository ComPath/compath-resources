# -*- coding: utf-8 -*-

"""Parsers for ComPath's resources."""

import pandas as pd

from compath_resources.constants import (
    KEGG_REACTOME_URL, KEGG_WIKIPATHWAYS_URL, REACTOME_HIERARCHICAL_MAPPINGS_URL,
    SPECIAL_MAPPINGS_URL, WIKIPATHWAYS_REACTOME_URL,
)

__all__ = [
    'get_df',
    'get_kegg_reactome_df',
    'get_kegg_wikipathways_df',
    'get_wikipathways_reactome_df',
    'get_reactome_hierarchy_df',
    'get_special_mappings_df',
]


def get_df(reactome: bool = False) -> pd.DataFrame:
    """Get all dataframes.

    :param reactome: include Reactome hiearchy?
    :return: dataframe with ComPath dataset
    """
    dfs = [
        get_kegg_wikipathways_df(),
        get_kegg_reactome_df(),
        get_wikipathways_reactome_df(),
        get_special_mappings_df(),
    ]

    if reactome:
        dfs.append(get_reactome_hierarchy_df())

    return pd.concat(dfs)


def get_kegg_wikipathways_df() -> pd.DataFrame:
    return pd.read_csv(KEGG_WIKIPATHWAYS_URL)


def get_kegg_reactome_df() -> pd.DataFrame:
    return pd.read_csv(KEGG_REACTOME_URL)


def get_wikipathways_reactome_df() -> pd.DataFrame:
    return pd.read_csv(WIKIPATHWAYS_REACTOME_URL)


def get_special_mappings_df() -> pd.DataFrame:
    return pd.read_csv(SPECIAL_MAPPINGS_URL, usecols=list(range(7)))


def get_reactome_hierarchy_df() -> pd.DataFrame:
    return pd.read_csv(REACTOME_HIERARCHICAL_MAPPINGS_URL)
