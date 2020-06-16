# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import logging
from superdesk import get_resource_service


logger = logging.getLogger(__name__)


def translate_to_desk_language(item, **kwargs):
    """ This macro will set the language of the articles to the Desk language. """

    dest_desk = kwargs.get('desk')
    item_source = item.get('source')

    if dest_desk and item_source:
        if item_source == 'THE CANADIAN PRESS':
            return
        elif dest_desk.get('desk_language') == 'fr-CA':
            item['language'] = 'fr-CA'
        elif dest_desk.get('desk_language') == 'en-CA' and item.get('language') != 'fr-CA':
            item['language'] = 'en-CA'
    elif kwargs['desk'].get('desk_language') == 'fr-CA':
        item['language'] = 'fr-CA'


name = 'Translate To Desk Language'
label = name
callback = translate_to_desk_language
access_type = 'frontend'
action_type = 'direct'