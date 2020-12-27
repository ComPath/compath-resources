# -*- coding: utf-8 -*-

"""Curation utilities."""

import itertools as itt
import logging
import os
from difflib import SequenceMatcher
from typing import Mapping, Tuple

import click
import pandas as pd
from tqdm import tqdm

from bio2bel.compath import get_compath_manager_classes
from compath_resources.constants import COMPATH_HOME

logger = logging.getLogger(__name__)


def make_similarity_matrices(
    minimum_gene_set_similarity: float = 0.8,
    minimum_string_similarity: float = 0.00,
) -> Mapping[Tuple[str, str], pd.DataFrame]:
    """Make similarity matricies.

    :param minimum_gene_set_similarity:
    :param minimum_string_similarity:
    """
    database = {}
    mappings = {}
    for name, manager_cls in get_compath_manager_classes().items():
        logger.info('loading %s', name)
        manager = manager_cls()
        if not manager.is_populated():
            logger.warning('not populated %s', name)
            continue
        logger.info('getting pathways from %s', name)
        database[name] = manager.get_pathway_id_to_symbols()
        mappings[name] = manager.get_pathway_id_name_mapping()

    rv = {}
    for (a_database_name, a_sets), (b_database_name, b_sets) in itt.combinations(database.items(), r=2):
        logger.info('calculating similarities between %s and %s', a_database_name, b_database_name)
        a_pathway_id_to_name, b_pathway_id_to_name = mappings[a_database_name], mappings[b_database_name]

        rows = []
        it = itt.product(a_sets.items(), b_sets.items())
        it = tqdm(it, total=len(a_sets) * len(b_sets))
        for (a_pathway_id, a_set), (b_pathway_id, b_set) in it:
            gene_similarity = calculate_jaccard(a_set, b_set)
            if gene_similarity < minimum_gene_set_similarity:
                continue

            a_pathway_name = a_pathway_id_to_name[a_pathway_id]
            b_pathway_name = b_pathway_id_to_name[b_pathway_id]

            sequence_matcher = SequenceMatcher(None, a_pathway_name, b_pathway_name)
            string_similarity = sequence_matcher.ratio()
            if string_similarity < minimum_string_similarity:
                continue

            rows.append((
                a_pathway_id, a_pathway_name,
                b_pathway_id, b_pathway_name,
                round(gene_similarity, 3), round(string_similarity, 3),
            ))

        rv[a_database_name, b_database_name] = df = pd.DataFrame(
            rows,
            columns=[f'{a_database_name}_id', f'{a_database_name}_name', f'{b_database_name}_id',
                     f'{b_database_name}_name', 'gene_set_similarity', 'string_similarity'],
        ).sort_values([f'{a_database_name}_name', 'gene_set_similarity'], ascending=False)

        path = os.path.join(COMPATH_HOME, f'{a_database_name}_{b_database_name}.tsv')
        df.to_csv(path, sep='\t', index=False)

    return rv


def calculate_jaccard(set_1, set_2) -> float:
    """Calculate the jaccard similarity between two sets.

    :param set set_1: set 1
    :param set set_2: set 2
    """
    intersection = len(set_1.intersection(set_2))
    smaller_set = min(len(set_1), len(set_2))

    return intersection / smaller_set


@click.command()
def _main():
    make_similarity_matrices()


if __name__ == '__main__':
    _main()
