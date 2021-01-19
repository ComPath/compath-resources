# -*- coding: utf-8 -*-

"""Generate charts for the ComPath GitHub Pages site."""

import click
import matplotlib.pyplot as plt
import pandas as pd
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
    df = get_df(include_reactome_hierarchy=False, include_decopath=True, include_special=True)
    prefix_df = pd.concat([df['Source Resource'], df['Target Resource']]).to_frame()
    prefix_df.columns = ['Prefix']

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    sns.countplot(data=prefix_df, x='Prefix', ax=axes[0])
    sns.countplot(data=df, x='Mapping Type', ax=axes[1])
    axes[1].set_ylabel('')
    plt.suptitle(f'Breakdown of {len(df.index)} ComPath Mappings')
    plt.tight_layout()
    plt.savefig(IMG_DIRECTORY / 'prefixes.png', dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    charts()
