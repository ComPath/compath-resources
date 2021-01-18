# -*- coding: utf-8 -*-

"""Constants for ComPath's resources."""

import os
from pathlib import Path

import pystow

COMPATH_HOME = pystow.get('compath')

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = Path(os.path.abspath(os.path.join(HERE, os.pardir, os.pardir)))
MAPPINGS_DIRECTORY = ROOT / 'mappings'
DOCS_DIRECTORY = ROOT / 'docs'
IMG_DIRECTORY = DOCS_DIRECTORY / 'img'

_BASE_URL = 'https://raw.githubusercontent.com/ComPath/resources/master/mappings'

# Inter-database mappings
KEGG_WIKIPATHWAYS_URL = f'{_BASE_URL}/kegg_wikipathways.csv'
KEGG_WIKIPATHWAYS_PATH = MAPPINGS_DIRECTORY / 'kegg_wikipathways.csv'

KEGG_REACTOME_URL = f'{_BASE_URL}/kegg_reactome.csv'
KEGG_REACTOME_PATH = MAPPINGS_DIRECTORY / 'kegg_reactome.csv'

WIKIPATHWAYS_REACTOME_URL = f'{_BASE_URL}/wikipathways_reactome.csv'
WIKIPATHWAYS_REACTOME_PATH = MAPPINGS_DIRECTORY / 'wikipathways_reactome.csv'

PATHBANK_KEGG_URL = f'{_BASE_URL}/pathbank_kegg.csv'
PATHBANK_KEGG_PATH = MAPPINGS_DIRECTORY / 'pathbank_kegg.csv'

PATHBANK_REACTOME_URL = f'{_BASE_URL}/pathbank_reactome.csv'
PATHBANK_REACTOME_PATH = MAPPINGS_DIRECTORY / 'pathbank_reactome.csv'

PATHBANK_WIKIPATHWAYS_URL = f'{_BASE_URL}/pathbank_wikipathwayss.csv'
PATHBANK_WIKIPATHWAYS_PATH = MAPPINGS_DIRECTORY / 'pathbank_wikipathwayss.csv'

# Intra-database mappings
SPECIAL_MAPPINGS_URL = f'{_BASE_URL}/special_mappings.csv'
SPECIAL_MAPPINGS_PATH = MAPPINGS_DIRECTORY / 'special_mappings.csv'

REACTOME_HIERARCHICAL_MAPPINGS_URL = f'{_BASE_URL}/reactome_hierarchy.tsv'
REACTOME_HIERARCHICAL_MAPPINGS_PATH = MAPPINGS_DIRECTORY / 'reactome_hierarchy.tsv'
