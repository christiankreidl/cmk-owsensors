# -*- coding: utf-8 -*-
from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import (
    metric_info,
    graph_info,
)

unit_info["g/m3"] = {
    "title"     : _(u"g/m³"),
    "symbol"    : _(u"g/m³"),
    "render"    : lambda v: physical_precision(v, 2, _(u"g/m³")),
}

metric_info["humidity_abs"] = {
    "title" : "Absolute humidity",
    "unit"  : "g/m3",
    "color" : "#0000ff",
}

metric_info["dewpoint"] = {
    "title" : "Dewpoint",
    "unit"  : "c",
    "color" : "#ff3a3a",
}

metric_info["temperature"] = {
    "title" : _("Temperature"),
    "unit"  : "c",
    "color" : "16/a"
}

graph_info["check_mk-owsensors.humid"] = {
    "title" : "Humidity (relative)",
    "metrics" : [
        ( "humidity", "line"),
    ],
    "scalars": [
        "humidity:warn",
        "humidity:crit",
    ],
    "legend_precision" : 1,
    "range": (0, 100),
}

graph_info["check_mk-owsensors.humidabs"] = {
    "title" : "Humidity (absolute)",
    "metrics" : [
        ( "humidity_abs", "line"),
    ],
    "legend_precision" : 1,
    "range": (0, 50),
}

graph_info["check_mk-owsensors.dewpoint"] = {
    "title" : "Dewpoint",
    "metrics" : [
        ( "dewpoint", "line"),
    ],
    "legend_precision" : 1,
    "range": (0, 30),
}

graph_info["check_mk-owsensors.temperature"] = {
    "title" : "Temperature of humidity sensor",
    "metrics" : [
        ( "temperature", "line"),
    ],
    "legend_precision" : 1,
    "range": (0, 60),
}

