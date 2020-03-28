import logging
from collections import defaultdict
from typing import Mapping, Tuple

import itertools as itt
import pandas as pd
from tqdm import tqdm

from bio2bel.compath import get_compath_manager_classes

logger = logging.getLogger(__name__)


def make_similarity_matricies() -> Mapping[Tuple[str, str], pd.DataFrame]:
    database = {}
    for name, manager_cls in get_compath_manager_classes().items():
        logger.info('loading %s', name)
        manager = manager_cls()
        logger.info('getting pathways from %s', name)
        database[name] = manager.get_pathway_dicts()

    rv = {}
    for (a_name, a_sets), (b_name, b_sets) in itt.combinations(database.items(), r=2):
        logger.info('calculating similarities between %s and %s', a_name, b_name)
        data = defaultdict(dict)
        it = itt.product(a_sets.items(), b_sets.items())
        it = tqdm(it, total=len(a_sets) * len(b_sets))
        for (a_pathway, a_set), (b_pathway, b_set) in it:
            data[a_pathway][b_pathway] = calculate_jaccard(a_set, b_set)
        rv[a_name, b_name] = pd.DataFrame.from_dict(data)

    return rv


def calculate_jaccard(set_1, set_2):
    """calculates jaccard similarity between two sets

    :param set set_1: set 1
    :param set set_2: set 2
    :returns similarity
    :rtype: float
    """
    intersection = len(set_1.intersection(set_2))
    smaller_set = min(len(set_1), len(set_2))

    return intersection / smaller_set


if __name__ == '__main__':
    r = make_similarity_matricies()
    for (a,b), df in r.items():
        df.to_csv(f'/Users/cthoyt/Desktop/{a}_{b}.tsv', sep='\t', index=True)
