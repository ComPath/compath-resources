# -*- coding: utf-8 -*-

"""Generate charts for the ComPath GitHub Pages site."""

import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from more_click import verbose_option

from compath_resources import get_df
from compath_resources.constants import DATA_DIRECTORY, IMG_DIRECTORY

__all__ = [
    'charts',
]


@click.command()
@verbose_option
def charts():
    """Generate the summary for ComPath."""
    sns.set_theme(style="darkgrid")
    df = get_df(include_reactome_hierarchy=False, include_decopath=True, include_special=True)
    df.to_csv(DATA_DIRECTORY.joinpath('compath.tsv'), sep='\t', index=False)

    prefix_df = pd.concat([df['source_prefix'], df['target_prefix']]).to_frame()
    prefix_df.columns = ['Prefix']

    fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=True)
    sns.countplot(data=prefix_df, x='Prefix', ax=axes[0])
    sns.countplot(data=df, x='relation', ax=axes[1])
    axes[0].set_xlabel('')
    axes[0].set_title('By Prefix')
    axes[1].set_xlabel('')
    axes[1].set_title('By Type')
    axes[1].set_ylabel('')
    plt.suptitle(f'Summary of {len(df.index)} ComPath Mappings')
    plt.tight_layout()
    plt.savefig(IMG_DIRECTORY / 'prefixes.svg')
    plt.savefig(IMG_DIRECTORY / 'prefixes.png', dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    charts()
