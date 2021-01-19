# -*- coding: utf-8 -*-

"""Generate charts for the ComPath GitHub Pages site."""

from collections import Counter

import click
import matplotlib.pyplot as plt
import seaborn as sns
from more_click import verbose_option

from compath_resources import get_df
from compath_resources.constants import IMG_DIRECTORY

__all__ = [
    'charts',
]


@click.command()
@verbose_option
def charts():
    """Generate the summary for ComPath."""
    sns.set_theme(style="darkgrid")
    df = get_df(include_reactome_hierarchy=False, include_decopath=True)
    counter = Counter()
    for source_prefix, _source_id, _source_name, _mapp, target_prefix, _target_id, _target_name in df.values:
        counter[source_prefix] += 1
        counter[target_prefix] += 1

    fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=True)
    sns.countplot(data=df, x='Source Resource', ax=axes[0])
    sns.countplot(data=df, x='Target Resource', ax=axes[1])
    axes[1].set_ylabel('')
    plt.tight_layout()
    plt.savefig(IMG_DIRECTORY / 'prefixes.png', dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    charts()
