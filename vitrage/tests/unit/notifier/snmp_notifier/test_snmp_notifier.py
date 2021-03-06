# Copyright 2017 - Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from vitrage.common.constants import VertexProperties as VProps
from vitrage.graph import Vertex
from vitrage.notifier.plugins.snmp.snmp_notifier import SnmpNotifier
from vitrage.tests import base
from vitrage.tests.unit.notifier.snmp_notifier import common


class SnmpNotifierTest(base.BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.resource_props = {VProps.IS_DELETED: common.false_,
                              VProps.IS_PLACEHOLDER: common.false_}
        cls.props = {VProps.IS_DELETED: common.false_,
                     VProps.NAME: common.name_,
                     VProps.RESOURCE: cls.resource_props,
                     VProps.CATEGORY: common.category_,
                     VProps.OPERATIONAL_SEVERITY: common.critical_}
        cls.alarm_vertex = Vertex('RESOURCE:nova.instance:test1', cls.props)

    def test_parse_alarm(self):
        alarm_data = SnmpNotifier._parse_alarm_data(self.alarm_vertex)

        self.assert_is_not_empty(alarm_data)

        self.assertEqual(alarm_data.get(VProps.IS_DELETED), common.false_)
        self.assertEqual(alarm_data.get(VProps.NAME), common.name_)
        self.assertEqual(alarm_data.get(VProps.CATEGORY), common.category_)
        self.assertEqual(alarm_data.get(VProps.OPERATIONAL_SEVERITY),
                         common.critical_)

        self.assertEqual(alarm_data.get(VProps.RESOURCE + '_' +
                                        VProps.IS_DELETED), common.false_)
        self.assertEqual(alarm_data.get(VProps.RESOURCE + '_' +
                                        VProps.IS_PLACEHOLDER), common.false_)
