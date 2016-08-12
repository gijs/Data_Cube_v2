# ------------------------------------------------------------------------------
# Name:       median_t_expression.py
# Purpose:    median t reduction example for Analytics Engine & Execution Engine.
#             post-integration with NDExpr.
#             post-integration with Data Access API.
#
# Author:     Peter Wang
#
# Created:    22 December 2015
# Copyright:  2015 Commonwealth Scientific and Industrial Research Organisation
#             (CSIRO)
# License:    This software is open source under the Apache v2.0 License
#             as provided in the accompanying LICENSE file or available from
#             https://github.com/data-cube/agdc-v2/blob/master/LICENSE
#             By continuing, you acknowledge that you have read and you accept
#             and will abide by the terms of the License.
#
# ------------------------------------------------------------------------------

from __future__ import absolute_import
from __future__ import print_function

# pylint: disable=too-many-locals

# temporary fix to pass Travis CI
# pylint: disable=wrong-import-order, import-error


from pprint import pprint
from datetime import datetime
from datacube.analytics.analytics_engine import AnalyticsEngine
from datacube.execution.execution_engine import ExecutionEngine
from datacube.analytics.utils.analytics_utils import plot

from glue.core import Data, DataCollection
from glue.app.qt.application import GlueApplication


def main():
    a = AnalyticsEngine()
    e = ExecutionEngine()

    # Lake Burley Griffin
    dimensions = {'x':    {'range': (149.07, 149.18)},
                  'y':    {'range': (-35.32, -35.28)},
                  'time': {'range': (datetime(1990, 1, 1), datetime(1990, 12, 31))}}

    arrays = a.create_array(('LANDSAT_5', 'nbar'), ['nir'], dimensions, 'get_data')

    median = a.apply_expression(arrays, 'median(array1, 0)', 'medianT')

    e.execute_plan(a.plan)

    plot(e.cache['medianT'])

    b40_result = e.cache['get_data']['array_result']['nir']
    median_result = e.cache['medianT']['array_result']['medianT']

    b40_data = Data(x=b40_result[:, ::-1, :], label='B40')
    median_data = Data(x=median_result[::-1, :], label='medianT')

    long_data = Data(x=b40_result.coords['x'], label='long')
    lat_data = Data(x=b40_result.coords['y'], label='lat')
    time_data = Data(x=b40_result.coords['time'], label='time')

    collection = DataCollection([median_data, b40_data, long_data, lat_data, time_data, ])
    app = GlueApplication(collection)
    app.start()


if __name__ == '__main__':
    main()
