#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2021 Christian Kreidl

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

#<<<owsensors>>>
# name sensor_type temperature unit [ relhumid unit dewpoint unit abshumid unit]
#AC-unit-intake 28 23.6 °C
#Room-Rack1-445 26 23.6 °C 26 %RH 2.9 °C 5.5 g/m³
#Room-Rack1-542 26 23.3 °C 27 %RH 3.0 °C 5.6 g/m³


from typing import (
    Any,
    Callable,
    Dict,
    Mapping,
    Optional,
    TypedDict,
    Tuple,
)
from .agent_based_api.v1 import (
    get_value_store,
#    check_levels,
    register,
#    render,
    type_defs,
    Metric,
#    Result,
    Service,
#    ServiceLabel,
#    State,
)
#import datetime

from .utils.humidity import check_humidity
from .utils.temperature import check_temperature, TempParamDict

Sensor  = Dict[str, float]
Section = Dict[str, Sensor]

def parse_owsensors(string_table: type_defs.StringTable) -> Section:
   result: Section = {}

   for line in string_table:
      sname = line[0]
      sensor_type = line[1]

      # DS18B20 Tempsensor
      if sensor_type == "28":
         result.setdefault("temp", {})[sname] = float(line[2])

      # DS2438 battery monitor aka Multisensor
      if sensor_type == "26":
         result.setdefault("temp", {})[sname]      = float(line[2])
         result.setdefault("humid", {})[sname]     = float(line[4])
         result.setdefault("dew", {})[sname]       = float(line[6])
         result.setdefault("humidabs", {})[sname]  = float(line[8])
   return result


def discover_owsensors_sensors_temp(section) -> type_defs.DiscoveryResult:
    for sensorname in section.get('temp', {}).keys():
        yield Service(item=sensorname)

def discover_owsensors_sensors_humid(section) -> type_defs.DiscoveryResult:
    for sensorname in section.get('humid', {}).keys():
        yield Service(item=sensorname)


def check_owsensors_temperature(
    item: str, params: TempParamDict, section: Section
) -> type_defs.CheckResult:
    if item in section.get('temp', {}):
        yield from check_temperature(
            section['temp'][item],
            params,
            unique_name="owsensors_temp_%s" % item,
            value_store=get_value_store(),
        )


def check_owsensors_humidity(
    item: str, params: Mapping[str, Any], section: Section
) -> type_defs.CheckResult:
    if item in section.get('humid', {}):
         yield Metric("dewpoint", section['dew'][item])
         yield Metric("humidity_abs", section['humidabs'][item])
         yield Metric("temperature", section['temp'][item])
         yield from check_humidity(section['humid'][item], params)



register.agent_section(
    name="owsensors",
    parse_function=parse_owsensors,
)

register.check_plugin(
    name="owsensors_temp",
    sections=["owsensors"],
    service_name="Temperature %s",
    discovery_function=discover_owsensors_sensors_temp,
    check_function=check_owsensors_temperature,
    check_ruleset_name="temperature",
    check_default_parameters={},
)

register.check_plugin(
    name="owsensors_humid",
    sections=["owsensors"],
    service_name="Humidity %s",
    discovery_function=discover_owsensors_sensors_humid,
    check_function=check_owsensors_humidity,
    check_ruleset_name="humidity",
    check_default_parameters={},
)
