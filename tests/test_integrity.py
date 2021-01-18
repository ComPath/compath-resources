# -*- coding: utf-8 -*-

"""Test data integrity."""

import os
import pathlib
import unittest

import bioregistry
import pandas as pd

HERE = pathlib.Path(os.path.dirname(__file__))
MAPPINGS_DIRECTORY = os.path.abspath(os.path.join(HERE, os.pardir, 'mappings'))


class TestIntegrity(unittest.TestCase):
    """Test case for checking data integrity."""

    def setUp(self) -> None:
        """Set up integrity tests."""
        self.registry = bioregistry.read_bioregistry()
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
