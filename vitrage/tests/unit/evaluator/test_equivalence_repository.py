# Copyright 2017 - ZTE Corporation
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

import os

from vitrage.common.exception import VitrageError
from vitrage.evaluator.equivalence_repository import EquivalenceRepository
from vitrage.tests import base
from vitrage.tests.mocks import utils


class TestEquivalenceRepository(base.BaseTest):

    # noinspection PyPep8Naming
    def setUp(self):
        super(TestEquivalenceRepository, self).setUp()
        self.equivalence_repository = EquivalenceRepository()

    def test_duplicate_entities_in_equivalence(self):
        base_dir = utils.get_resources_dir() + '/templates/equivalences_dup'
        for directory in os.listdir(base_dir):
            self.assertRaises(VitrageError,
                              self.equivalence_repository.load_files,
                              os.path.join(base_dir, directory))
