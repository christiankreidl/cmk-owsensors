#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2025 Christian Kreidl

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.graphing.v1 import metrics, perfometers, graphs, Title
from cmk.plugins.collection.graphing.temperature import UNIT_DEGREE_CELSIUS

UNIT_DENSITY = metrics.Unit(metrics.DecimalNotation("g/m³"), metrics.StrictPrecision(2))

metric_owsensors_humidity_absolute = metrics.Metric(
    name="humidity_abs",
    title=Title("Absolute humidity"),
    unit=UNIT_DENSITY,
    color=metrics.Color.GREEN,
)

metric_owsensors_dewpoint = metrics.Metric(
    name="dewpoint",
    title=Title("Dewpoint"),
    unit=UNIT_DEGREE_CELSIUS,
    color=metrics.Color.BLUE,
)

graph_owsensors_humidity_abs = graphs.Graph(
    name="owsensors_humidity_abs",
    title=Title("Humidity (absolute)"),
    simple_lines=[
        "humidity_abs",
    ],
    minimal_range=graphs.MinimalRange(
        0,
        50,
    ),
)

graph_owsensors_dewpoint = graphs.Graph(
    name="owsensors_dewpoint",
    title=Title("Dewpoint"),
    simple_lines=[
        "dewpoint",
    ],
    minimal_range=graphs.MinimalRange(
        0,
        30,
    ),
)

