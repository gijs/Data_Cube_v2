# Copyright 2016 United States Government as represented by the Administrator 
# of the National Aeronautics and Space Administration. All Rights Reserved.
#
# Portion of this code is Copyright Geoscience Australia, Licensed under the 
# Apache License, Version 2.0 (the "License"); you may not use this file 
# except in compliance with the License. You may obtain a copy of the License 
# at
#
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# The CEOS 2 platform is licensed under the Apache License, Version 2.0 (the 
# "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at 
# http://www.apache.org/licenses/LICENSE-2.0. 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
# License for the specific language governing permissions and limitations 
# under the License.

# Unit test dependencies
from django.test import TestCase

# Other dependencies
from django.core.urlresolvers import reverse
from django.core import management
from django.test.client import Client
from ..forms import DataSelectForm, GeospatialForm
from ..models import ResultType, SatelliteBand
from datetime import datetime

class TestForms(TestCase):

    # Used to show for diffs greater than certain characters.
    maxDiff = None
    
    def setUp(self):
        management.call_command('loaddata', 'db_backups/data_dump.json', verbosity=0)
        self.client.login(username='localuser', password='amadev12')

    def test_data_select_form(self):

        results = ResultType.objects.all()
        results_value = []
        for result in results:
            results_value.append((result.result_id,result.result_type))

        bands = SatelliteBand.objects.all()
        bands_value = []
        for band in bands:
            bands_value.append((band.id, band.band_name))

        form_data = {'result_type': 'true_color', 'band_selection': [1,2,3], 'title': 'a title', 'description': 'some description'}
        form = DataSelectForm(result_list = results_value, band_list = bands_value, data = form_data)

        self.assertTrue(form.is_valid())

    def test_geospacial_form(self):
        form_data = {'latitude_min': 0.0, 'latitude_max': 1.0, 'longitude_min': 34.0, 'longitude_max': 35.0, 'time_start': '01/01/2015', 'time_end': '01/01/2016'}
        form = GeospatialForm(data = form_data)

        self.assertTrue(form.is_valid())
