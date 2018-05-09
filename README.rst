ComPath Curation
================
This repository contains the curation efforts made with `ComPath <https://github.com/ComPath>`_. The aim is to generate mapping files across pathway databases in order to establish
relationships between similar pathways in three of the major pathway databases:

- `KEGG <http://www.kegg.jp/>`_
- `Reactome <http://reactome.org/>`_
- `WikiPathways <https://www.wikipathways.org/index.php/WikiPathways>`_

Mapping Between Pathway Databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A total of 3 mapping files are stored in this package, one for each pairwise comparison:

- `KEGG - WikiPathways <https://github.com/ComPath/curation/blob/master/mappings/kegg_wikipathways.xlsx>`_
- `KEGG - Reactome <https://github.com/ComPath/curation/blob/master/mappings/kegg_reactome.xlsx>`_
- `WikiPathways - Reactome <https://github.com/ComPath/curation/blob/master/mappings/wikipathways_reactome.xlsx>`_

Inter-curator agreement
-----------------------

The curation team was formed by:

- Carlos Bobis-Álvarez
- Josep Marín-Llaó
- `Daniel Domingo-Fernández <https://github.com/ddomingof>`_

Mapping types
-------------
We have distinguished between two types of mappings: equivalentTo and isPartOf:

- equivalentTo. Reflects that the pathway pair shares a high similarity. The guidelines for this mapping are:

  - The pair should share at least a certain degree of similarity (this is required). In other words, only pathways with at least 1 overlapping gene can be used for the mapping.

  - Same focus and biological function. A high concordance in the name between the pair is not required but it is helpful to identify this similarity. Curators have read the descriptions for each database to assess whether the focus of the pathway is the same or not.

- isPartOf. This type of mapping represents a hierarchical relationship between the pathway 1 (child) and 2 (parent). An example of this type of mappings can be found in the Reactome hierarchy.
