# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .work_item_tracking_resource import WorkItemTrackingResource


class FieldDependentRule(WorkItemTrackingResource):
    """FieldDependentRule.

    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <work-item-tracking.models.ReferenceLinks>`
    :param dependent_fields:
    :type dependent_fields: list of :class:`WorkItemFieldReference <work-item-tracking.models.WorkItemFieldReference>`
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dependent_fields': {'key': 'dependentFields', 'type': '[WorkItemFieldReference]'}
    }

    def __init__(self, url=None, _links=None, dependent_fields=None):
        super(FieldDependentRule, self).__init__(url=url, _links=_links)
        self.dependent_fields = dependent_fields