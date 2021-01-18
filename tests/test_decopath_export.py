# -*- coding: utf-8 -*-

"""Test the decopath export."""

import unittest

import pandas as pd

from compath_resources.convert_decopath import DECOPATH_TSV_PATH, get_decopath_df


class TestDecopathExport(unittest.TestCase):
    """Test the decopath export."""

    def test_export(self):
        """Test the exported data is the same as the excel."""
        xlsx_df = get_decopath_df()
        tsv_df = pd.read_csv(DECOPATH_TSV_PATH, sep='\t')
        self.assertTrue((xlsx_df.values == tsv_df.values).all())
