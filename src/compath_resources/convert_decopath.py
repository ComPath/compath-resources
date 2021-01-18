# -*- coding: utf-8 -*-

"""Turn the decopath XLSX into a usable TSV."""

import pandas as pd

from compath_resources.constants import MAPPINGS_DIRECTORY

__all__ = [
    'get_decopath_df',
    'convert_decopath',
]

DECOPATH_XLSX_PATH = MAPPINGS_DIRECTORY / 'decopath_ontology.xlsx'
DECOPATH_TSV_PATH = MAPPINGS_DIRECTORY / 'decopath.tsv'


def get_decopath_df() -> pd.DataFrame:
    """Get the decopath dataframe."""
    excel_file = pd.ExcelFile(DECOPATH_XLSX_PATH, engine='openpyxl')
    dfs = []
    for sheet_name in excel_file.sheet_names:
        df = excel_file.parse(sheet_name, usecols=list(range(7)))
        df = df.dropna()
        dfs.append(df)
    return pd.concat(dfs)


def convert_decopath():
    """Export the decopath dataframe as a TSV."""
    get_decopath_df().to_csv(DECOPATH_TSV_PATH, sep='\t', index=False)


if __name__ == '__main__':
    convert_decopath()
