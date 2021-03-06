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

from oslo_log import log as logging
from oslo_utils import importutils

from vitrage.common.constants import NotifierEventTypes
from vitrage.common.constants import VertexProperties as VProps
from vitrage.notifier.plugins.base import NotifierBase

LOG = logging.getLogger(__name__)


class SnmpNotifier(NotifierBase):
    @staticmethod
    def get_notifier_name():
        return 'snmp'

    def __init__(self, conf):
        super(SnmpNotifier, self).__init__(conf)
        self.snmp_sender = \
            importutils.import_object(conf.snmp.snmp_sender_class, conf)

    def process_event(self, data, event_type):

        if event_type == NotifierEventTypes.ACTIVATE_DEDUCED_ALARM_EVENT \
                or event_type == \
                NotifierEventTypes.DEACTIVATE_DEDUCED_ALARM_EVENT:

            LOG.info('Vitrage snmp Info: Sending snmp trap')

            try:
                self.snmp_sender.send_snmp(self._parse_alarm_data(data))
            except Exception as e:
                LOG.exception('Vitrage snmp Error: '
                              'Failed to send SNMP trap: %s', e)
                return

    @staticmethod
    def _parse_alarm_data(data):

        new_data_format = {}

        for key, val in data.items():
            new_data_format[key] = val
            if key == VProps.RESOURCE:
                for k, v in val.items():
                    new_data_format[VProps.RESOURCE + '_' + str(k)] = v

        return new_data_format
