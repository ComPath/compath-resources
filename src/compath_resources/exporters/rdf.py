# -*- coding: utf-8 -*-

"""Export ComPath resources as RDF."""

import rdflib
from rdflib import Namespace
from rdflib.namespace import RDFS

from ..parser import get_df

__all__ = [
    'get_rdf',
]

KEGG_PREFIX = 'http://identifiers.org/kegg.pathway/'
REACTOME_PREFIX = 'http://identifiers.org/reactome/'
WIKIPATHWAYS_PREFIX = 'http://identifiers.org/wikipathways/'
PATHBANK_PREFIX = 'http://identifiers.org/pathbank/'
COMPATH_PREFIX = 'http://compath.scai.fraunhofer.de/rdfs#'

KEGG_NAMESPACE = Namespace(KEGG_PREFIX)
REACTOME_NAMESPACE = Namespace(REACTOME_PREFIX)
PATHBANK_NAMESPACE = Namespace(PATHBANK_PREFIX)
WIKIPATHWAYS_NAMESPACE = Namespace(WIKIPATHWAYS_PREFIX)
compath = Namespace(COMPATH_PREFIX)

RELATIONS = {
    'partOf': compath['partOf'],
    'equivalentTo': compath['equivalentTo'],
}
NAMESPACES = {
    'kegg': KEGG_NAMESPACE,
    'reactome': REACTOME_NAMESPACE,
    'pathbank': PATHBANK_NAMESPACE,
    'wikipathways': WIKIPATHWAYS_NAMESPACE,
}


def get_rdf() -> rdflib.Graph:
    """Get an RDFLib graph."""
    graph = rdflib.Graph()

    graph.namespace_manager.bind('kegg', KEGG_NAMESPACE)
    graph.namespace_manager.bind('reactome', REACTOME_NAMESPACE)
    graph.namespace_manager.bind('wp', WIKIPATHWAYS_NAMESPACE)
    graph.namespace_manager.bind('pathbank', WIKIPATHWAYS_NAMESPACE)
    graph.namespace_manager.bind('compath', compath)

    df = get_df()
    for source_ns, source_id, source_name, relation, target_ns, target_id, target_name in df.values:
        h = NAMESPACES[source_ns][source_id]
        r = RELATIONS[relation]
        t = NAMESPACES[target_ns][target_id]

        graph.add((h, r, t))
        graph.add((h, RDFS.label, source_name))
        graph.add((t, RDFS.label, target_name))

    return graph
