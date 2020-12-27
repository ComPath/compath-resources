# -*- coding: utf-8 -*-

"""Plot pathway size statistics."""

import logging
from typing import Iterable, Mapping, Tuple

import click
import matplotlib.pyplot as plt
import seaborn as sns
from more_click import verbose_option

from bio2bel.compath import CompathManager, get_compath_manager_classes
from compath_resources.constants import COMPATH_HOME

logger = logging.getLogger(__name__)


@click.command()
@verbose_option
def main():
    """Plot pathway size statistics."""
    x = list(_iter())

    fig, axes = plt.subplots(len(x), figsize=(10, 6))

    for ax, (manager, pathway_id_to_size, maximum) in zip(axes.ravel(), x):
        _plot(ax, manager.module_name, maximum, pathway_id_to_size)

    path = COMPATH_HOME / 'size_statistics.png'
    plt.savefig(path, dpi=300)


def _iter(cutoff: int = 2000) -> Iterable[Tuple[CompathManager, Mapping[str, int], int]]:
    for name, manager_cls in get_compath_manager_classes().items():
        logger.info('loading %s', name)
        manager = manager_cls()

        if not manager.is_populated():
            # manager.populate()
            logger.warning('skipping unpopulated manager for %s', name)
            continue

        logger.info('getting pathway size distribution for %s', name)
        pathway_id_to_size = manager.get_pathway_size_distribution()
        pathway_id_to_size = {
            k: v
            for k, v in pathway_id_to_size.items()
            if v < cutoff
        }
        yield manager, pathway_id_to_size, max(pathway_id_to_size.values())


def _plot(ax, title, upper, distribution):
    ax.set_title(f'Distribution {title} pathways size', fontsize=18)
    ax.set_xlabel('Size', fontsize=18)
    ax.set_ylabel('Frequency', fontsize=18)
    ax.set_xlim(0, upper)

    values = list(distribution.values())
    sns.distplot(values, bins=20, hist=False, ax=ax)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
