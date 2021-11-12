# -*- coding: utf-8 -*-

from cmk.gui.plugins.views.perfometers.check_mk import (
    perfometer_fanspeed,
    perfometer_temperature_multi,
    perfometer_voltage,
    perfometer_humidity,
)

perfometers['check_mk-owsensors.humid'] = perfometer_humidity
