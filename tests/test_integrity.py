# -*- coding: utf-8 -*-

"""Test data integrity."""

import re
import unittest

import bioregistry
import pandas as pd

from compath_resources.resources import (
    get_decopath_df, get_kegg_reactome_df, get_kegg_wikipathways_df, get_pathbank_kegg_df, get_pathbank_reactome_df,
    get_pathbank_wikipathways_df, get_reactome_hierarchy_df, get_special_mappings_df, get_wikipathways_reactome_df,
)
from compath_resources.sync import (
    _import_decopath_df, _import_kegg_reactome_df, _import_kegg_wikipathways_df, _import_pathbank_kegg_df,
    _import_pathbank_reactome_df, _import_pathbank_wikipathways_df, _import_reactome_hierarchy_df,
    _import_special_mappings_df, _import_wikipathways_reactome_df,
)

DATA = [
    (_import_decopath_df, get_decopath_df),
    (_import_kegg_reactome_df, get_kegg_reactome_df),
    (_import_pathbank_reactome_df, get_pathbank_reactome_df),
    (_import_pathbank_kegg_df, get_pathbank_kegg_df),
    (_import_wikipathways_reactome_df, get_wikipathways_reactome_df),
    (_import_reactome_hierarchy_df, get_reactome_hierarchy_df),
    (_import_special_mappings_df, get_special_mappings_df),
    (_import_pathbank_wikipathways_df, get_pathbank_wikipathways_df),
    (_import_kegg_wikipathways_df, get_kegg_wikipathways_df),
]


class TestIntegrity(unittest.TestCase):
    """Test case for checking data integrity."""

    def test_curies(self):
        """Test correct prefixes and identifiers."""
        registry = bioregistry.read_bioregistry()
        registry['decopath'] = {}  # TODO decopath needs a real resource and an entry in the bioregistry

        miriam_patterns = {
            k: re.compile(entry['miriam']['pattern'])
            for k, entry in registry.items()
            if 'miriam' in entry
        }

        dataframes = {
            getter.__name__.removeprefix('get_').removesuffix('_df'): getter()
            for _, getter in DATA
        }

        rows = ['Source Resource', 'Source ID', 'Target Resource', 'Target ID']
        for name, df in dataframes.items():
            with self.subTest(name=name):
                for i, (source_prefix, source_id, target_prefix, target_id) in enumerate(df[rows].values):
                    self.assertIn(source_prefix, registry.keys())
                    self.assertNotEqual(source_prefix, 'kegg')
                    self.assertFalse(
                        bioregistry.is_deprecated(source_prefix),
                        msg=f'[{name}, row {i}] deprecated source prefix: {source_prefix}',
                    )
                    if source_regex := miriam_patterns.get(source_prefix):
                        self.assertRegex(
                            source_id, source_regex,
                            msg=f'[{name}, row {i}] source prefix: {source_prefix}',
                        )
                    self.assertIn(target_prefix, registry.keys())
                    self.assertNotEqual(target_prefix, 'kegg')
                    self.assertFalse(
                        bioregistry.is_deprecated(target_prefix),
                        msg=f'[{name}, row {i}] deprecated target prefix: {target_prefix}',
                    )
                    if target_regex := miriam_patterns.get(target_prefix):
                        self.assertRegex(
                            target_id, target_regex,
                            msg=f'[{name}, row {i}] target prefix: {target_prefix}',
                        )

    def test_import(self):
        """Test the exported data is the same as the excel."""
        for importer, getter in DATA:
            with self.subTest(name=importer.__name__):
                xlsx_df = importer()
                self.assertIsInstance(xlsx_df, pd.DataFrame)
                tsv_df = getter()
                self.assertIsInstance(tsv_df, pd.DataFrame)
                self.assertTrue(
                    (xlsx_df.values == tsv_df.values).all(),
                    msg='\nFiles are out of sync.\nrun `python -m compath_resources.sync',
                )
