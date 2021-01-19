# -*- coding: utf-8 -*-

"""Sync the files in the mappings folder of the git repository inside the :mod:`compath_resources` module.

.. warning:: DO NOT RELY ON THIS CODE IN YOUR PACKAGE. USE :mod:`compath_resources.resources`.
"""

import pandas as pd

import compath_resources.resources as rsc
from compath_resources.constants import ROOT

_MAPPINGS_DIRECTORY = ROOT / 'mappings'


def _fix_kegg_identifier(prefix, identifier) -> str:
    if prefix == 'kegg.pathway' and identifier.startswith('path:'):
        return identifier[len('path:'):]
    return identifier


def _fix_kegg_prefix(prefix: str) -> str:
    if prefix == 'kegg':
        return 'kegg.pathway'
    return prefix


def _fix_mapping(mapping: str) -> str:
    if mapping == 'equivalentTo':
        return 'skos:exactMatch'
    elif mapping == 'isPartOf':
        return 'BFO:0000050'
    else:
        raise ValueError(f'unknown mapping: {mapping}')


def _fix_kegg_entries(df: pd.DataFrame) -> None:
    df['Source Resource'] = df['Source Resource'].map(_fix_kegg_prefix)
    df['Target Resource'] = df['Target Resource'].map(_fix_kegg_prefix)
    df['Source ID'] = [
        _fix_kegg_identifier(prefix, identifier)
        for prefix, identifier in df[['Source Resource', 'Source ID']].values
    ]
    df['Target ID'] = [
        _fix_kegg_identifier(prefix, identifier)
        for prefix, identifier in df[['Target Resource', 'Target ID']].values
    ]
    df['Mapping Type'] = df['Mapping Type'].map(_fix_mapping)


def _import_decopath_df() -> pd.DataFrame:
    """Get the decopath dataframe."""
    excel_file = pd.ExcelFile(_MAPPINGS_DIRECTORY / 'decopath_ontology.xlsx', engine='openpyxl')
    dfs = []
    for sheet_name in excel_file.sheet_names:
        df = excel_file.parse(sheet_name, usecols=list(range(7)))
        df = df.dropna()
        dfs.append(df)
    return pd.concat(dfs)


def _import_df(path, sep: str = ',', **kwargs):
    df = pd.read_csv(path, sep=sep, **kwargs)
    _fix_kegg_entries(df)
    return df


def _import_kegg_wikipathways_df() -> pd.DataFrame:
    """Get KEGG-WikiPathways data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'kegg_wikipathways.csv')


def _import_kegg_reactome_df() -> pd.DataFrame:
    """Get KEGG-Reactome data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'kegg_reactome.csv')


def _import_wikipathways_reactome_df() -> pd.DataFrame:
    """Get WikiPathways-Reactome data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'wikipathways_reactome.csv')


def _import_pathbank_kegg_df() -> pd.DataFrame:
    """Get PathBank-KEGG data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'pathbank_kegg.csv')


def _import_pathbank_reactome_df() -> pd.DataFrame:
    """Get PathBank-Reactome data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'pathbank_reactome.csv')


def _import_pathbank_wikipathways_df() -> pd.DataFrame:
    """Get PathBank-WikiPathways data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'pathbank_wikipathways.csv')


def _import_special_mappings_df() -> pd.DataFrame:
    """Get special mappings data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'special_mappings.csv', usecols=list(range(7)))


def _import_reactome_hierarchy_df() -> pd.DataFrame:
    """Get reactome hierarchy data."""
    return _import_df(_MAPPINGS_DIRECTORY / 'reactome_hierarchy.tsv', sep='\t')


def _main():
    """Import all mappings into the package."""
    _import_decopath_df().to_csv(rsc.DECOPATH_PATH, sep='\t', index=False)
    _import_kegg_wikipathways_df().to_csv(rsc.KEGG_WIKIPATHWAYS_PATH, sep='\t', index=False)
    _import_kegg_reactome_df().to_csv(rsc.KEGG_REACTOME_PATH, sep='\t', index=False)
    _import_wikipathways_reactome_df().to_csv(rsc.WIKIPATHWAYS_REACTOME_PATH, sep='\t', index=False)
    _import_pathbank_kegg_df().to_csv(rsc.PATHBANK_KEGG_PATH, sep='\t', index=False)
    _import_pathbank_reactome_df().to_csv(rsc.PATHBANK_REACTOME_PATH, sep='\t', index=False)
    _import_pathbank_wikipathways_df().to_csv(rsc.PATHBANK_WIKIPATHWAYS_PATH, sep='\t', index=False)
    _import_special_mappings_df().to_csv(rsc.SPECIAL_MAPPINGS_PATH, sep='\t', index=False)
    _import_reactome_hierarchy_df().to_csv(rsc.REACTOME_HIERARCHICAL_MAPPINGS_PATH, sep='\t', index=False)


if __name__ == '__main__':
    _main()
