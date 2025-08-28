import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import CONF_ICON, CONF_ID

from .. import CONF_JK_RS485_BMS_ID, JK_RS485_BMS_COMPONENT_SCHEMA, jk_rs485_bms_ns
from ..const import (
    CONF_BALANCING, CONF_PRECHARGING, CONF_CHARGING, CONF_DISCHARGING, CONF_DISPLAY_ALWAYS_ON, CONF_EMERGENCY, CONF_HEATING, CONF_CHARGING_FLOAT_MODE, 
    CONF_SMART_SLEEP_ON, CONF_DISABLE_PCL_MODULE, CONF_DISABLE_TEMPERATURE_SENSORS, CONF_TIMED_STORED_DATA,
    CONF_GPS_HEARTBEAT, CONF_PORT_SELECTION, CONF_SPECIAL_CHARGER
)

DEPENDENCIES = ["jk_rs485_bms"]
CODEOWNERS = ["@syssi","@txubelaxu"]

ICON_CHARGING = "mdi:battery-charging-50"
ICON_DISCHARGING = "mdi:battery-charging-50"
ICON_BALANCING = "mdi:seesaw"
ICON_EMERGENCY = "mdi:exit-run"
ICON_HEATING = "mdi:radiator"
ICON_DISABLE_TEMPERATURE_SENSORS = "mdi:thermometer-off"
ICON_SMART_SLEEP_ON = "mdi:sleep"
ICON_TIMED_STORED_DATA = "mdi:calendar-clock"
ICON_DISABLE_PCL_MODULE = "mdi:power-plug-off"
ICON_CHARGING_FLOAT_MODE = "mdi:battery-charging-80"
ICON_DISPLAY_ALWAYS_ON = "mdi:television"

SWITCHES = {
    CONF_CHARGING:                            [0x0070,0x10,0x04],
    CONF_DISCHARGING:                         [0x0074,0x10,0x04],
    CONF_BALANCING:                           [0x0078,0x10,0x04],
    CONF_HEATING:                             [0x0014,0x11,0x02],
    CONF_DISABLE_TEMPERATURE_SENSORS:         [0x0014,0x11,0x02],
    CONF_GPS_HEARTBEAT:                       [0x0014,0x11,0x02],
    CONF_PORT_SELECTION:                      [0x0014,0x11,0x02],
    CONF_DISPLAY_ALWAYS_ON:                   [0x0014,0x11,0x02],
    CONF_SPECIAL_CHARGER:                     [0x0014,0x11,0x02],
    CONF_SMART_SLEEP_ON:                      [0x0014,0x11,0x02],
    CONF_DISABLE_PCL_MODULE:                  [0x0014,0x11,0x02],
    CONF_TIMED_STORED_DATA:                   [0x0014,0x11,0x02],
    CONF_CHARGING_FLOAT_MODE:                 [0x0014,0x11,0x02],
    CONF_PRECHARGING:                         [0x0000,0x00,0x00],
    CONF_EMERGENCY:                           [0x0000,0x00,0x00],
}

JkRS485BmsSwitch = jk_rs485_bms_ns.class_("JkRS485BmsSwitch", switch.Switch, cg.Component)

CONFIG_SCHEMA = JK_RS485_BMS_COMPONENT_SCHEMA.extend(
    {
        cv.Optional(CONF_PRECHARGING): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_CHARGING,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_CHARGING): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_CHARGING,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_DISCHARGING): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_DISCHARGING,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_BALANCING): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_BALANCING,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_EMERGENCY): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_EMERGENCY,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_HEATING): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_HEATING,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_DISABLE_TEMPERATURE_SENSORS): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_DISABLE_TEMPERATURE_SENSORS,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_DISPLAY_ALWAYS_ON): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_DISPLAY_ALWAYS_ON,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_SMART_SLEEP_ON): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_SMART_SLEEP_ON,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_TIMED_STORED_DATA): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_TIMED_STORED_DATA,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_CHARGING_FLOAT_MODE): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_CHARGING_FLOAT_MODE,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_DISABLE_PCL_MODULE): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_DISABLE_PCL_MODULE,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_GPS_HEARTBEAT): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_DISABLE_PCL_MODULE,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_PORT_SELECTION): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_DISABLE_PCL_MODULE,
        ).extend(cv.COMPONENT_SCHEMA),
        cv.Optional(CONF_SPECIAL_CHARGER): switch.switch_schema(
            JkRS485BmsSwitch,
            icon=ICON_DISABLE_PCL_MODULE,
        ).extend(cv.COMPONENT_SCHEMA),
    }
)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_JK_RS485_BMS_ID])
    for key, param_config in SWITCHES.items():
        if key in config:
            conf = config[key]
            var = cg.new_Pvariable(conf[CONF_ID])
            await cg.register_component(var, conf)
            await switch.register_switch(var, conf)
            cg.add(getattr(hub, f"set_{key}_switch")(var))
            cg.add(var.set_parent(hub))
            cg.add(var.set_register_address(param_config[0]))
            cg.add(var.set_third_element_of_frame(param_config[1]))
            cg.add(var.set_data_length(param_config[2]))