# -*- coding: utf-8 -*-

"""Test data integrity."""

import os
import unittest

import bioregistry
import pandas as pd

from compath_resources.constants import MAPPINGS_DIRECTORY
from compath_resources.convert_decopath import DECOPATH_TSV_PATH, get_decopath_df


class TestIntegrity(unittest.TestCase):
    """Test case for checking data integrity."""

    def setUp(self) -> None:
        """Set up integrity tests."""
        self.registry = bioregistry.read_bioregistry()
        self.registry['decopath'] = ...  # TODO decopath needs a real resource and an entry in the bioregistry
        self.x = {}
        for name in os.listdir(MAPPINGS_DIRECTORY):
            if name.endswith('.tsv'):
                print(name)
                self.x[name] = pd.read_csv(os.path.join(MAPPINGS_DIRECTORY, name), sep='\t')
            elif name.endswith('.csv'):
                print(name)
                self.x[name] = pd.read_csv(os.path.join(MAPPINGS_DIRECTORY, name), sep=',')

    def test_prefixes(self):
        """Test correct prefixes."""
        for name, df in self.x.items():
            with self.subTest(name=name):
                source_prefixes = df['Source Resource'].unique()
                for prefix in source_prefixes:
                    self.assertIn(prefix, self.registry)
                    self.assertFalse(bioregistry.is_deprecated(prefix), msg=f'deprecated source prefix: {prefix}')
                target_prefixes = df['Target Resource'].unique()
                for prefix in target_prefixes:
                    self.assertIn(prefix, self.registry)
                    self.assertFalse(bioregistry.is_deprecated(prefix), msg=f'deprecated target prefix: {prefix}')

    def test_decopath_export(self):
        """Test the exported data is the same as the excel."""
        xlsx_df = get_decopath_df()
        tsv_df = pd.read_csv(DECOPATH_TSV_PATH, sep='\t')
        self.assertTrue((xlsx_df.values == tsv_df.values).all())
