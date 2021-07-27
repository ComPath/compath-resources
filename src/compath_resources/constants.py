# -*- coding: utf-8 -*-

"""Constants for ComPath's resources."""

import os
from pathlib import Path

import pystow

COMPATH_HOME = pystow.join('compath')

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = Path(os.path.abspath(os.path.join(HERE, os.pardir, os.pardir)))
RESOURCES = Path(HERE) / 'resources'
DOCS_DIRECTORY = ROOT / 'docs'
IMG_DIRECTORY = DOCS_DIRECTORY / 'img'
DATA_DIRECTORY = DOCS_DIRECTORY / 'data'
DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)

_BASE_URL = 'https://raw.githubusercontent.com/ComPath/resources/master/mappings'

# Inter-database mappings URLs

KEGG_WIKIPATHWAYS_URL = f'{_BASE_URL}/kegg_wikipathways.csv'
KEGG_REACTOME_URL = f'{_BASE_URL}/kegg_reactome.csv'
WIKIPATHWAYS_REACTOME_URL = f'{_BASE_URL}/wikipathways_reactome.csv'
PATHBANK_KEGG_URL = f'{_BASE_URL}/pathbank_kegg.csv'
PATHBANK_REACTOME_URL = f'{_BASE_URL}/pathbank_reactome.csv'
PATHBANK_WIKIPATHWAYS_URL = f'{_BASE_URL}/pathbank_wikipathways.csv'

# Intra-database mappings URLS

SPECIAL_MAPPINGS_URL = f'{_BASE_URL}/special_mappings.csv'
REACTOME_HIERARCHICAL_MAPPINGS_URL = f'{_BASE_URL}/reactome_hierarchy.tsv'
