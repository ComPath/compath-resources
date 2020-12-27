# -*- coding: utf-8 -*-

"""Constants for ComPath's resources."""

import pystow

COMPATH_HOME = pystow.get('compath')

_BASE_URL = 'https://raw.githubusercontent.com/ComPath/resources/master/mappings'

# Inter-database mappings
KEGG_WIKIPATHWAYS_URL = f'{_BASE_URL}/kegg_wikipathways.csv'
KEGG_REACTOME_URL = f'{_BASE_URL}/kegg_reactome.csv'
WIKIPATHWAYS_REACTOME_URL = f'{_BASE_URL}/wikipathways_reactome.csv'

PATHBANK_KEGG_URL = f'{_BASE_URL}/pathbank_kegg.csv'
PATHBANK_REACTOME_URL = f'{_BASE_URL}/pathbank_reactome.csv'
PATHBANK_WIKIPATHWAYS_URL = f'{_BASE_URL}/pathbank_wikipathwayss.csv'

# Intra-database mappings
SPECIAL_MAPPINGS_URL = f'{_BASE_URL}/special_mappings.csv'
REACTOME_HIERARCHICAL_MAPPINGS_URL = f'{_BASE_URL}/reactome_hierarchy.csv'
