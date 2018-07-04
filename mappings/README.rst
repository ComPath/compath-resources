Mapping Between Pathway Databases
---------------------------------

Three mapping files are stored in this package, one for each pairwise comparison:

- `KEGG - WikiPathways <https://github.com/ComPath/curation/blob/master/mappings/kegg_wikipathways.xlsx>`_
- `KEGG - Reactome <https://github.com/ComPath/curation/blob/master/mappings/kegg_reactome.xlsx>`_
- `WikiPathways - Reactome <https://github.com/ComPath/curation/blob/master/mappings/wikipathways_reactome.xlsx>`_

Additionally, all the canonical mappings can be downloaded in the ComPath deployed version (http://compath.scai.fraunhofer.de/export_mappings)
and in `RDF <https://github.com/ComPath/curation/blob/master/mappings/comapth_mappings.rdf>`_

*It is important to mention that even more mappings are stored in the database thanks to the ComPath inference system. For example, when a KEGG ot WikiPathways pathway is assigned as equivalent to a Reactome pathway, ComPath uses the Reactome hierarchy to infer new hierarchical mappings and map the super/sub pathways of the Reactome pathway to this corresponding equivalent pathway.*
