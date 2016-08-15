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


class AodhProperties(object):
    ALARM_ID = 'alarm_id'
    DESCRIPTION = 'description'
    ENABLED = 'enabled'
    EVENT = 'event'
    EVENT_TYPE = 'event_type'
    EVENT_RESOURCE_ID = 'traits.resource_id'
    NAME = 'name'
    STATE = 'state'
    PROJECT_ID = 'project_id'
    QUERY = 'query'
    REPEAT_ACTIONS = 'repeat_actions'
    RESOURCE_ID = 'resource_id'
    SEVERITY = 'severity'
    STATE_TIMESTAMP = 'state_timestamp'
    THRESHOLD = 'threshold'
    TIMESTAMP = 'timestamp'
    TYPE = 'type'
    VITRAGE_ID = 'vitrage_id'


class AodhState(object):
    OK = 'ok'
    ALARM = 'alarm'
    INSUFFICIENT_DATA = 'insufficient_data'
