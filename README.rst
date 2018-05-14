ComPath Resources
=================
This repository contains the different resources that complement with `ComPath <https://github.com/ComPath>`_.
Among these resources, there are `Jupyter notebooks <https://github.com/ComPath/resources/tree/master/notebooks>`_ as well as the results of the curation effort `('mappings' folder) <https://github.com/ComPath/resources/tree/master/mappings>`_
where we curated pathway knowledge in order to establish mappings between pathways from different databases.

Curation (Pathway Mappings)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The aim of this exercise was to generate mapping files across pathway databases in order to establish relationships between similar pathways in three of the major pathway databases:

- `KEGG <http://www.kegg.jp/>`_
- `Reactome <http://reactome.org/>`_
- `WikiPathways <https://www.wikipathways.org/index.php/WikiPathways>`_

*We recommend to download the mappings directly from the ComPath website since WikiPathways names are not stable and might have been changed. However, the mapping file that can be retrieved from the website contains stable identifiers from all resources.*

Mapping Between Pathway Databases
---------------------------------

A total of 3 mapping files are stored in this package, one for each pairwise comparison:

- `KEGG - WikiPathways <https://github.com/ComPath/curation/blob/master/mappings/kegg_wikipathways.xlsx>`_
- `KEGG - Reactome <https://github.com/ComPath/curation/blob/master/mappings/kegg_reactome.xlsx>`_
- `WikiPathways - Reactome <https://github.com/ComPath/curation/blob/master/mappings/wikipathways_reactome.xlsx>`_

*It is important to mention that even more mappings are stored in the database thanks to the ComPath inference system. For example, when a KEGG/WikiPathways pathway is assigned as equivalent to a Reactome pathway, ComPath uses the Reactome hierarchy to infer new hierarchical mappings and map the super/sub pathways of the Reactome pathway to its corresponding KEGG/WikiPathways pathway.*

Curation team
-------------

The curation exercise was conducted under inter-curator agreement in a team formed by:

- Carlos Bobis-Álvarez
- Josep Marín-Llaó
- `Daniel Domingo-Fernández <https://github.com/ddomingof>`_

Mapping types
-------------
We have distinguished between two types of relationships between pathways (mappings): “equivalentTo” and “isPartOf”.

- equivalentTo. Both pathways refer to the same biological process. The requirements for this relationship are:

  - The pair must share at least a certain degree of similarity. In other words, only pathways with at least 1 overlapping gene can be mapped with this relationship.

  - Equal scope and context.

- isPartOf. This type of mapping represents a hierarchical relationship between the pathway 1 (child) and 2 (parent). Meaning that pathway 1 is a subset of pathway 2 (e.g., Reactome pathway hierarchy).
