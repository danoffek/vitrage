# Copyright 2016 - Alcatel-Lucent
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from vitrage.common.constants import DatasourceProperties as DSProps
from vitrage.common.constants import EntityCategory
from vitrage.common.constants import GraphAction
from vitrage.common.constants import VertexProperties as VProps
from vitrage.datasources.neutron.network import NEUTRON_NETWORK_DATASOURCE
from vitrage.datasources.resource_transformer_base import \
    ResourceTransformerBase
from vitrage.datasources import transformer_base as tbase
from vitrage.datasources.transformer_base import extract_field_value
import vitrage.graph.utils as graph_utils


class NetworkTransformer(ResourceTransformerBase):

    UPDATE_ID_PROPERTY = {
        'network.create.end': ('network', 'id'),
        'network.update.end': ('network', 'id'),
        'network.delete.end': ('network_id',),
        None: ('id',)
    }

    # graph actions which need to refer them differently
    GRAPH_ACTION_MAPPING = {
        'network.delete.end': GraphAction.DELETE_ENTITY,
    }

    def __init__(self, transformers, conf):
        super(NetworkTransformer, self).__init__(transformers, conf)

    def _create_snapshot_entity_vertex(self, entity_event):

        name = entity_event['name']
        entity_id = entity_event['id']
        state = entity_event['status']
        update_timestamp = entity_event['updated_at']
        project_id = entity_event.get('tenant_id', None)

        return self._create_vertex(entity_event,
                                   name,
                                   entity_id,
                                   state,
                                   update_timestamp,
                                   project_id)

    def _create_update_entity_vertex(self, entity_event):

        event_type = entity_event[DSProps.EVENT_TYPE]
        name = extract_field_value(entity_event, 'network', 'name')
        state = extract_field_value(entity_event, 'network', 'status')
        update_timestamp = \
            extract_field_value(entity_event, 'network', 'updated_at')
        entity_id = extract_field_value(entity_event,
                                        *self.UPDATE_ID_PROPERTY[event_type])
        project_id = extract_field_value(entity_event, 'network', 'tenant_id')

        return self._create_vertex(entity_event,
                                   name,
                                   entity_id,
                                   state,
                                   update_timestamp,
                                   project_id)

    def _create_vertex(self,
                       entity_event,
                       name,
                       entity_id,
                       state,
                       update_timestamp,
                       project_id):

        metadata = {
            VProps.NAME: name,
            VProps.PROJECT_ID: project_id,
        }

        sample_timestamp = entity_event[DSProps.SAMPLE_DATE]

        return graph_utils.create_vertex(
            self._create_entity_key(entity_event),
            entity_id=entity_id,
            entity_category=EntityCategory.RESOURCE,
            entity_type=NEUTRON_NETWORK_DATASOURCE,
            entity_state=state,
            sample_timestamp=sample_timestamp,
            update_timestamp=update_timestamp,
            metadata=metadata)

    def _create_entity_key(self, entity_event):
        event_type = entity_event.get(DSProps.EVENT_TYPE, None)
        network_id = extract_field_value(entity_event,
                                         *self.UPDATE_ID_PROPERTY[event_type])

        key_fields = self._key_values(NEUTRON_NETWORK_DATASOURCE, network_id)
        return tbase.build_key(key_fields)

    def get_type(self):
        return NEUTRON_NETWORK_DATASOURCE
