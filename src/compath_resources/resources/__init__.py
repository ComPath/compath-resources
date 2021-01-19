# -*- coding: utf-8 -*-

"""ComPath resources."""

import pandas as pd

from compath_resources.constants import RESOURCES

# Inter-database mappings
KEGG_WIKIPATHWAYS_PATH = RESOURCES / 'kegg_wikipathways.tsv'
KEGG_REACTOME_PATH = RESOURCES / 'kegg_reactome.tsv'
WIKIPATHWAYS_REACTOME_PATH = RESOURCES / 'wikipathways_reactome.tsv'
PATHBANK_KEGG_PATH = RESOURCES / 'pathbank_kegg.tsv'
PATHBANK_REACTOME_PATH = RESOURCES / 'pathbank_reactome.tsv'
PATHBANK_WIKIPATHWAYS_PATH = RESOURCES / 'pathbank_wikipathways.tsv'

# Intra-database mappings
SPECIAL_MAPPINGS_PATH = RESOURCES / 'special_mappings.tsv'
REACTOME_HIERARCHICAL_MAPPINGS_PATH = RESOURCES / 'reactome_hierarchy.tsv'

DECOPATH_PATH = RESOURCES / 'decopath.tsv'


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
        get_decopath_df(),
    ]

    if include_reactome_hierarchy:
        dfs.append(get_reactome_hierarchy_df())

    return pd.concat(dfs)


def get_decopath_df() -> pd.DataFrame:
    """Get the decopath mappings."""
    return pd.read_csv(DECOPATH_PATH, sep='\t')


"""Inter-database mappings"""


def get_kegg_wikipathways_df() -> pd.DataFrame:
    """Get KEGG-WikiPathways data."""
    return pd.read_csv(KEGG_WIKIPATHWAYS_PATH, sep='\t')


def get_kegg_reactome_df() -> pd.DataFrame:
    """Get KEGG-Reactome data."""
    return pd.read_csv(KEGG_REACTOME_PATH, sep='\t')


def get_wikipathways_reactome_df() -> pd.DataFrame:
    """Get WikiPathways-Reactome data."""
    return pd.read_csv(WIKIPATHWAYS_REACTOME_PATH, sep='\t')


def get_pathbank_kegg_df() -> pd.DataFrame:
    """Get PathBank-KEGG data."""
    return pd.read_csv(PATHBANK_KEGG_PATH, sep='\t')


def get_pathbank_reactome_df() -> pd.DataFrame:
    """Get PathBank-Reactome data."""
    return pd.read_csv(PATHBANK_REACTOME_PATH, sep='\t')


def get_pathbank_wikipathways_df() -> pd.DataFrame:
    """Get PathBank-WikiPathways data."""
    return pd.read_csv(PATHBANK_WIKIPATHWAYS_PATH, sep='\t')


"""Intra-database mappings"""


def get_special_mappings_df() -> pd.DataFrame:
    """Get special mappings data."""
    return pd.read_csv(SPECIAL_MAPPINGS_PATH, sep='\t')


def get_reactome_hierarchy_df() -> pd.DataFrame:
    """Get reactome hierarchy data."""
    return pd.read_csv(REACTOME_HIERARCHICAL_MAPPINGS_PATH, sep='\t')
