# Copyright 2015 - Alcatel-Lucent
# Copyright 2016 - Nokia
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


class VertexProperties(object):
    CATEGORY = 'category'
    TYPE = 'type'
    ID = 'id'
    IS_DELETED = 'is_deleted'
    STATE = 'state'
    VITRAGE_STATE = 'vitrage_state'
    AGGREGATED_STATE = 'aggregated_state'
    OPERATIONAL_STATE = 'operational_state'
    PROJECT_ID = 'project_id'
    UPDATE_TIMESTAMP = 'update_timestamp'
    SAMPLE_TIMESTAMP = 'sample_timestamp'
    NAME = 'name'
    IS_PLACEHOLDER = 'is_placeholder'
    SEVERITY = 'severity'
    AGGREGATED_SEVERITY = 'aggregated_severity'
    OPERATIONAL_SEVERITY = 'operational_severity'
    VITRAGE_ID = 'vitrage_id'
    IS_MARKED_DOWN = 'is_marked_down'
    INFO = 'info'
    GRAPH_INDEX = 'graph_index'
    RAWTEXT = 'rawtext'
    RESOURCE_ID = 'resource_id'
    RESOURCE = 'resource'
    IS_REAL_VITRAGE_ID = 'is_real_vitrage_id'


class EdgeProperties(object):
    RELATIONSHIP_TYPE = 'relationship_type'
    IS_DELETED = 'is_deleted'
    UPDATE_TIMESTAMP = 'update_timestamp'


class EdgeLabel(object):
    ON = 'on'
    CONTAINS = 'contains'
    CAUSES = 'causes'
    ATTACHED = 'attached'
    ATTACHED_PUBLIC = 'attached_public'
    ATTACHED_PRIVATE = 'attached_private'
    CONNECT = 'connect'
    MANAGED_BY = 'managed_by'
    COMPRISED = 'comprised'

    @staticmethod
    def labels():
        return [EdgeLabel.__dict__[label]
                for label in vars(EdgeLabel)
                if not label.startswith(('_', 'labels'))]


class DatasourceAction(object):
    SNAPSHOT = 'snapshot'
    INIT_SNAPSHOT = 'init_snapshot'
    UPDATE = 'update'


class UpdateMethod(object):
    NONE = 'none'
    PULL = 'pull'
    PUSH = 'push'


class EntityCategory(object):
    RESOURCE = 'RESOURCE'
    ALARM = 'ALARM'

    @staticmethod
    def categories():
        return [EntityCategory.__dict__[category]
                for category in vars(EntityCategory)
                if not category.startswith(('_', 'categories'))]


class DatasourceProperties(object):
    ENTITY_TYPE = 'vitrage_entity_type'
    DATASOURCE_ACTION = 'vitrage_datasource_action'
    SAMPLE_DATE = 'vitrage_sample_date'
    EVENT_TYPE = 'vitrage_event_type'


class GraphAction(object):
    CREATE_ENTITY = 'create_entity'
    DELETE_ENTITY = 'delete_entity'
    UPDATE_ENTITY = 'update_entity'
    DELETE_RELATIONSHIP = 'delete_relationship'
    UPDATE_RELATIONSHIP = 'update_relationship'
    REMOVE_DELETED_ENTITY = 'remove_deleted_entity'
    END_MESSAGE = 'end_message'


class NotifierEventTypes(object):
    ACTIVATE_DEDUCED_ALARM_EVENT = 'vitrage.deduced_alarm.activate'
    DEACTIVATE_DEDUCED_ALARM_EVENT = 'vitrage.deduced_alarm.deactivate'
    ACTIVATE_MARK_DOWN_EVENT = 'vitrage.mark_down.activate'
    DEACTIVATE_MARK_DOWN_EVENT = 'vitrage.mark_down.deactivate'


class TemplateTopologyFields(object):
    """yaml fields for topology definitions"""
    METADATA = 'metadata'
    DESCRIPTION = 'description'
    NAME = 'name'

    DEFINITIONS = 'definitions'

    ENTITIES = 'entities'
    ENTITY = 'entity'
    TYPE = 'type'
    ID = 'id'

    RELATIONSHIPS = 'relationships'
    RELATIONSHIP = 'relationship'
    RELATIONSHIP_TYPE = 'relationship_type'
    SOURCE = 'source'
    TARGET = 'target'


class EventProperties(object):
    TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    TYPE = 'type'
    TIME = 'time'
    DETAILS = 'details'


class DatasourceOpts(object):
    TRANSFORMER = 'transformer'
    DRIVER = 'driver'
    UPDATE_METHOD = 'update_method'
    CHANGES_INTERVAL = 'changes_interval'
    CONFIG_FILE = 'config_file'
