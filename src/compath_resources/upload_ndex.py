# -*- coding: utf-8 -*-

"""Upload the ComPath Mappings to NDEx.

.. seealso:: http://public.ndexbio.org/v2/network/551a8489-5a65-11eb-9e72-0ac135e8bacf
"""

import click
import pystow
from tqdm import tqdm

from biomappings.utils import MiriamValidator

from compath_resources import get_df
from compath_resources.utils import get_git_hash

COMPATH_NDEX_UUID = '551a8489-5a65-11eb-9e72-0ac135e8bacf'


@click.command()
@click.option('--username')
@click.option('--password')
def ndex(username, password):
    """Upload to NDEx."""
    try:
        from ndex2 import NiceCXBuilder
    except ImportError:
        click.secho('Need to `pip install ndex2` before uploading to NDEx', fg='red')
        return

    miriam_validator = MiriamValidator()

    cx = NiceCXBuilder()
    cx.set_name('ComPath')
    cx.add_network_attribute('description', 'Manually curated mappings between pathways.')
    cx.add_network_attribute('reference', 'https://github.com/compath/compath-resources')
    cx.add_network_attribute('rights', 'Waiver-No rights reserved (CC0)')

    context = {'orcid': 'https://identifiers.org/orcid:'}
    mappings = get_df(include_special=True, include_decopath=True, include_reactome_hierarchy=True)
    for _, mapping in mappings.iterrows():
        for prefix in (mapping['Source Resource'], mapping['Target Resource']):
            if prefix in {'decopath', 'pathbank'}:
                continue
            if miriam_validator.namespace_embedded(prefix):
                prefix = prefix.upper()
            context[prefix] = f'https://identifiers.org/{prefix}:'
    cx.set_context(context)

    cx.add_network_attribute('version', get_git_hash())
    cx.add_network_attribute('author', [
        'Daniel Domingo-Fernández',
        'Carlos Bobis-Álvarez',
        'Josep Marín-Llaó',
        'Yojana Gadiya',
        'Sarah Mubeen',
        'Charles Tapley Hoyt',
    ], type='list_of_string')

    for _, mapping in tqdm(mappings.iterrows(), desc='Loading NiceCXBuilder'):
        source = cx.add_node(
            represents=mapping['Source Name'],
            name=f'{mapping["Source Resource"]}:{mapping["Source ID"]}',
        )
        target = cx.add_node(
            represents=mapping['Target Name'],
            name=f'{mapping["Target Resource"]}:{mapping["Target ID"]}',
        )
        cx.add_edge(
            source=source,
            target=target,
            interaction=mapping['Mapping Type'],
        )

    nice_cx = cx.get_nice_cx()
    nice_cx.update_to(
        uuid=COMPATH_NDEX_UUID,
        server=pystow.get_config('ndex', 'server', 'http://public.ndexbio.org'),
        username=pystow.get_config('ndex', 'username', username),
        password=pystow.get_config('ndex', 'password', password),
    )


if __name__ == '__main__':
    ndex()
