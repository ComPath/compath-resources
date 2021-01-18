# -*- coding: utf-8 -*-

"""Test data integrity."""

import os
import re
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
        self.registry['decopath'] = {}  # TODO decopath needs a real resource and an entry in the bioregistry
        self.x = {}
        self.miriam_patterns = {
            k: re.compile(entry['miriam']['pattern'])
            for k, entry in self.registry.items()
            if 'miriam' in entry
        }
        for name in os.listdir(MAPPINGS_DIRECTORY):
            if name.endswith('.tsv'):
                print(name)
                self.x[name] = pd.read_csv(os.path.join(MAPPINGS_DIRECTORY, name), sep='\t')
            elif name.endswith('.csv'):
                print(name)
                self.x[name] = pd.read_csv(os.path.join(MAPPINGS_DIRECTORY, name), sep=',')

    def test_prefixes(self):
        """Test correct prefixes."""
        rows = ['Source Resource', 'Source ID', 'Target Resource', 'Target ID']
        for name, df in self.x.items():
            with self.subTest(name=name):
                for i, (source_prefix, source_id, target_prefix, target_id) in enumerate(df[rows].values):
                    self.assertIn(source_prefix, self.registry.keys())
                    self.assertNotEqual(source_prefix, 'kegg')
                    self.assertFalse(
                        bioregistry.is_deprecated(source_prefix),
                        msg=f'[{name}, row {i}] deprecated source prefix: {source_prefix}',
                    )
                    if source_regex := self.miriam_patterns.get(source_prefix):
                        self.assertRegex(
                            source_id, source_regex,
                            msg=f'[{name}, row {i}] source prefix: {source_prefix}',
                        )
                    self.assertIn(target_prefix, self.registry.keys())
                    self.assertNotEqual(target_prefix, 'kegg')
                    self.assertFalse(
                        bioregistry.is_deprecated(target_prefix),
                        msg=f'[{name}, row {i}] deprecated target prefix: {target_prefix}',
                    )
                    if target_regex := self.miriam_patterns.get(target_prefix):
                        self.assertRegex(
                            target_id, target_regex,
                            msg=f'[{name}, row {i}] target prefix: {target_prefix}',
                        )

    def test_decopath_export(self):
        """Test the exported data is the same as the excel."""
        xlsx_df = get_decopath_df()
        tsv_df = pd.read_csv(DECOPATH_TSV_PATH, sep='\t')
        self.assertTrue((xlsx_df.values == tsv_df.values).all())
