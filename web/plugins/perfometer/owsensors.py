# -*- coding: utf-8 -*-

from cmk.gui.plugins.metrics import perfometer_info

perfometer_info.append({
    "type": "linear",
    "metric": ["humidity"],
    "total": 100.0,
})