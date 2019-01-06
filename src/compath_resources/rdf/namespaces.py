# -*- coding: utf-8 -*-

"""Namespacs for RDFLib."""

from rdflib import Namespace

KEGG_PREFIX = 'http://identifiers.org/kegg.pathway/'
REACTOME_PREFIX = 'http://identifiers.org/reactome/'
WIKIPATHWAYS_PREFIX = 'http://identifiers.org/wikipathways/'
COMPATH_PREFIX = 'http://compath.scai.fraunhofer.de/rdfs#'

kegg = Namespace(KEGG_PREFIX)
reactome = Namespace(REACTOME_PREFIX)
wikipathways = Namespace(WIKIPATHWAYS_PREFIX)
compath = Namespace(COMPATH_PREFIX)
