# -*- coding: utf-8 -*-

"""Test data integrity."""

import unittest

import pandas as pd

from compath_resources.import_mappings import (
    _import_decopath_df, _import_kegg_reactome_df, _import_kegg_wikipathways_df, _import_pathbank_kegg_df,
    _import_pathbank_reactome_df, _import_pathbank_wikipathways_df, _import_reactome_hierarchy_df,
    _import_special_mappings_df, _import_wikipathways_reactome_df,
)
from compath_resources.resources import (
    get_decopath_df, get_kegg_reactome_df, get_kegg_wikipathways_df, get_pathbank_kegg_df, get_pathbank_reactome_df,
    get_pathbank_wikipathways_df, get_reactome_hierarchy_df, get_special_mappings_df, get_wikipathways_reactome_df,
)


class TestIntegrity(unittest.TestCase):
    """Test case for checking data integrity."""

    def test_import(self):
        """Test the exported data is the same as the excel."""
        for importer, getter in [
            (_import_decopath_df, get_decopath_df),
            (_import_kegg_reactome_df, get_kegg_reactome_df),
            (_import_pathbank_reactome_df, get_pathbank_reactome_df),
            (_import_pathbank_kegg_df, get_pathbank_kegg_df),
            (_import_wikipathways_reactome_df, get_wikipathways_reactome_df),
            (_import_reactome_hierarchy_df, get_reactome_hierarchy_df),
            (_import_special_mappings_df, get_special_mappings_df),
            (_import_pathbank_wikipathways_df, get_pathbank_wikipathways_df),
            (_import_kegg_wikipathways_df, get_kegg_wikipathways_df),
        ]:
            with self.subTest(name=importer.__name__):
                xlsx_df = importer()
                self.assertIsInstance(xlsx_df, pd.DataFrame)
                tsv_df = getter()
                self.assertIsInstance(tsv_df, pd.DataFrame)
                self.assertTrue((xlsx_df.values == tsv_df.values).all())
