ComPath Resources
=================
|tests| |pypi_version| |python_versions| |pypi_license| |zenodo|

This repository contains the different resources derived or generated using `ComPath <https://github.com/ComPath>`_.
Among these resources, there are `Jupyter notebooks <https://github.com/ComPath/compath-resources/tree/master/notebooks>`_
outlining possible analyses that can be made using ComPath plugins as well as the results of the curation effort
(see the `mappings <https://github.com/ComPath/compath-resources/tree/master/mappings>`_ folder) where pathway mappings between
three of the major pathway databases (see below) are stored. As of March 2020, `PathBank <https://pathbank.org/>`_
mappings are now available in ComPath.

Citation
--------
If you use ComPath in your work, please consider citing:

.. [1] Domingo-Fernández, D., *et al.* (2018). `ComPath: An ecosystem for exploring, analyzing, and curating mappings across pathway databases <https://doi.org/10.1038/s41540-018-0078-8>`_. *npj Syst Biol Appl.*, 4(1):43.

Installation
------------
Easiest
~~~~~~~
Download the latest stable code from `PyPI <https://pypi.python.org/pypi/compath_resources>`_ with:

.. code-block:: python

   python3 -m pip install compath_resources

Get the Latest
~~~~~~~~~~~~~~~
Download the most recent code from `GitHub <https://github.com/ComPath/compath-resources>`_ with:

.. code-block:: python

   python3 -m pip install git+https://github.com/ComPath/compath-resources.git@master
    
Curation (Pathway Mappings)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The aim of this exercise was to generate mapping files across pathway databases in order to establish relationships
between similar pathways in three of the major pathway databases:

- `KEGG <http://www.kegg.jp/>`_
- `Reactome <http://reactome.org/>`_
- `WikiPathways <https://www.wikipathways.org/index.php/WikiPathways>`_

*We recommend to download the mappings directly from the ComPath website since the pathways in WikiPathways are not
stable and might have been changed. However, the mapping file distributed by the website contains stable identifiers
from all resources.*

Update: March 2020
~~~~~~~~~~~~~~~~~~
Mappings between `PathBank <https://pathbank.org/>`_ and the above-mentioned databases are now available in ComPath.

Mapping Between Pathway Databases
---------------------------------
A total of 6 mapping files are stored in this package, one for each pairwise comparison [*]_:

- `KEGG - WikiPathways <https://github.com/ComPath/compath-resources/blob/master/mappings/kegg_wikipathways.csv>`_
- `KEGG - Reactome <https://github.com/ComPath/compath-resources/blob/master/mappings/kegg_reactome.csv>`_
- `WikiPathways - Reactome <https://github.com/ComPath/compath-resources/blob/master/mappings/wikipathways_reactome.csv>`_
- `PathBank - KEGG <https://github.com/ComPath/compath-resources/blob/master/mappings/pathbank_kegg.csv>`_
- `PathBank - Reactome <https://github.com/ComPath/compath-resources/blob/master/mappings/pathbank_reactome.csv>`_
- `PathBank - WikiPathways <https://github.com/ComPath/compath-resources/blob/master/mappings/pathbank_wikipathways.csv>`_

.. [*] Pairwise mappings between KEGG, Reactome and WikiPathways were last updated in March of 2019. PathBank mappings
    were last updated in March of 2020.

Curation Team
-------------
The curation exercise was conducted under inter-curator agreement in a team formed by:

- Carlos Bobis-Álvarez
- `Josep Marín-Llaó <https://github.com/jmarinllao>`_
- `Daniel Domingo-Fernández <https://github.com/ddomingof>`_
- `Yojana Gadiya <https://github.com/YojanaGadiya>`_

Mapping Types
-------------
We have distinguished between two types of relationships between pathways (mappings): “equivalentTo” and “isPartOf”.

- equivalentTo. An undirected relationship denoting both pathways refer to the same biological process. The
  requirements for this relationship are:

  - Scope: both pathways represent the same biological pathway information.
  - Similarity: both pathways must share at minimum of one overlapping gene.
  - Context: both pathways should take place in the same context (e.g., cell line, physiology)

- isPartOf. A directed relationship denoting the hierarchical relationship between the pathway 1 (child) and 2
  (parent). The requirements are:

  - Subset: The subject (pathway 1) is a subset of pathway 2 (e.g., Reactome pathway hierarchy). 
  - Similarity: same as above
  - Context: same as above
  
.. |python_versions| image:: https://img.shields.io/pypi/pyversions/compath_resources.svg
    :alt: Stable Supported Python Versions
.. |pypi_version| image:: https://img.shields.io/pypi/v/compath_resources.svg
    :target: https://pypi.python.org/pypi/compath_resources
    :alt: Current version on PyPI
.. |pypi_license| image:: https://img.shields.io/pypi/l/compath_resources.svg
    :alt: MIT License
.. |zenodo| image:: https://zenodo.org/badge/132792765.svg
   :target: https://zenodo.org/badge/latestdoi/132792765
.. |tests| image:: https://github.com/ComPath/compath-resources/workflows/Tests/badge.svg
   :target: https://github.com/ComPath/compath-resources/actions?query=workflow%3ATests
