"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n modules/canbus/proto/lexus.proto\x12\rapollo.canbus"\x8c\x02\n\x15Hazard_lights_rpt_214\x12\x14\n\x0coutput_value\x18\x01 \x01(\x08\x12\x17\n\x0fcommanded_value\x18\x02 \x01(\x08\x12\x14\n\x0cmanual_input\x18\x03 \x01(\x08\x12\x15\n\rvehicle_fault\x18\x04 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x05 \x01(\x08\x12\x17\n\x0foverride_active\x18\x06 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x07 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x08 \x01(\x08\x12\x0f\n\x07enabled\x18\t \x01(\x08\x12\x1c\n\x14command_output_fault\x18\n \x01(\x08"\x93\x01\n\x10Steering_cmd_12c\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12\x10\n\x08position\x18\x05 \x01(\x01\x12\x15\n\rrotation_rate\x18\x06 \x01(\x01"\x9f\t\n\x1bDash_controls_right_rpt_210\x12Q\n\x0coutput_value\x18\x01 \x01(\x0e2;.apollo.canbus.Dash_controls_right_rpt_210.Output_valueType\x12W\n\x0fcommanded_value\x18\x02 \x01(\x0e2>.apollo.canbus.Dash_controls_right_rpt_210.Commanded_valueType\x12\x15\n\rvehicle_fault\x18\x03 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x04 \x01(\x08\x12\x17\n\x0foverride_active\x18\x05 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x06 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x07 \x01(\x08\x12\x0f\n\x07enabled\x18\x08 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\t \x01(\x08\x12Q\n\x0cmanual_input\x18\n \x01(\x0e2;.apollo.canbus.Dash_controls_right_rpt_210.Manual_inputType"\xe7\x01\n\x10Output_valueType\x12"\n\x1eOUTPUT_VALUE_DASH_CONTROL_NONE\x10\x00\x12 \n\x1cOUTPUT_VALUE_DASH_CONTROL_OK\x10\x01\x12"\n\x1eOUTPUT_VALUE_DASH_CONTROL_LEFT\x10\x02\x12#\n\x1fOUTPUT_VALUE_DASH_CONTROL_RIGHT\x10\x03\x12 \n\x1cOUTPUT_VALUE_DASH_CONTROL_UP\x10\x04\x12"\n\x1eOUTPUT_VALUE_DASH_CONTROL_DOWN\x10\x05"\xfc\x01\n\x13Commanded_valueType\x12%\n!COMMANDED_VALUE_DASH_CONTROL_NONE\x10\x00\x12#\n\x1fCOMMANDED_VALUE_DASH_CONTROL_OK\x10\x01\x12%\n!COMMANDED_VALUE_DASH_CONTROL_LEFT\x10\x02\x12&\n"COMMANDED_VALUE_DASH_CONTROL_RIGHT\x10\x03\x12#\n\x1fCOMMANDED_VALUE_DASH_CONTROL_UP\x10\x04\x12%\n!COMMANDED_VALUE_DASH_CONTROL_DOWN\x10\x05"\xe7\x01\n\x10Manual_inputType\x12"\n\x1eMANUAL_INPUT_DASH_CONTROL_NONE\x10\x00\x12 \n\x1cMANUAL_INPUT_DASH_CONTROL_OK\x10\x01\x12"\n\x1eMANUAL_INPUT_DASH_CONTROL_LEFT\x10\x02\x12#\n\x1fMANUAL_INPUT_DASH_CONTROL_RIGHT\x10\x03\x12 \n\x1cMANUAL_INPUT_DASH_CONTROL_UP\x10\x04\x12"\n\x1eMANUAL_INPUT_DASH_CONTROL_DOWN\x10\x05"\xf8\x03\n\x1aDash_controls_left_cmd_10c\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12`\n\x14dash_controls_button\x18\x05 \x01(\x0e2B.apollo.canbus.Dash_controls_left_cmd_10c.Dash_controls_buttonType"\x9f\x02\n\x18Dash_controls_buttonType\x12*\n&DASH_CONTROLS_BUTTON_DASH_CONTROL_NONE\x10\x00\x12(\n$DASH_CONTROLS_BUTTON_DASH_CONTROL_OK\x10\x01\x12*\n&DASH_CONTROLS_BUTTON_DASH_CONTROL_LEFT\x10\x02\x12+\n\'DASH_CONTROLS_BUTTON_DASH_CONTROL_RIGHT\x10\x03\x12(\n$DASH_CONTROLS_BUTTON_DASH_CONTROL_UP\x10\x04\x12*\n&DASH_CONTROLS_BUTTON_DASH_CONTROL_DOWN\x10\x05"\x87\x02\n\x10Steering_rpt_22c\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x17\n\x0foverride_active\x18\x03 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x04 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x05 \x01(\x08\x12\x0f\n\x07enabled\x18\x06 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x07 \x01(\x08\x12\x14\n\x0cmanual_input\x18\x08 \x01(\x01\x12\x17\n\x0fcommanded_value\x18\t \x01(\x01\x12\x14\n\x0coutput_value\x18\n \x01(\x01"\xa0\x01\n\x10Turn_aux_rpt_330\x12%\n\x1dpass_blinker_bulb_on_is_valid\x18\x01 \x01(\x08\x12\x1c\n\x14pass_blinker_bulb_on\x18\x02 \x01(\x08\x12\'\n\x1fdriver_blinker_bulb_on_is_valid\x18\x03 \x01(\x08\x12\x1e\n\x16driver_blinker_bulb_on\x18\x04 \x01(\x08"\xfa\x05\n\x11Headlight_rpt_218\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x17\n\x0foverride_active\x18\x03 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x04 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x05 \x01(\x08\x12\x0f\n\x07enabled\x18\x06 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x07 \x01(\x08\x12G\n\x0coutput_value\x18\x08 \x01(\x0e21.apollo.canbus.Headlight_rpt_218.Output_valueType\x12G\n\x0cmanual_input\x18\t \x01(\x0e21.apollo.canbus.Headlight_rpt_218.Manual_inputType\x12M\n\x0fcommanded_value\x18\n \x01(\x0e24.apollo.canbus.Headlight_rpt_218.Commanded_valueType"l\n\x10Output_valueType\x12\x1f\n\x1bOUTPUT_VALUE_HEADLIGHTS_OFF\x10\x00\x12\x1a\n\x16OUTPUT_VALUE_LOW_BEAMS\x10\x01\x12\x1b\n\x17OUTPUT_VALUE_HIGH_BEAMS\x10\x02"l\n\x10Manual_inputType\x12\x1f\n\x1bMANUAL_INPUT_HEADLIGHTS_OFF\x10\x00\x12\x1a\n\x16MANUAL_INPUT_LOW_BEAMS\x10\x01\x12\x1b\n\x17MANUAL_INPUT_HIGH_BEAMS\x10\x02"x\n\x13Commanded_valueType\x12"\n\x1eCOMMANDED_VALUE_HEADLIGHTS_OFF\x10\x00\x12\x1d\n\x19COMMANDED_VALUE_LOW_BEAMS\x10\x01\x12\x1e\n\x1aCOMMANDED_VALUE_HIGH_BEAMS\x10\x02"\x8a\x01\n\x15Hazard_lights_cmd_114\x12\x19\n\x11hazard_lights_cmd\x18\x01 \x01(\x08\x12\x18\n\x10ignore_overrides\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x0e\n\x06enable\x18\x04 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x05 \x01(\x08"\x9b\t\n\x1aDash_controls_left_rpt_20c\x12P\n\x0coutput_value\x18\x01 \x01(\x0e2:.apollo.canbus.Dash_controls_left_rpt_20c.Output_valueType\x12V\n\x0fcommanded_value\x18\x02 \x01(\x0e2=.apollo.canbus.Dash_controls_left_rpt_20c.Commanded_valueType\x12P\n\x0cmanual_input\x18\x03 \x01(\x0e2:.apollo.canbus.Dash_controls_left_rpt_20c.Manual_inputType\x12\x15\n\rvehicle_fault\x18\x04 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x05 \x01(\x08\x12\x17\n\x0foverride_active\x18\x06 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x07 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x08 \x01(\x08\x12\x0f\n\x07enabled\x18\t \x01(\x08\x12\x1c\n\x14command_output_fault\x18\n \x01(\x08"\xe7\x01\n\x10Output_valueType\x12"\n\x1eOUTPUT_VALUE_DASH_CONTROL_NONE\x10\x00\x12 \n\x1cOUTPUT_VALUE_DASH_CONTROL_OK\x10\x01\x12"\n\x1eOUTPUT_VALUE_DASH_CONTROL_LEFT\x10\x02\x12#\n\x1fOUTPUT_VALUE_DASH_CONTROL_RIGHT\x10\x03\x12 \n\x1cOUTPUT_VALUE_DASH_CONTROL_UP\x10\x04\x12"\n\x1eOUTPUT_VALUE_DASH_CONTROL_DOWN\x10\x05"\xfc\x01\n\x13Commanded_valueType\x12%\n!COMMANDED_VALUE_DASH_CONTROL_NONE\x10\x00\x12#\n\x1fCOMMANDED_VALUE_DASH_CONTROL_OK\x10\x01\x12%\n!COMMANDED_VALUE_DASH_CONTROL_LEFT\x10\x02\x12&\n"COMMANDED_VALUE_DASH_CONTROL_RIGHT\x10\x03\x12#\n\x1fCOMMANDED_VALUE_DASH_CONTROL_UP\x10\x04\x12%\n!COMMANDED_VALUE_DASH_CONTROL_DOWN\x10\x05"\xe7\x01\n\x10Manual_inputType\x12"\n\x1eMANUAL_INPUT_DASH_CONTROL_NONE\x10\x00\x12 \n\x1cMANUAL_INPUT_DASH_CONTROL_OK\x10\x01\x12"\n\x1eMANUAL_INPUT_DASH_CONTROL_LEFT\x10\x02\x12#\n\x1fMANUAL_INPUT_DASH_CONTROL_RIGHT\x10\x03\x12 \n\x1cMANUAL_INPUT_DASH_CONTROL_UP\x10\x04\x12"\n\x1eMANUAL_INPUT_DASH_CONTROL_DOWN\x10\x05"\x80\x04\n\x15Headlight_aux_rpt_318\x12 \n\x18headlights_mode_is_valid\x18\x01 \x01(\x08\x12Q\n\x0fheadlights_mode\x18\x02 \x01(\x0e28.apollo.canbus.Headlight_aux_rpt_318.Headlights_modeType\x12\x1e\n\x16fog_lights_on_is_valid\x18\x03 \x01(\x08\x12\x15\n\rfog_lights_on\x18\x04 \x01(\x08\x12%\n\x1dheadlights_on_bright_is_valid\x18\x05 \x01(\x08\x12\x1c\n\x14headlights_on_bright\x18\x06 \x01(\x08\x12\x1e\n\x16headlights_on_is_valid\x18\x07 \x01(\x08\x12\x15\n\rheadlights_on\x18\x08 \x01(\x08"\xbe\x01\n\x13Headlights_modeType\x12"\n\x1eHEADLIGHTS_MODE_HEADLIGHTS_OFF\x10\x00\x12\'\n#HEADLIGHTS_MODE_PARKING_LIGHTS_ONLY\x10\x01\x12-\n)HEADLIGHTS_MODE_HEADLIGHTS_ON_MANUAL_MODE\x10\x02\x12+\n\'HEADLIGHTS_MODE_HEADLIGHTS_ON_AUTO_MODE\x10\x03"\xfa\x03\n\x1bDash_controls_right_cmd_110\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12a\n\x14dash_controls_button\x18\x05 \x01(\x0e2C.apollo.canbus.Dash_controls_right_cmd_110.Dash_controls_buttonType"\x9f\x02\n\x18Dash_controls_buttonType\x12*\n&DASH_CONTROLS_BUTTON_DASH_CONTROL_NONE\x10\x00\x12(\n$DASH_CONTROLS_BUTTON_DASH_CONTROL_OK\x10\x01\x12*\n&DASH_CONTROLS_BUTTON_DASH_CONTROL_LEFT\x10\x02\x12+\n\'DASH_CONTROLS_BUTTON_DASH_CONTROL_RIGHT\x10\x03\x12(\n$DASH_CONTROLS_BUTTON_DASH_CONTROL_UP\x10\x04\x12*\n&DASH_CONTROLS_BUTTON_DASH_CONTROL_DOWN\x10\x05"\x8f\x03\n\rWiper_cmd_134\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12=\n\twiper_cmd\x18\x04 \x01(\x0e2*.apollo.canbus.Wiper_cmd_134.Wiper_cmdType\x12\x14\n\x0cclear_faults\x18\x05 \x01(\x08"\xe6\x01\n\rWiper_cmdType\x12\x18\n\x14WIPER_CMD_WIPERS_OFF\x10\x00\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_1\x10\x01\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_2\x10\x02\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_3\x10\x03\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_4\x10\x04\x12\x1c\n\x18WIPER_CMD_INTERMITTENT_5\x10\x05\x12\x11\n\rWIPER_CMD_LOW\x10\x06\x12\x12\n\x0eWIPER_CMD_HIGH\x10\x07"\xbb\t\n\rWiper_rpt_234\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x17\n\x0foverride_active\x18\x03 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x04 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x05 \x01(\x08\x12\x0f\n\x07enabled\x18\x06 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x07 \x01(\x08\x12C\n\x0coutput_value\x18\x08 \x01(\x0e2-.apollo.canbus.Wiper_rpt_234.Output_valueType\x12I\n\x0fcommanded_value\x18\t \x01(\x0e20.apollo.canbus.Wiper_rpt_234.Commanded_valueType\x12C\n\x0cmanual_input\x18\n \x01(\x0e2-.apollo.canbus.Wiper_rpt_234.Manual_inputType"\x81\x02\n\x10Output_valueType\x12\x1b\n\x17OUTPUT_VALUE_WIPERS_OFF\x10\x00\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_1\x10\x01\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_2\x10\x02\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_3\x10\x03\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_4\x10\x04\x12\x1f\n\x1bOUTPUT_VALUE_INTERMITTENT_5\x10\x05\x12\x14\n\x10OUTPUT_VALUE_LOW\x10\x06\x12\x15\n\x11OUTPUT_VALUE_HIGH\x10\x07"\x9c\x02\n\x13Commanded_valueType\x12\x1e\n\x1aCOMMANDED_VALUE_WIPERS_OFF\x10\x00\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_1\x10\x01\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_2\x10\x02\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_3\x10\x03\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_4\x10\x04\x12"\n\x1eCOMMANDED_VALUE_INTERMITTENT_5\x10\x05\x12\x17\n\x13COMMANDED_VALUE_LOW\x10\x06\x12\x18\n\x14COMMANDED_VALUE_HIGH\x10\x07"\x81\x02\n\x10Manual_inputType\x12\x1b\n\x17MANUAL_INPUT_WIPERS_OFF\x10\x00\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_1\x10\x01\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_2\x10\x02\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_3\x10\x03\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_4\x10\x04\x12\x1f\n\x1bMANUAL_INPUT_INTERMITTENT_5\x10\x05\x12\x14\n\x10MANUAL_INPUT_LOW\x10\x06\x12\x15\n\x11MANUAL_INPUT_HIGH\x10\x07"\xf9\x05\n\x0cTurn_rpt_230\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x17\n\x0foverride_active\x18\x03 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x04 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x05 \x01(\x08\x12\x0f\n\x07enabled\x18\x06 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x07 \x01(\x08\x12B\n\x0cmanual_input\x18\x08 \x01(\x0e2,.apollo.canbus.Turn_rpt_230.Manual_inputType\x12H\n\x0fcommanded_value\x18\t \x01(\x0e2/.apollo.canbus.Turn_rpt_230.Commanded_valueType\x12B\n\x0coutput_value\x18\n \x01(\x0e2,.apollo.canbus.Turn_rpt_230.Output_valueType"q\n\x10Manual_inputType\x12\x16\n\x12MANUAL_INPUT_RIGHT\x10\x00\x12\x15\n\x11MANUAL_INPUT_NONE\x10\x01\x12\x15\n\x11MANUAL_INPUT_LEFT\x10\x02\x12\x17\n\x13MANUAL_INPUT_HAZARD\x10\x03"\x80\x01\n\x13Commanded_valueType\x12\x19\n\x15COMMANDED_VALUE_RIGHT\x10\x00\x12\x18\n\x14COMMANDED_VALUE_NONE\x10\x01\x12\x18\n\x14COMMANDED_VALUE_LEFT\x10\x02\x12\x1a\n\x16COMMANDED_VALUE_HAZARD\x10\x03"q\n\x10Output_valueType\x12\x16\n\x12OUTPUT_VALUE_RIGHT\x10\x00\x12\x15\n\x11OUTPUT_VALUE_NONE\x10\x01\x12\x15\n\x11OUTPUT_VALUE_LEFT\x10\x02\x12\x17\n\x13OUTPUT_VALUE_HAZARD\x10\x03"\xa8\x02\n\x11Headlight_cmd_118\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12I\n\rheadlight_cmd\x18\x05 \x01(\x0e22.apollo.canbus.Headlight_cmd_118.Headlight_cmdType"p\n\x11Headlight_cmdType\x12 \n\x1cHEADLIGHT_CMD_HEADLIGHTS_OFF\x10\x00\x12\x1b\n\x17HEADLIGHT_CMD_LOW_BEAMS\x10\x01\x12\x1c\n\x18HEADLIGHT_CMD_HIGH_BEAMS\x10\x02"\xa7\x03\n\x0cDoor_rpt_417\x12\x1f\n\x17fuel_door_open_is_valid\x18\x01 \x01(\x08\x12\x1b\n\x13trunk_open_is_valid\x18\x02 \x01(\x08\x12\x1a\n\x12hood_open_is_valid\x18\x03 \x01(\x08\x12$\n\x1crear_pass_door_open_is_valid\x18\x04 \x01(\x08\x12&\n\x1erear_driver_door_open_is_valid\x18\x05 \x01(\x08\x12\x1f\n\x17pass_door_open_is_valid\x18\x06 \x01(\x08\x12!\n\x19driver_door_open_is_valid\x18\x07 \x01(\x08\x12\x16\n\x0efuel_door_open\x18\x08 \x01(\x08\x12\x12\n\ntrunk_open\x18\t \x01(\x08\x12\x11\n\thood_open\x18\n \x01(\x08\x12\x1b\n\x13rear_pass_door_open\x18\x0b \x01(\x08\x12\x1d\n\x15rear_driver_door_open\x18\x0c \x01(\x08\x12\x16\n\x0epass_door_open\x18\r \x01(\x08\x12\x18\n\x10driver_door_open\x18\x0e \x01(\x08"\xef\x04\n\x10Component_rpt_20\x12J\n\x0ecomponent_type\x18\x01 \x01(\x0e22.apollo.canbus.Component_rpt_20.Component_typeType\x12J\n\x0ecomponent_func\x18\x02 \x01(\x0e22.apollo.canbus.Component_rpt_20.Component_funcType\x12\x0f\n\x07counter\x18\x03 \x01(\x05\x12\x12\n\ncomplement\x18\x04 \x01(\x05\x12\x14\n\x0cconfig_fault\x18\x05 \x01(\x08"h\n\x12Component_typeType\x12\x19\n\x15COMPONENT_TYPE_PACMOD\x10\x00\x12\x1a\n\x16COMPONENT_TYPE_PACMINI\x10\x01\x12\x1b\n\x17COMPONENT_TYPE_PACMICRO\x10\x02"\x9d\x02\n\x12Component_funcType\x12\x19\n\x15COMPONENT_FUNC_PACMOD\x10\x00\x12/\n+COMPONENT_FUNC_STEERING_AND_STEERING_COLUMN\x10\x01\x12*\n&COMPONENT_FUNC_ACCELERATOR_AND_BRAKING\x10\x02\x12\x1a\n\x16COMPONENT_FUNC_BRAKING\x10\x03\x12\x1b\n\x17COMPONENT_FUNC_SHIFTING\x10\x04\x12\x1b\n\x17COMPONENT_FUNC_STEERING\x10\x05\x12\x1c\n\x18COMPONENT_FUNC_E_SHIFTER\x10\x06\x12\x1b\n\x17COMPONENT_FUNC_WATCHDOG\x10\x07"\x8d\x01\n\x13Wheel_speed_rpt_407\x12\x1c\n\x14wheel_spd_rear_right\x18\x01 \x01(\x01\x12\x1b\n\x13wheel_spd_rear_left\x18\x02 \x01(\x01\x12\x1d\n\x15wheel_spd_front_right\x18\x03 \x01(\x01\x12\x1c\n\x14wheel_spd_front_left\x18\x04 \x01(\x01"G\n\x18Steering_motor_rpt_3_406\x12\x15\n\rtorque_output\x18\x01 \x01(\x01\x12\x14\n\x0ctorque_input\x18\x02 \x01(\x01"i\n\x18Steering_motor_rpt_2_405\x12\x1b\n\x13encoder_temperature\x18\x01 \x01(\x05\x12\x19\n\x11motor_temperature\x18\x02 \x01(\x05\x12\x15\n\rangular_speed\x18\x03 \x01(\x01"I\n\x18Steering_motor_rpt_1_404\x12\x15\n\rmotor_current\x18\x01 \x01(\x01\x12\x16\n\x0eshaft_position\x18\x02 \x01(\x01"D\n\x15Brake_motor_rpt_3_403\x12\x15\n\rtorque_output\x18\x01 \x01(\x01\x12\x14\n\x0ctorque_input\x18\x02 \x01(\x01"f\n\x15Brake_motor_rpt_2_402\x12\x1b\n\x13encoder_temperature\x18\x01 \x01(\x05\x12\x19\n\x11motor_temperature\x18\x02 \x01(\x05\x12\x15\n\rangular_speed\x18\x03 \x01(\x01"F\n\x15Brake_motor_rpt_1_401\x12\x15\n\rmotor_current\x18\x01 \x01(\x01\x12\x16\n\x0eshaft_position\x18\x02 \x01(\x01"\xdb\x02\n\x11Wiper_aux_rpt_334\x12\x1c\n\x14spray_empty_is_valid\x18\x01 \x01(\x08\x12\x13\n\x0bspray_empty\x18\x02 \x01(\x08\x12!\n\x19spray_near_empty_is_valid\x18\x03 \x01(\x08\x12\x18\n\x10spray_near_empty\x18\x04 \x01(\x08\x12\x1e\n\x16rear_spraying_is_valid\x18\x05 \x01(\x08\x12\x15\n\rrear_spraying\x18\x06 \x01(\x08\x12\x1c\n\x14rear_wiping_is_valid\x18\x07 \x01(\x08\x12\x13\n\x0brear_wiping\x18\x08 \x01(\x08\x12\x1f\n\x17front_spraying_is_valid\x18\t \x01(\x08\x12\x16\n\x0efront_spraying\x18\n \x01(\x08\x12\x1d\n\x15front_wiping_is_valid\x18\x0b \x01(\x08\x12\x14\n\x0cfront_wiping\x18\x0c \x01(\x08"\xa1\x02\n\x11Shift_aux_rpt_328\x12\'\n\x1fspeed_interlock_active_is_valid\x18\x01 \x01(\x08\x12\x1e\n\x16speed_interlock_active\x18\x02 \x01(\x08\x12\'\n\x1fbrake_interlock_active_is_valid\x18\x03 \x01(\x08\x12\x1e\n\x16brake_interlock_active\x18\x04 \x01(\x08\x12%\n\x1dstay_in_neutral_mode_is_valid\x18\x05 \x01(\x08\x12\x1c\n\x14stay_in_neutral_mode\x18\x06 \x01(\x08\x12\x1e\n\x16between_gears_is_valid\x18\x07 \x01(\x08\x12\x15\n\rbetween_gears\x18\x08 \x01(\x08"\x84\x02\n\rAccel_rpt_200\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x03 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x04 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x05 \x01(\x08\x12\x17\n\x0foverride_active\x18\x06 \x01(\x08\x12\x0f\n\x07enabled\x18\x07 \x01(\x08\x12\x14\n\x0cmanual_input\x18\x08 \x01(\x01\x12\x17\n\x0fcommanded_value\x18\t \x01(\x01\x12\x14\n\x0coutput_value\x18\n \x01(\x01"\x84\x02\n\rBrake_rpt_204\x12\x1c\n\x14command_output_fault\x18\x01 \x01(\x08\x12\x15\n\rvehicle_fault\x18\x02 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x03 \x01(\x08\x12\x17\n\x0foverride_active\x18\x04 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x05 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x06 \x01(\x08\x12\x0f\n\x07enabled\x18\x07 \x01(\x08\x12\x14\n\x0cmanual_input\x18\x08 \x01(\x01\x12\x17\n\x0fcommanded_value\x18\t \x01(\x01\x12\x14\n\x0coutput_value\x18\n \x01(\x01"\xd5\x01\n\x0cHorn_cmd_11c\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12:\n\x08horn_cmd\x18\x05 \x01(\x0e2(.apollo.canbus.Horn_cmd_11c.Horn_cmdType"1\n\x0cHorn_cmdType\x12\x10\n\x0cHORN_CMD_OFF\x10\x00\x12\x0f\n\x0bHORN_CMD_ON\x10\x01"\xc7\x06\n\rGlobal_rpt_10\x12\x1b\n\x13config_fault_active\x18\x01 \x01(\x08\x12 \n\x18pacmod_subsystem_timeout\x18\x02 \x01(\x08\x12U\n\x15pacmod_system_enabled\x18\x03 \x01(\x0e26.apollo.canbus.Global_rpt_10.Pacmod_system_enabledType\x12e\n\x1dpacmod_system_override_active\x18\x04 \x01(\x0e2>.apollo.canbus.Global_rpt_10.Pacmod_system_override_activeType\x12"\n\x1apacmod_system_fault_active\x18\x05 \x01(\x08\x12\x17\n\x0fveh_can_timeout\x18\x06 \x01(\x08\x12\x17\n\x0fstr_can_timeout\x18\x07 \x01(\x08\x12I\n\x0fbrk_can_timeout\x18\x08 \x01(\x0e20.apollo.canbus.Global_rpt_10.Brk_can_timeoutType\x12\x17\n\x0fusr_can_timeout\x18\t \x01(\x08\x12\x1b\n\x13usr_can_read_errors\x18\n \x01(\x05"r\n\x19Pacmod_system_enabledType\x12*\n&PACMOD_SYSTEM_ENABLED_CONTROL_DISABLED\x10\x00\x12)\n%PACMOD_SYSTEM_ENABLED_CONTROL_ENABLED\x10\x01"\x83\x01\n!Pacmod_system_override_activeType\x120\n,PACMOD_SYSTEM_OVERRIDE_ACTIVE_NOT_OVERRIDDEN\x10\x00\x12,\n(PACMOD_SYSTEM_OVERRIDE_ACTIVE_OVERRIDDEN\x10\x01"h\n\x13Brk_can_timeoutType\x12)\n%BRK_CAN_TIMEOUT_NO_ACTIVE_CAN_TIMEOUT\x10\x00\x12&\n"BRK_CAN_TIMEOUT_ACTIVE_CAN_TIMEOUT\x10\x01"\xc2\x01\n\x11Accel_aux_rpt_300\x12!\n\x19user_interaction_is_valid\x18\x01 \x01(\x08\x12\x18\n\x10user_interaction\x18\x02 \x01(\x08\x12 \n\x18raw_pedal_force_is_valid\x18\x03 \x01(\x08\x12\x17\n\x0fraw_pedal_force\x18\x04 \x01(\x01\x12\x1e\n\x16raw_pedal_pos_is_valid\x18\x05 \x01(\x08\x12\x15\n\rraw_pedal_pos\x18\x06 \x01(\x01"\x8c\x0b\n\x1eCruise_control_buttons_rpt_208\x12T\n\x0coutput_value\x18\x01 \x01(\x0e2>.apollo.canbus.Cruise_control_buttons_rpt_208.Output_valueType\x12T\n\x0cmanual_input\x18\x02 \x01(\x0e2>.apollo.canbus.Cruise_control_buttons_rpt_208.Manual_inputType\x12Z\n\x0fcommanded_value\x18\x03 \x01(\x0e2A.apollo.canbus.Cruise_control_buttons_rpt_208.Commanded_valueType\x12\x15\n\rvehicle_fault\x18\x04 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x05 \x01(\x08\x12\x17\n\x0foverride_active\x18\x06 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x07 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x08 \x01(\x08\x12\x0f\n\x07enabled\x18\t \x01(\x08\x12\x1c\n\x14command_output_fault\x18\n \x01(\x08"\xb1\x02\n\x10Output_valueType\x12$\n OUTPUT_VALUE_CRUISE_CONTROL_NONE\x10\x00\x12$\n OUTPUT_VALUE_CRUISE_CONTROL_CNCL\x10\x01\x12+\n\'OUTPUT_VALUE_CRUISE_CONTROL_ACC_FURTHER\x10\x02\x12*\n&OUTPUT_VALUE_CRUISE_CONTROL_ACC_CLOSER\x10\x03\x12\'\n#OUTPUT_VALUE_CRUISE_CONTROL_SET_DEC\x10\x04\x12\'\n#OUTPUT_VALUE_CRUISE_CONTROL_RES_INC\x10\x05\x12&\n"OUTPUT_VALUE_CRUISE_CONTROL_ON_OFF\x10\x06"\xb1\x02\n\x10Manual_inputType\x12$\n MANUAL_INPUT_CRUISE_CONTROL_NONE\x10\x00\x12$\n MANUAL_INPUT_CRUISE_CONTROL_CNCL\x10\x01\x12+\n\'MANUAL_INPUT_CRUISE_CONTROL_ACC_FURTHER\x10\x02\x12*\n&MANUAL_INPUT_CRUISE_CONTROL_ACC_CLOSER\x10\x03\x12\'\n#MANUAL_INPUT_CRUISE_CONTROL_SET_DEC\x10\x04\x12\'\n#MANUAL_INPUT_CRUISE_CONTROL_RES_INC\x10\x05\x12&\n"MANUAL_INPUT_CRUISE_CONTROL_ON_OFF\x10\x06"\xc9\x02\n\x13Commanded_valueType\x12\'\n#COMMANDED_VALUE_CRUISE_CONTROL_NONE\x10\x00\x12\'\n#COMMANDED_VALUE_CRUISE_CONTROL_CNCL\x10\x01\x12.\n*COMMANDED_VALUE_CRUISE_CONTROL_ACC_FURTHER\x10\x02\x12-\n)COMMANDED_VALUE_CRUISE_CONTROL_ACC_CLOSER\x10\x03\x12*\n&COMMANDED_VALUE_CRUISE_CONTROL_SET_DEC\x10\x04\x12*\n&COMMANDED_VALUE_CRUISE_CONTROL_RES_INC\x10\x05\x12)\n%COMMANDED_VALUE_CRUISE_CONTROL_ON_OFF\x10\x06"\xe4\x01\n\x15Vehicle_speed_rpt_400\x12\x15\n\rvehicle_speed\x18\x01 \x01(\x01\x12Y\n\x13vehicle_speed_valid\x18\x02 \x01(\x0e2<.apollo.canbus.Vehicle_speed_rpt_400.Vehicle_speed_validType"Y\n\x17Vehicle_speed_validType\x12\x1f\n\x1bVEHICLE_SPEED_VALID_INVALID\x10\x00\x12\x1d\n\x19VEHICLE_SPEED_VALID_VALID\x10\x01"\xb8\x02\n\x11Brake_aux_rpt_304\x12\x1d\n\x15brake_on_off_is_valid\x18\x01 \x01(\x08\x12\x14\n\x0cbrake_on_off\x18\x02 \x01(\x08\x12!\n\x19user_interaction_is_valid\x18\x03 \x01(\x08\x12\x18\n\x10user_interaction\x18\x04 \x01(\x08\x12#\n\x1braw_brake_pressure_is_valid\x18\x05 \x01(\x08\x12\x1a\n\x12raw_brake_pressure\x18\x06 \x01(\x01\x12 \n\x18raw_pedal_force_is_valid\x18\x07 \x01(\x08\x12\x17\n\x0fraw_pedal_force\x18\x08 \x01(\x01\x12\x1e\n\x16raw_pedal_pos_is_valid\x18\t \x01(\x08\x12\x15\n\rraw_pedal_pos\x18\n \x01(\x01"\xbc\x04\n\x16Media_controls_cmd_120\x12X\n\x12media_controls_cmd\x18\x01 \x01(\x0e2<.apollo.canbus.Media_controls_cmd_120.Media_controls_cmdType\x12\x18\n\x10ignore_overrides\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12\x0e\n\x06enable\x18\x05 \x01(\x08"\xef\x02\n\x16Media_controls_cmdType\x12)\n%MEDIA_CONTROLS_CMD_MEDIA_CONTROL_NONE\x10\x00\x122\n.MEDIA_CONTROLS_CMD_MEDIA_CONTROL_VOICE_COMMAND\x10\x01\x12)\n%MEDIA_CONTROLS_CMD_MEDIA_CONTROL_MUTE\x10\x02\x126\n2MEDIA_CONTROLS_CMD_MEDIA_CONTROL_PREV_TRACK_ANSWER\x10\x03\x127\n3MEDIA_CONTROLS_CMD_MEDIA_CONTROL_NEXT_TRACK_HANG_UP\x10\x04\x12+\n\'MEDIA_CONTROLS_CMD_MEDIA_CONTROL_VOL_UP\x10\x05\x12-\n)MEDIA_CONTROLS_CMD_MEDIA_CONTROL_VOL_DOWN\x10\x06"\xdc\x04\n\x1eCruise_control_buttons_cmd_108\x12f\n\x15cruise_control_button\x18\x01 \x01(\x0e2G.apollo.canbus.Cruise_control_buttons_cmd_108.Cruise_control_buttonType\x12\x18\n\x10ignore_overrides\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x0e\n\x06enable\x18\x04 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x05 \x01(\x08"\xf9\x02\n\x19Cruise_control_buttonType\x12-\n)CRUISE_CONTROL_BUTTON_CRUISE_CONTROL_NONE\x10\x00\x12-\n)CRUISE_CONTROL_BUTTON_CRUISE_CONTROL_CNCL\x10\x01\x124\n0CRUISE_CONTROL_BUTTON_CRUISE_CONTROL_ACC_FURTHER\x10\x02\x123\n/CRUISE_CONTROL_BUTTON_CRUISE_CONTROL_ACC_CLOSER\x10\x03\x120\n,CRUISE_CONTROL_BUTTON_CRUISE_CONTROL_SET_DEC\x10\x04\x120\n,CRUISE_CONTROL_BUTTON_CRUISE_CONTROL_RES_INC\x10\x05\x12/\n+CRUISE_CONTROL_BUTTON_CRUISE_CONTROL_ON_OFF\x10\x06"\x8a\x01\n\x15Parking_brake_cmd_124\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x19\n\x11parking_brake_cmd\x18\x04 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x05 \x01(\x08"\xd6\x04\n\x0cHorn_rpt_21c\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x17\n\x0foverride_active\x18\x03 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x04 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x05 \x01(\x08\x12\x0f\n\x07enabled\x18\x06 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x07 \x01(\x08\x12B\n\x0coutput_value\x18\x08 \x01(\x0e2,.apollo.canbus.Horn_rpt_21c.Output_valueType\x12H\n\x0fcommanded_value\x18\t \x01(\x0e2/.apollo.canbus.Horn_rpt_21c.Commanded_valueType\x12B\n\x0cmanual_input\x18\n \x01(\x0e2,.apollo.canbus.Horn_rpt_21c.Manual_inputType"=\n\x10Output_valueType\x12\x14\n\x10OUTPUT_VALUE_OFF\x10\x00\x12\x13\n\x0fOUTPUT_VALUE_ON\x10\x01"F\n\x13Commanded_valueType\x12\x17\n\x13COMMANDED_VALUE_OFF\x10\x00\x12\x16\n\x12COMMANDED_VALUE_ON\x10\x01"=\n\x10Manual_inputType\x12\x14\n\x10MANUAL_INPUT_OFF\x10\x00\x12\x13\n\x0fMANUAL_INPUT_ON\x10\x01"\x9d\x08\n\rShift_rpt_228\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x17\n\x0foverride_active\x18\x03 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x04 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x05 \x01(\x08\x12\x0f\n\x07enabled\x18\x06 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x07 \x01(\x08\x12C\n\x0cmanual_input\x18\x08 \x01(\x0e2-.apollo.canbus.Shift_rpt_228.Manual_inputType\x12I\n\x0fcommanded_value\x18\t \x01(\x0e20.apollo.canbus.Shift_rpt_228.Commanded_valueType\x12C\n\x0coutput_value\x18\n \x01(\x0e2-.apollo.canbus.Shift_rpt_228.Output_valueType"\xe1\x01\n\x10Manual_inputType\x12\x15\n\x11MANUAL_INPUT_PARK\x10\x00\x12\x18\n\x14MANUAL_INPUT_REVERSE\x10\x01\x12\x18\n\x14MANUAL_INPUT_NEUTRAL\x10\x02\x12\x1d\n\x19MANUAL_INPUT_FORWARD_HIGH\x10\x03\x12\x14\n\x10MANUAL_INPUT_LOW\x10\x04\x12\x1e\n\x1aMANUAL_INPUT_BETWEEN_GEARS\x10\x05\x12\x16\n\x12MANUAL_INPUT_ERROR\x10\x06\x12\x15\n\x11MANUAL_INPUT_NONE\x10\x07"\xbe\x01\n\x13Commanded_valueType\x12\x18\n\x14COMMANDED_VALUE_PARK\x10\x00\x12\x1b\n\x17COMMANDED_VALUE_REVERSE\x10\x01\x12\x1b\n\x17COMMANDED_VALUE_NEUTRAL\x10\x02\x12 \n\x1cCOMMANDED_VALUE_FORWARD_HIGH\x10\x03\x12\x17\n\x13COMMANDED_VALUE_LOW\x10\x04\x12\x18\n\x14COMMANDED_VALUE_NONE\x10\x07"\xe1\x01\n\x10Output_valueType\x12\x15\n\x11OUTPUT_VALUE_PARK\x10\x00\x12\x18\n\x14OUTPUT_VALUE_REVERSE\x10\x01\x12\x18\n\x14OUTPUT_VALUE_NEUTRAL\x10\x02\x12\x1d\n\x19OUTPUT_VALUE_FORWARD_HIGH\x10\x03\x12\x14\n\x10OUTPUT_VALUE_LOW\x10\x04\x12\x1e\n\x1aOUTPUT_VALUE_BETWEEN_GEARS\x10\x05\x12\x16\n\x12OUTPUT_VALUE_ERROR\x10\x06\x12\x15\n\x11OUTPUT_VALUE_NONE\x10\x07"\xbd\x02\n\rShift_cmd_128\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12=\n\tshift_cmd\x18\x05 \x01(\x0e2*.apollo.canbus.Shift_cmd_128.Shift_cmdType"\x94\x01\n\rShift_cmdType\x12\x12\n\x0eSHIFT_CMD_PARK\x10\x00\x12\x15\n\x11SHIFT_CMD_REVERSE\x10\x01\x12\x15\n\x11SHIFT_CMD_NEUTRAL\x10\x02\x12\x1a\n\x16SHIFT_CMD_FORWARD_HIGH\x10\x03\x12\x11\n\rSHIFT_CMD_LOW\x10\x04\x12\x12\n\x0eSHIFT_CMD_NONE\x10\x07"z\n\rAccel_cmd_100\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12\x11\n\taccel_cmd\x18\x05 \x01(\x01"\x8c\x02\n\x15Parking_brake_rpt_224\x12\x15\n\rvehicle_fault\x18\x01 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x02 \x01(\x08\x12\x17\n\x0foverride_active\x18\x03 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x04 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x05 \x01(\x08\x12\x0f\n\x07enabled\x18\x06 \x01(\x08\x12\x1c\n\x14command_output_fault\x18\x07 \x01(\x08\x12\x14\n\x0coutput_value\x18\x08 \x01(\x08\x12\x17\n\x0fcommanded_value\x18\t \x01(\x08\x12\x14\n\x0cmanual_input\x18\n \x01(\x08"z\n\rBrake_cmd_104\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12\x11\n\tbrake_cmd\x18\x05 \x01(\x01"\x96\x0b\n\x16Media_controls_rpt_220\x12L\n\x0coutput_value\x18\x01 \x01(\x0e26.apollo.canbus.Media_controls_rpt_220.Output_valueType\x12R\n\x0fcommanded_value\x18\x02 \x01(\x0e29.apollo.canbus.Media_controls_rpt_220.Commanded_valueType\x12L\n\x0cmanual_input\x18\x03 \x01(\x0e26.apollo.canbus.Media_controls_rpt_220.Manual_inputType\x12\x15\n\rvehicle_fault\x18\x04 \x01(\x08\x12\x14\n\x0cpacmod_fault\x18\x05 \x01(\x08\x12\x17\n\x0foverride_active\x18\x06 \x01(\x08\x12\x1d\n\x15output_reported_fault\x18\x07 \x01(\x08\x12\x1a\n\x12input_output_fault\x18\x08 \x01(\x08\x12\x0f\n\x07enabled\x18\t \x01(\x08\x12\x1c\n\x14command_output_fault\x18\n \x01(\x08"\xbf\x02\n\x10Output_valueType\x12#\n\x1fOUTPUT_VALUE_MEDIA_CONTROL_NONE\x10\x00\x12,\n(OUTPUT_VALUE_MEDIA_CONTROL_VOICE_COMMAND\x10\x01\x12#\n\x1fOUTPUT_VALUE_MEDIA_CONTROL_MUTE\x10\x02\x120\n,OUTPUT_VALUE_MEDIA_CONTROL_PREV_TRACK_ANSWER\x10\x03\x121\n-OUTPUT_VALUE_MEDIA_CONTROL_NEXT_TRACK_HANG_UP\x10\x04\x12%\n!OUTPUT_VALUE_MEDIA_CONTROL_VOL_UP\x10\x05\x12\'\n#OUTPUT_VALUE_MEDIA_CONTROL_VOL_DOWN\x10\x06"\xd7\x02\n\x13Commanded_valueType\x12&\n"COMMANDED_VALUE_MEDIA_CONTROL_NONE\x10\x00\x12/\n+COMMANDED_VALUE_MEDIA_CONTROL_VOICE_COMMAND\x10\x01\x12&\n"COMMANDED_VALUE_MEDIA_CONTROL_MUTE\x10\x02\x123\n/COMMANDED_VALUE_MEDIA_CONTROL_PREV_TRACK_ANSWER\x10\x03\x124\n0COMMANDED_VALUE_MEDIA_CONTROL_NEXT_TRACK_HANG_UP\x10\x04\x12(\n$COMMANDED_VALUE_MEDIA_CONTROL_VOL_UP\x10\x05\x12*\n&COMMANDED_VALUE_MEDIA_CONTROL_VOL_DOWN\x10\x06"\xbf\x02\n\x10Manual_inputType\x12#\n\x1fMANUAL_INPUT_MEDIA_CONTROL_NONE\x10\x00\x12,\n(MANUAL_INPUT_MEDIA_CONTROL_VOICE_COMMAND\x10\x01\x12#\n\x1fMANUAL_INPUT_MEDIA_CONTROL_MUTE\x10\x02\x120\n,MANUAL_INPUT_MEDIA_CONTROL_PREV_TRACK_ANSWER\x10\x03\x121\n-MANUAL_INPUT_MEDIA_CONTROL_NEXT_TRACK_HANG_UP\x10\x04\x12%\n!MANUAL_INPUT_MEDIA_CONTROL_VOL_UP\x10\x05\x12\'\n#MANUAL_INPUT_MEDIA_CONTROL_VOL_DOWN\x10\x06"\xf0\x01\n\x14Steering_aux_rpt_32c\x12!\n\x19user_interaction_is_valid\x18\x01 \x01(\x08\x12\x18\n\x10user_interaction\x18\x02 \x01(\x08\x12\x1e\n\x16rotation_rate_is_valid\x18\x03 \x01(\x08\x12\x15\n\rrotation_rate\x18\x04 \x01(\x01\x12\x1b\n\x13raw_torque_is_valid\x18\x05 \x01(\x08\x12\x12\n\nraw_torque\x18\x06 \x01(\x01\x12\x1d\n\x15raw_position_is_valid\x18\x07 \x01(\x08\x12\x14\n\x0craw_position\x18\x08 \x01(\x01"\xc9\x01\n\x17Lat_lon_heading_rpt_40e\x12\x0f\n\x07heading\x18\x01 \x01(\x01\x12\x19\n\x11longitude_seconds\x18\x02 \x01(\x05\x12\x19\n\x11longitude_minutes\x18\x03 \x01(\x05\x12\x19\n\x11longitude_degrees\x18\x04 \x01(\x05\x12\x18\n\x10latitude_seconds\x18\x05 \x01(\x05\x12\x18\n\x10latitude_minutes\x18\x06 \x01(\x05\x12\x18\n\x10latitude_degrees\x18\x07 \x01(\x05"$\n\x10Yaw_rate_rpt_40d\x12\x10\n\x08yaw_rate\x18\x01 \x01(\x01"\x89\x01\n\x11Date_time_rpt_40f\x12\x13\n\x0btime_second\x18\x01 \x01(\x05\x12\x13\n\x0btime_minute\x18\x02 \x01(\x05\x12\x11\n\ttime_hour\x18\x03 \x01(\x05\x12\x10\n\x08date_day\x18\x04 \x01(\x05\x12\x12\n\ndate_month\x18\x05 \x01(\x05\x12\x11\n\tdate_year\x18\x06 \x01(\x05"L\n\x0bVin_rpt_414\x12\x12\n\nveh_serial\x18\x01 \x01(\x05\x12\x13\n\x0bveh_my_code\x18\x02 \x01(\x05\x12\x14\n\x0cveh_mfg_code\x18\x03 \x01(\x05"\xb3\x03\n\x11Occupancy_rpt_415\x12&\n\x1erear_seatbelt_buckled_is_valid\x18\x01 \x01(\x08\x12&\n\x1epass_seatbelt_buckled_is_valid\x18\x02 \x01(\x08\x12(\n driver_seatbelt_buckled_is_valid\x18\x03 \x01(\x08\x12#\n\x1brear_seat_occupied_is_valid\x18\x04 \x01(\x08\x12#\n\x1bpass_seat_occupied_is_valid\x18\x05 \x01(\x08\x12%\n\x1ddriver_seat_occupied_is_valid\x18\x06 \x01(\x08\x12\x1d\n\x15rear_seatbelt_buckled\x18\x07 \x01(\x08\x12\x1d\n\x15pass_seatbelt_buckled\x18\x08 \x01(\x08\x12\x1f\n\x17driver_seatbelt_buckled\x18\t \x01(\x08\x12\x1a\n\x12rear_seat_occupied\x18\n \x01(\x08\x12\x1a\n\x12pass_seat_occupied\x18\x0b \x01(\x08\x12\x1c\n\x14driver_seat_occupied\x18\x0c \x01(\x08"\xb6\x05\n\x17Interior_lights_rpt_416\x12\x1a\n\x12dim_level_is_valid\x18\x01 \x01(\x08\x12\x1f\n\x17mood_lights_on_is_valid\x18\x02 \x01(\x08\x12$\n\x1crear_dome_lights_on_is_valid\x18\x03 \x01(\x08\x12%\n\x1dfront_dome_lights_on_is_valid\x18\x04 \x01(\x08\x12G\n\tdim_level\x18\x05 \x01(\x0e24.apollo.canbus.Interior_lights_rpt_416.Dim_levelType\x12\x16\n\x0emood_lights_on\x18\x06 \x01(\x08\x12\x1b\n\x13rear_dome_lights_on\x18\x07 \x01(\x08\x12\x1c\n\x14front_dome_lights_on\x18\x08 \x01(\x08"\xf4\x02\n\rDim_levelType\x12\x1b\n\x17DIM_LEVEL_DIM_LEVEL_MIN\x10\x00\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_1\x10\x01\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_2\x10\x02\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_3\x10\x03\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_4\x10\x04\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_5\x10\x05\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_6\x10\x06\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_7\x10\x07\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_8\x10\x08\x12\x19\n\x15DIM_LEVEL_DIM_LEVEL_9\x10\t\x12\x1a\n\x16DIM_LEVEL_DIM_LEVEL_10\x10\n\x12\x1a\n\x16DIM_LEVEL_DIM_LEVEL_11\x10\x0b\x12\x1b\n\x17DIM_LEVEL_DIM_LEVEL_MAX\x10\x0c"\xb3\x02\n\x0cTurn_cmd_130\x12\x18\n\x10ignore_overrides\x18\x01 \x01(\x08\x12\x0e\n\x06enable\x18\x02 \x01(\x08\x12\x16\n\x0eclear_override\x18\x03 \x01(\x08\x12\x14\n\x0cclear_faults\x18\x04 \x01(\x08\x12H\n\x0fturn_signal_cmd\x18\x05 \x01(\x0e2/.apollo.canbus.Turn_cmd_130.Turn_signal_cmdType"\x80\x01\n\x13Turn_signal_cmdType\x12\x19\n\x15TURN_SIGNAL_CMD_RIGHT\x10\x00\x12\x18\n\x14TURN_SIGNAL_CMD_NONE\x10\x01\x12\x18\n\x14TURN_SIGNAL_CMD_LEFT\x10\x02\x12\x1a\n\x16TURN_SIGNAL_CMD_HAZARD\x10\x03"h\n\x17Detected_object_rpt_411\x12&\n\x1efront_object_distance_high_res\x18\x01 \x01(\x01\x12%\n\x1dfront_object_distance_low_res\x18\x02 \x01(\x01"B\n\x16Veh_specific_rpt_1_412\x12\x13\n\x0bshift_pos_2\x18\x01 \x01(\x05\x12\x13\n\x0bshift_pos_1\x18\x02 \x01(\x05",\n\x14Veh_dynamics_rpt_413\x12\x14\n\x0cveh_g_forces\x18\x01 \x01(\x01"\x8f\x01\n\x13Rear_lights_rpt_418\x12"\n\x1areverse_lights_on_is_valid\x18\x01 \x01(\x08\x12 \n\x18brake_lights_on_is_valid\x18\x02 \x01(\x08\x12\x19\n\x11reverse_lights_on\x18\x03 \x01(\x08\x12\x17\n\x0fbrake_lights_on\x18\x04 \x01(\x08"\x97\x1c\n\x05Lexus\x12C\n\x15hazard_lights_rpt_214\x18\x01 \x01(\x0b2$.apollo.canbus.Hazard_lights_rpt_214\x129\n\x10steering_cmd_12c\x18\x02 \x01(\x0b2\x1f.apollo.canbus.Steering_cmd_12c\x12O\n\x1bdash_controls_right_rpt_210\x18\x03 \x01(\x0b2*.apollo.canbus.Dash_controls_right_rpt_210\x12M\n\x1adash_controls_left_cmd_10c\x18\x04 \x01(\x0b2).apollo.canbus.Dash_controls_left_cmd_10c\x129\n\x10steering_rpt_22c\x18\x05 \x01(\x0b2\x1f.apollo.canbus.Steering_rpt_22c\x129\n\x10turn_aux_rpt_330\x18\x06 \x01(\x0b2\x1f.apollo.canbus.Turn_aux_rpt_330\x12;\n\x11headlight_rpt_218\x18\x07 \x01(\x0b2 .apollo.canbus.Headlight_rpt_218\x12C\n\x15hazard_lights_cmd_114\x18\x08 \x01(\x0b2$.apollo.canbus.Hazard_lights_cmd_114\x12M\n\x1adash_controls_left_rpt_20c\x18\t \x01(\x0b2).apollo.canbus.Dash_controls_left_rpt_20c\x12C\n\x15headlight_aux_rpt_318\x18\n \x01(\x0b2$.apollo.canbus.Headlight_aux_rpt_318\x12O\n\x1bdash_controls_right_cmd_110\x18\x0b \x01(\x0b2*.apollo.canbus.Dash_controls_right_cmd_110\x123\n\rwiper_cmd_134\x18\x0c \x01(\x0b2\x1c.apollo.canbus.Wiper_cmd_134\x123\n\rwiper_rpt_234\x18\r \x01(\x0b2\x1c.apollo.canbus.Wiper_rpt_234\x121\n\x0cturn_rpt_230\x18\x0e \x01(\x0b2\x1b.apollo.canbus.Turn_rpt_230\x12;\n\x11headlight_cmd_118\x18\x0f \x01(\x0b2 .apollo.canbus.Headlight_cmd_118\x121\n\x0cdoor_rpt_417\x18\x10 \x01(\x0b2\x1b.apollo.canbus.Door_rpt_417\x129\n\x10component_rpt_20\x18\x11 \x01(\x0b2\x1f.apollo.canbus.Component_rpt_20\x12?\n\x13wheel_speed_rpt_407\x18\x12 \x01(\x0b2".apollo.canbus.Wheel_speed_rpt_407\x12I\n\x18steering_motor_rpt_3_406\x18\x13 \x01(\x0b2\'.apollo.canbus.Steering_motor_rpt_3_406\x12I\n\x18steering_motor_rpt_2_405\x18\x14 \x01(\x0b2\'.apollo.canbus.Steering_motor_rpt_2_405\x12I\n\x18steering_motor_rpt_1_404\x18\x15 \x01(\x0b2\'.apollo.canbus.Steering_motor_rpt_1_404\x12C\n\x15brake_motor_rpt_3_403\x18\x16 \x01(\x0b2$.apollo.canbus.Brake_motor_rpt_3_403\x12C\n\x15brake_motor_rpt_2_402\x18\x17 \x01(\x0b2$.apollo.canbus.Brake_motor_rpt_2_402\x12C\n\x15brake_motor_rpt_1_401\x18\x18 \x01(\x0b2$.apollo.canbus.Brake_motor_rpt_1_401\x12;\n\x11wiper_aux_rpt_334\x18\x19 \x01(\x0b2 .apollo.canbus.Wiper_aux_rpt_334\x12;\n\x11shift_aux_rpt_328\x18\x1a \x01(\x0b2 .apollo.canbus.Shift_aux_rpt_328\x123\n\raccel_rpt_200\x18\x1b \x01(\x0b2\x1c.apollo.canbus.Accel_rpt_200\x123\n\rbrake_rpt_204\x18\x1c \x01(\x0b2\x1c.apollo.canbus.Brake_rpt_204\x121\n\x0chorn_cmd_11c\x18\x1d \x01(\x0b2\x1b.apollo.canbus.Horn_cmd_11c\x123\n\rglobal_rpt_10\x18\x1e \x01(\x0b2\x1c.apollo.canbus.Global_rpt_10\x12;\n\x11accel_aux_rpt_300\x18\x1f \x01(\x0b2 .apollo.canbus.Accel_aux_rpt_300\x12U\n\x1ecruise_control_buttons_rpt_208\x18  \x01(\x0b2-.apollo.canbus.Cruise_control_buttons_rpt_208\x12C\n\x15vehicle_speed_rpt_400\x18! \x01(\x0b2$.apollo.canbus.Vehicle_speed_rpt_400\x12;\n\x11brake_aux_rpt_304\x18" \x01(\x0b2 .apollo.canbus.Brake_aux_rpt_304\x12E\n\x16media_controls_cmd_120\x18# \x01(\x0b2%.apollo.canbus.Media_controls_cmd_120\x12U\n\x1ecruise_control_buttons_cmd_108\x18$ \x01(\x0b2-.apollo.canbus.Cruise_control_buttons_cmd_108\x12C\n\x15parking_brake_cmd_124\x18% \x01(\x0b2$.apollo.canbus.Parking_brake_cmd_124\x121\n\x0chorn_rpt_21c\x18& \x01(\x0b2\x1b.apollo.canbus.Horn_rpt_21c\x123\n\rshift_rpt_228\x18\' \x01(\x0b2\x1c.apollo.canbus.Shift_rpt_228\x123\n\rshift_cmd_128\x18( \x01(\x0b2\x1c.apollo.canbus.Shift_cmd_128\x123\n\raccel_cmd_100\x18) \x01(\x0b2\x1c.apollo.canbus.Accel_cmd_100\x12C\n\x15parking_brake_rpt_224\x18* \x01(\x0b2$.apollo.canbus.Parking_brake_rpt_224\x123\n\rbrake_cmd_104\x18+ \x01(\x0b2\x1c.apollo.canbus.Brake_cmd_104\x12E\n\x16media_controls_rpt_220\x18, \x01(\x0b2%.apollo.canbus.Media_controls_rpt_220\x12A\n\x14steering_aux_rpt_32c\x18- \x01(\x0b2#.apollo.canbus.Steering_aux_rpt_32c\x12G\n\x17lat_lon_heading_rpt_40e\x18. \x01(\x0b2&.apollo.canbus.Lat_lon_heading_rpt_40e\x129\n\x10yaw_rate_rpt_40d\x18/ \x01(\x0b2\x1f.apollo.canbus.Yaw_rate_rpt_40d\x12;\n\x11date_time_rpt_40f\x180 \x01(\x0b2 .apollo.canbus.Date_time_rpt_40f\x12/\n\x0bvin_rpt_414\x181 \x01(\x0b2\x1a.apollo.canbus.Vin_rpt_414\x12;\n\x11occupancy_rpt_415\x182 \x01(\x0b2 .apollo.canbus.Occupancy_rpt_415\x12G\n\x17interior_lights_rpt_416\x183 \x01(\x0b2&.apollo.canbus.Interior_lights_rpt_416\x121\n\x0cturn_cmd_130\x184 \x01(\x0b2\x1b.apollo.canbus.Turn_cmd_130\x12G\n\x17detected_object_rpt_411\x185 \x01(\x0b2&.apollo.canbus.Detected_object_rpt_411\x12E\n\x16veh_specific_rpt_1_412\x186 \x01(\x0b2%.apollo.canbus.Veh_specific_rpt_1_412\x12A\n\x14veh_dynamics_rpt_413\x187 \x01(\x0b2#.apollo.canbus.Veh_dynamics_rpt_413\x12?\n\x13rear_lights_rpt_418\x188 \x01(\x0b2".apollo.canbus.Rear_lights_rpt_418')
_HAZARD_LIGHTS_RPT_214 = DESCRIPTOR.message_types_by_name['Hazard_lights_rpt_214']
_STEERING_CMD_12C = DESCRIPTOR.message_types_by_name['Steering_cmd_12c']
_DASH_CONTROLS_RIGHT_RPT_210 = DESCRIPTOR.message_types_by_name['Dash_controls_right_rpt_210']
_DASH_CONTROLS_LEFT_CMD_10C = DESCRIPTOR.message_types_by_name['Dash_controls_left_cmd_10c']
_STEERING_RPT_22C = DESCRIPTOR.message_types_by_name['Steering_rpt_22c']
_TURN_AUX_RPT_330 = DESCRIPTOR.message_types_by_name['Turn_aux_rpt_330']
_HEADLIGHT_RPT_218 = DESCRIPTOR.message_types_by_name['Headlight_rpt_218']
_HAZARD_LIGHTS_CMD_114 = DESCRIPTOR.message_types_by_name['Hazard_lights_cmd_114']
_DASH_CONTROLS_LEFT_RPT_20C = DESCRIPTOR.message_types_by_name['Dash_controls_left_rpt_20c']
_HEADLIGHT_AUX_RPT_318 = DESCRIPTOR.message_types_by_name['Headlight_aux_rpt_318']
_DASH_CONTROLS_RIGHT_CMD_110 = DESCRIPTOR.message_types_by_name['Dash_controls_right_cmd_110']
_WIPER_CMD_134 = DESCRIPTOR.message_types_by_name['Wiper_cmd_134']
_WIPER_RPT_234 = DESCRIPTOR.message_types_by_name['Wiper_rpt_234']
_TURN_RPT_230 = DESCRIPTOR.message_types_by_name['Turn_rpt_230']
_HEADLIGHT_CMD_118 = DESCRIPTOR.message_types_by_name['Headlight_cmd_118']
_DOOR_RPT_417 = DESCRIPTOR.message_types_by_name['Door_rpt_417']
_COMPONENT_RPT_20 = DESCRIPTOR.message_types_by_name['Component_rpt_20']
_WHEEL_SPEED_RPT_407 = DESCRIPTOR.message_types_by_name['Wheel_speed_rpt_407']
_STEERING_MOTOR_RPT_3_406 = DESCRIPTOR.message_types_by_name['Steering_motor_rpt_3_406']
_STEERING_MOTOR_RPT_2_405 = DESCRIPTOR.message_types_by_name['Steering_motor_rpt_2_405']
_STEERING_MOTOR_RPT_1_404 = DESCRIPTOR.message_types_by_name['Steering_motor_rpt_1_404']
_BRAKE_MOTOR_RPT_3_403 = DESCRIPTOR.message_types_by_name['Brake_motor_rpt_3_403']
_BRAKE_MOTOR_RPT_2_402 = DESCRIPTOR.message_types_by_name['Brake_motor_rpt_2_402']
_BRAKE_MOTOR_RPT_1_401 = DESCRIPTOR.message_types_by_name['Brake_motor_rpt_1_401']
_WIPER_AUX_RPT_334 = DESCRIPTOR.message_types_by_name['Wiper_aux_rpt_334']
_SHIFT_AUX_RPT_328 = DESCRIPTOR.message_types_by_name['Shift_aux_rpt_328']
_ACCEL_RPT_200 = DESCRIPTOR.message_types_by_name['Accel_rpt_200']
_BRAKE_RPT_204 = DESCRIPTOR.message_types_by_name['Brake_rpt_204']
_HORN_CMD_11C = DESCRIPTOR.message_types_by_name['Horn_cmd_11c']
_GLOBAL_RPT_10 = DESCRIPTOR.message_types_by_name['Global_rpt_10']
_ACCEL_AUX_RPT_300 = DESCRIPTOR.message_types_by_name['Accel_aux_rpt_300']
_CRUISE_CONTROL_BUTTONS_RPT_208 = DESCRIPTOR.message_types_by_name['Cruise_control_buttons_rpt_208']
_VEHICLE_SPEED_RPT_400 = DESCRIPTOR.message_types_by_name['Vehicle_speed_rpt_400']
_BRAKE_AUX_RPT_304 = DESCRIPTOR.message_types_by_name['Brake_aux_rpt_304']
_MEDIA_CONTROLS_CMD_120 = DESCRIPTOR.message_types_by_name['Media_controls_cmd_120']
_CRUISE_CONTROL_BUTTONS_CMD_108 = DESCRIPTOR.message_types_by_name['Cruise_control_buttons_cmd_108']
_PARKING_BRAKE_CMD_124 = DESCRIPTOR.message_types_by_name['Parking_brake_cmd_124']
_HORN_RPT_21C = DESCRIPTOR.message_types_by_name['Horn_rpt_21c']
_SHIFT_RPT_228 = DESCRIPTOR.message_types_by_name['Shift_rpt_228']
_SHIFT_CMD_128 = DESCRIPTOR.message_types_by_name['Shift_cmd_128']
_ACCEL_CMD_100 = DESCRIPTOR.message_types_by_name['Accel_cmd_100']
_PARKING_BRAKE_RPT_224 = DESCRIPTOR.message_types_by_name['Parking_brake_rpt_224']
_BRAKE_CMD_104 = DESCRIPTOR.message_types_by_name['Brake_cmd_104']
_MEDIA_CONTROLS_RPT_220 = DESCRIPTOR.message_types_by_name['Media_controls_rpt_220']
_STEERING_AUX_RPT_32C = DESCRIPTOR.message_types_by_name['Steering_aux_rpt_32c']
_LAT_LON_HEADING_RPT_40E = DESCRIPTOR.message_types_by_name['Lat_lon_heading_rpt_40e']
_YAW_RATE_RPT_40D = DESCRIPTOR.message_types_by_name['Yaw_rate_rpt_40d']
_DATE_TIME_RPT_40F = DESCRIPTOR.message_types_by_name['Date_time_rpt_40f']
_VIN_RPT_414 = DESCRIPTOR.message_types_by_name['Vin_rpt_414']
_OCCUPANCY_RPT_415 = DESCRIPTOR.message_types_by_name['Occupancy_rpt_415']
_INTERIOR_LIGHTS_RPT_416 = DESCRIPTOR.message_types_by_name['Interior_lights_rpt_416']
_TURN_CMD_130 = DESCRIPTOR.message_types_by_name['Turn_cmd_130']
_DETECTED_OBJECT_RPT_411 = DESCRIPTOR.message_types_by_name['Detected_object_rpt_411']
_VEH_SPECIFIC_RPT_1_412 = DESCRIPTOR.message_types_by_name['Veh_specific_rpt_1_412']
_VEH_DYNAMICS_RPT_413 = DESCRIPTOR.message_types_by_name['Veh_dynamics_rpt_413']
_REAR_LIGHTS_RPT_418 = DESCRIPTOR.message_types_by_name['Rear_lights_rpt_418']
_LEXUS = DESCRIPTOR.message_types_by_name['Lexus']
_DASH_CONTROLS_RIGHT_RPT_210_OUTPUT_VALUETYPE = _DASH_CONTROLS_RIGHT_RPT_210.enum_types_by_name['Output_valueType']
_DASH_CONTROLS_RIGHT_RPT_210_COMMANDED_VALUETYPE = _DASH_CONTROLS_RIGHT_RPT_210.enum_types_by_name['Commanded_valueType']
_DASH_CONTROLS_RIGHT_RPT_210_MANUAL_INPUTTYPE = _DASH_CONTROLS_RIGHT_RPT_210.enum_types_by_name['Manual_inputType']
_DASH_CONTROLS_LEFT_CMD_10C_DASH_CONTROLS_BUTTONTYPE = _DASH_CONTROLS_LEFT_CMD_10C.enum_types_by_name['Dash_controls_buttonType']
_HEADLIGHT_RPT_218_OUTPUT_VALUETYPE = _HEADLIGHT_RPT_218.enum_types_by_name['Output_valueType']
_HEADLIGHT_RPT_218_MANUAL_INPUTTYPE = _HEADLIGHT_RPT_218.enum_types_by_name['Manual_inputType']
_HEADLIGHT_RPT_218_COMMANDED_VALUETYPE = _HEADLIGHT_RPT_218.enum_types_by_name['Commanded_valueType']
_DASH_CONTROLS_LEFT_RPT_20C_OUTPUT_VALUETYPE = _DASH_CONTROLS_LEFT_RPT_20C.enum_types_by_name['Output_valueType']
_DASH_CONTROLS_LEFT_RPT_20C_COMMANDED_VALUETYPE = _DASH_CONTROLS_LEFT_RPT_20C.enum_types_by_name['Commanded_valueType']
_DASH_CONTROLS_LEFT_RPT_20C_MANUAL_INPUTTYPE = _DASH_CONTROLS_LEFT_RPT_20C.enum_types_by_name['Manual_inputType']
_HEADLIGHT_AUX_RPT_318_HEADLIGHTS_MODETYPE = _HEADLIGHT_AUX_RPT_318.enum_types_by_name['Headlights_modeType']
_DASH_CONTROLS_RIGHT_CMD_110_DASH_CONTROLS_BUTTONTYPE = _DASH_CONTROLS_RIGHT_CMD_110.enum_types_by_name['Dash_controls_buttonType']
_WIPER_CMD_134_WIPER_CMDTYPE = _WIPER_CMD_134.enum_types_by_name['Wiper_cmdType']
_WIPER_RPT_234_OUTPUT_VALUETYPE = _WIPER_RPT_234.enum_types_by_name['Output_valueType']
_WIPER_RPT_234_COMMANDED_VALUETYPE = _WIPER_RPT_234.enum_types_by_name['Commanded_valueType']
_WIPER_RPT_234_MANUAL_INPUTTYPE = _WIPER_RPT_234.enum_types_by_name['Manual_inputType']
_TURN_RPT_230_MANUAL_INPUTTYPE = _TURN_RPT_230.enum_types_by_name['Manual_inputType']
_TURN_RPT_230_COMMANDED_VALUETYPE = _TURN_RPT_230.enum_types_by_name['Commanded_valueType']
_TURN_RPT_230_OUTPUT_VALUETYPE = _TURN_RPT_230.enum_types_by_name['Output_valueType']
_HEADLIGHT_CMD_118_HEADLIGHT_CMDTYPE = _HEADLIGHT_CMD_118.enum_types_by_name['Headlight_cmdType']
_COMPONENT_RPT_20_COMPONENT_TYPETYPE = _COMPONENT_RPT_20.enum_types_by_name['Component_typeType']
_COMPONENT_RPT_20_COMPONENT_FUNCTYPE = _COMPONENT_RPT_20.enum_types_by_name['Component_funcType']
_HORN_CMD_11C_HORN_CMDTYPE = _HORN_CMD_11C.enum_types_by_name['Horn_cmdType']
_GLOBAL_RPT_10_PACMOD_SYSTEM_ENABLEDTYPE = _GLOBAL_RPT_10.enum_types_by_name['Pacmod_system_enabledType']
_GLOBAL_RPT_10_PACMOD_SYSTEM_OVERRIDE_ACTIVETYPE = _GLOBAL_RPT_10.enum_types_by_name['Pacmod_system_override_activeType']
_GLOBAL_RPT_10_BRK_CAN_TIMEOUTTYPE = _GLOBAL_RPT_10.enum_types_by_name['Brk_can_timeoutType']
_CRUISE_CONTROL_BUTTONS_RPT_208_OUTPUT_VALUETYPE = _CRUISE_CONTROL_BUTTONS_RPT_208.enum_types_by_name['Output_valueType']
_CRUISE_CONTROL_BUTTONS_RPT_208_MANUAL_INPUTTYPE = _CRUISE_CONTROL_BUTTONS_RPT_208.enum_types_by_name['Manual_inputType']
_CRUISE_CONTROL_BUTTONS_RPT_208_COMMANDED_VALUETYPE = _CRUISE_CONTROL_BUTTONS_RPT_208.enum_types_by_name['Commanded_valueType']
_VEHICLE_SPEED_RPT_400_VEHICLE_SPEED_VALIDTYPE = _VEHICLE_SPEED_RPT_400.enum_types_by_name['Vehicle_speed_validType']
_MEDIA_CONTROLS_CMD_120_MEDIA_CONTROLS_CMDTYPE = _MEDIA_CONTROLS_CMD_120.enum_types_by_name['Media_controls_cmdType']
_CRUISE_CONTROL_BUTTONS_CMD_108_CRUISE_CONTROL_BUTTONTYPE = _CRUISE_CONTROL_BUTTONS_CMD_108.enum_types_by_name['Cruise_control_buttonType']
_HORN_RPT_21C_OUTPUT_VALUETYPE = _HORN_RPT_21C.enum_types_by_name['Output_valueType']
_HORN_RPT_21C_COMMANDED_VALUETYPE = _HORN_RPT_21C.enum_types_by_name['Commanded_valueType']
_HORN_RPT_21C_MANUAL_INPUTTYPE = _HORN_RPT_21C.enum_types_by_name['Manual_inputType']
_SHIFT_RPT_228_MANUAL_INPUTTYPE = _SHIFT_RPT_228.enum_types_by_name['Manual_inputType']
_SHIFT_RPT_228_COMMANDED_VALUETYPE = _SHIFT_RPT_228.enum_types_by_name['Commanded_valueType']
_SHIFT_RPT_228_OUTPUT_VALUETYPE = _SHIFT_RPT_228.enum_types_by_name['Output_valueType']
_SHIFT_CMD_128_SHIFT_CMDTYPE = _SHIFT_CMD_128.enum_types_by_name['Shift_cmdType']
_MEDIA_CONTROLS_RPT_220_OUTPUT_VALUETYPE = _MEDIA_CONTROLS_RPT_220.enum_types_by_name['Output_valueType']
_MEDIA_CONTROLS_RPT_220_COMMANDED_VALUETYPE = _MEDIA_CONTROLS_RPT_220.enum_types_by_name['Commanded_valueType']
_MEDIA_CONTROLS_RPT_220_MANUAL_INPUTTYPE = _MEDIA_CONTROLS_RPT_220.enum_types_by_name['Manual_inputType']
_INTERIOR_LIGHTS_RPT_416_DIM_LEVELTYPE = _INTERIOR_LIGHTS_RPT_416.enum_types_by_name['Dim_levelType']
_TURN_CMD_130_TURN_SIGNAL_CMDTYPE = _TURN_CMD_130.enum_types_by_name['Turn_signal_cmdType']
Hazard_lights_rpt_214 = _reflection.GeneratedProtocolMessageType('Hazard_lights_rpt_214', (_message.Message,), {'DESCRIPTOR': _HAZARD_LIGHTS_RPT_214, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Hazard_lights_rpt_214)
Steering_cmd_12c = _reflection.GeneratedProtocolMessageType('Steering_cmd_12c', (_message.Message,), {'DESCRIPTOR': _STEERING_CMD_12C, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Steering_cmd_12c)
Dash_controls_right_rpt_210 = _reflection.GeneratedProtocolMessageType('Dash_controls_right_rpt_210', (_message.Message,), {'DESCRIPTOR': _DASH_CONTROLS_RIGHT_RPT_210, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Dash_controls_right_rpt_210)
Dash_controls_left_cmd_10c = _reflection.GeneratedProtocolMessageType('Dash_controls_left_cmd_10c', (_message.Message,), {'DESCRIPTOR': _DASH_CONTROLS_LEFT_CMD_10C, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Dash_controls_left_cmd_10c)
Steering_rpt_22c = _reflection.GeneratedProtocolMessageType('Steering_rpt_22c', (_message.Message,), {'DESCRIPTOR': _STEERING_RPT_22C, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Steering_rpt_22c)
Turn_aux_rpt_330 = _reflection.GeneratedProtocolMessageType('Turn_aux_rpt_330', (_message.Message,), {'DESCRIPTOR': _TURN_AUX_RPT_330, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Turn_aux_rpt_330)
Headlight_rpt_218 = _reflection.GeneratedProtocolMessageType('Headlight_rpt_218', (_message.Message,), {'DESCRIPTOR': _HEADLIGHT_RPT_218, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Headlight_rpt_218)
Hazard_lights_cmd_114 = _reflection.GeneratedProtocolMessageType('Hazard_lights_cmd_114', (_message.Message,), {'DESCRIPTOR': _HAZARD_LIGHTS_CMD_114, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Hazard_lights_cmd_114)
Dash_controls_left_rpt_20c = _reflection.GeneratedProtocolMessageType('Dash_controls_left_rpt_20c', (_message.Message,), {'DESCRIPTOR': _DASH_CONTROLS_LEFT_RPT_20C, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Dash_controls_left_rpt_20c)
Headlight_aux_rpt_318 = _reflection.GeneratedProtocolMessageType('Headlight_aux_rpt_318', (_message.Message,), {'DESCRIPTOR': _HEADLIGHT_AUX_RPT_318, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Headlight_aux_rpt_318)
Dash_controls_right_cmd_110 = _reflection.GeneratedProtocolMessageType('Dash_controls_right_cmd_110', (_message.Message,), {'DESCRIPTOR': _DASH_CONTROLS_RIGHT_CMD_110, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Dash_controls_right_cmd_110)
Wiper_cmd_134 = _reflection.GeneratedProtocolMessageType('Wiper_cmd_134', (_message.Message,), {'DESCRIPTOR': _WIPER_CMD_134, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Wiper_cmd_134)
Wiper_rpt_234 = _reflection.GeneratedProtocolMessageType('Wiper_rpt_234', (_message.Message,), {'DESCRIPTOR': _WIPER_RPT_234, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Wiper_rpt_234)
Turn_rpt_230 = _reflection.GeneratedProtocolMessageType('Turn_rpt_230', (_message.Message,), {'DESCRIPTOR': _TURN_RPT_230, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Turn_rpt_230)
Headlight_cmd_118 = _reflection.GeneratedProtocolMessageType('Headlight_cmd_118', (_message.Message,), {'DESCRIPTOR': _HEADLIGHT_CMD_118, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Headlight_cmd_118)
Door_rpt_417 = _reflection.GeneratedProtocolMessageType('Door_rpt_417', (_message.Message,), {'DESCRIPTOR': _DOOR_RPT_417, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Door_rpt_417)
Component_rpt_20 = _reflection.GeneratedProtocolMessageType('Component_rpt_20', (_message.Message,), {'DESCRIPTOR': _COMPONENT_RPT_20, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Component_rpt_20)
Wheel_speed_rpt_407 = _reflection.GeneratedProtocolMessageType('Wheel_speed_rpt_407', (_message.Message,), {'DESCRIPTOR': _WHEEL_SPEED_RPT_407, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Wheel_speed_rpt_407)
Steering_motor_rpt_3_406 = _reflection.GeneratedProtocolMessageType('Steering_motor_rpt_3_406', (_message.Message,), {'DESCRIPTOR': _STEERING_MOTOR_RPT_3_406, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Steering_motor_rpt_3_406)
Steering_motor_rpt_2_405 = _reflection.GeneratedProtocolMessageType('Steering_motor_rpt_2_405', (_message.Message,), {'DESCRIPTOR': _STEERING_MOTOR_RPT_2_405, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Steering_motor_rpt_2_405)
Steering_motor_rpt_1_404 = _reflection.GeneratedProtocolMessageType('Steering_motor_rpt_1_404', (_message.Message,), {'DESCRIPTOR': _STEERING_MOTOR_RPT_1_404, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Steering_motor_rpt_1_404)
Brake_motor_rpt_3_403 = _reflection.GeneratedProtocolMessageType('Brake_motor_rpt_3_403', (_message.Message,), {'DESCRIPTOR': _BRAKE_MOTOR_RPT_3_403, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Brake_motor_rpt_3_403)
Brake_motor_rpt_2_402 = _reflection.GeneratedProtocolMessageType('Brake_motor_rpt_2_402', (_message.Message,), {'DESCRIPTOR': _BRAKE_MOTOR_RPT_2_402, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Brake_motor_rpt_2_402)
Brake_motor_rpt_1_401 = _reflection.GeneratedProtocolMessageType('Brake_motor_rpt_1_401', (_message.Message,), {'DESCRIPTOR': _BRAKE_MOTOR_RPT_1_401, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Brake_motor_rpt_1_401)
Wiper_aux_rpt_334 = _reflection.GeneratedProtocolMessageType('Wiper_aux_rpt_334', (_message.Message,), {'DESCRIPTOR': _WIPER_AUX_RPT_334, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Wiper_aux_rpt_334)
Shift_aux_rpt_328 = _reflection.GeneratedProtocolMessageType('Shift_aux_rpt_328', (_message.Message,), {'DESCRIPTOR': _SHIFT_AUX_RPT_328, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Shift_aux_rpt_328)
Accel_rpt_200 = _reflection.GeneratedProtocolMessageType('Accel_rpt_200', (_message.Message,), {'DESCRIPTOR': _ACCEL_RPT_200, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Accel_rpt_200)
Brake_rpt_204 = _reflection.GeneratedProtocolMessageType('Brake_rpt_204', (_message.Message,), {'DESCRIPTOR': _BRAKE_RPT_204, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Brake_rpt_204)
Horn_cmd_11c = _reflection.GeneratedProtocolMessageType('Horn_cmd_11c', (_message.Message,), {'DESCRIPTOR': _HORN_CMD_11C, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Horn_cmd_11c)
Global_rpt_10 = _reflection.GeneratedProtocolMessageType('Global_rpt_10', (_message.Message,), {'DESCRIPTOR': _GLOBAL_RPT_10, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Global_rpt_10)
Accel_aux_rpt_300 = _reflection.GeneratedProtocolMessageType('Accel_aux_rpt_300', (_message.Message,), {'DESCRIPTOR': _ACCEL_AUX_RPT_300, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Accel_aux_rpt_300)
Cruise_control_buttons_rpt_208 = _reflection.GeneratedProtocolMessageType('Cruise_control_buttons_rpt_208', (_message.Message,), {'DESCRIPTOR': _CRUISE_CONTROL_BUTTONS_RPT_208, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Cruise_control_buttons_rpt_208)
Vehicle_speed_rpt_400 = _reflection.GeneratedProtocolMessageType('Vehicle_speed_rpt_400', (_message.Message,), {'DESCRIPTOR': _VEHICLE_SPEED_RPT_400, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Vehicle_speed_rpt_400)
Brake_aux_rpt_304 = _reflection.GeneratedProtocolMessageType('Brake_aux_rpt_304', (_message.Message,), {'DESCRIPTOR': _BRAKE_AUX_RPT_304, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Brake_aux_rpt_304)
Media_controls_cmd_120 = _reflection.GeneratedProtocolMessageType('Media_controls_cmd_120', (_message.Message,), {'DESCRIPTOR': _MEDIA_CONTROLS_CMD_120, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Media_controls_cmd_120)
Cruise_control_buttons_cmd_108 = _reflection.GeneratedProtocolMessageType('Cruise_control_buttons_cmd_108', (_message.Message,), {'DESCRIPTOR': _CRUISE_CONTROL_BUTTONS_CMD_108, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Cruise_control_buttons_cmd_108)
Parking_brake_cmd_124 = _reflection.GeneratedProtocolMessageType('Parking_brake_cmd_124', (_message.Message,), {'DESCRIPTOR': _PARKING_BRAKE_CMD_124, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Parking_brake_cmd_124)
Horn_rpt_21c = _reflection.GeneratedProtocolMessageType('Horn_rpt_21c', (_message.Message,), {'DESCRIPTOR': _HORN_RPT_21C, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Horn_rpt_21c)
Shift_rpt_228 = _reflection.GeneratedProtocolMessageType('Shift_rpt_228', (_message.Message,), {'DESCRIPTOR': _SHIFT_RPT_228, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Shift_rpt_228)
Shift_cmd_128 = _reflection.GeneratedProtocolMessageType('Shift_cmd_128', (_message.Message,), {'DESCRIPTOR': _SHIFT_CMD_128, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Shift_cmd_128)
Accel_cmd_100 = _reflection.GeneratedProtocolMessageType('Accel_cmd_100', (_message.Message,), {'DESCRIPTOR': _ACCEL_CMD_100, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Accel_cmd_100)
Parking_brake_rpt_224 = _reflection.GeneratedProtocolMessageType('Parking_brake_rpt_224', (_message.Message,), {'DESCRIPTOR': _PARKING_BRAKE_RPT_224, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Parking_brake_rpt_224)
Brake_cmd_104 = _reflection.GeneratedProtocolMessageType('Brake_cmd_104', (_message.Message,), {'DESCRIPTOR': _BRAKE_CMD_104, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Brake_cmd_104)
Media_controls_rpt_220 = _reflection.GeneratedProtocolMessageType('Media_controls_rpt_220', (_message.Message,), {'DESCRIPTOR': _MEDIA_CONTROLS_RPT_220, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Media_controls_rpt_220)
Steering_aux_rpt_32c = _reflection.GeneratedProtocolMessageType('Steering_aux_rpt_32c', (_message.Message,), {'DESCRIPTOR': _STEERING_AUX_RPT_32C, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Steering_aux_rpt_32c)
Lat_lon_heading_rpt_40e = _reflection.GeneratedProtocolMessageType('Lat_lon_heading_rpt_40e', (_message.Message,), {'DESCRIPTOR': _LAT_LON_HEADING_RPT_40E, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Lat_lon_heading_rpt_40e)
Yaw_rate_rpt_40d = _reflection.GeneratedProtocolMessageType('Yaw_rate_rpt_40d', (_message.Message,), {'DESCRIPTOR': _YAW_RATE_RPT_40D, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Yaw_rate_rpt_40d)
Date_time_rpt_40f = _reflection.GeneratedProtocolMessageType('Date_time_rpt_40f', (_message.Message,), {'DESCRIPTOR': _DATE_TIME_RPT_40F, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Date_time_rpt_40f)
Vin_rpt_414 = _reflection.GeneratedProtocolMessageType('Vin_rpt_414', (_message.Message,), {'DESCRIPTOR': _VIN_RPT_414, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Vin_rpt_414)
Occupancy_rpt_415 = _reflection.GeneratedProtocolMessageType('Occupancy_rpt_415', (_message.Message,), {'DESCRIPTOR': _OCCUPANCY_RPT_415, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Occupancy_rpt_415)
Interior_lights_rpt_416 = _reflection.GeneratedProtocolMessageType('Interior_lights_rpt_416', (_message.Message,), {'DESCRIPTOR': _INTERIOR_LIGHTS_RPT_416, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Interior_lights_rpt_416)
Turn_cmd_130 = _reflection.GeneratedProtocolMessageType('Turn_cmd_130', (_message.Message,), {'DESCRIPTOR': _TURN_CMD_130, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Turn_cmd_130)
Detected_object_rpt_411 = _reflection.GeneratedProtocolMessageType('Detected_object_rpt_411', (_message.Message,), {'DESCRIPTOR': _DETECTED_OBJECT_RPT_411, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Detected_object_rpt_411)
Veh_specific_rpt_1_412 = _reflection.GeneratedProtocolMessageType('Veh_specific_rpt_1_412', (_message.Message,), {'DESCRIPTOR': _VEH_SPECIFIC_RPT_1_412, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Veh_specific_rpt_1_412)
Veh_dynamics_rpt_413 = _reflection.GeneratedProtocolMessageType('Veh_dynamics_rpt_413', (_message.Message,), {'DESCRIPTOR': _VEH_DYNAMICS_RPT_413, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Veh_dynamics_rpt_413)
Rear_lights_rpt_418 = _reflection.GeneratedProtocolMessageType('Rear_lights_rpt_418', (_message.Message,), {'DESCRIPTOR': _REAR_LIGHTS_RPT_418, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Rear_lights_rpt_418)
Lexus = _reflection.GeneratedProtocolMessageType('Lexus', (_message.Message,), {'DESCRIPTOR': _LEXUS, '__module__': 'modules.canbus.proto.lexus_pb2'})
_sym_db.RegisterMessage(Lexus)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _HAZARD_LIGHTS_RPT_214._serialized_start = 52
    _HAZARD_LIGHTS_RPT_214._serialized_end = 320
    _STEERING_CMD_12C._serialized_start = 323
    _STEERING_CMD_12C._serialized_end = 470
    _DASH_CONTROLS_RIGHT_RPT_210._serialized_start = 473
    _DASH_CONTROLS_RIGHT_RPT_210._serialized_end = 1656
    _DASH_CONTROLS_RIGHT_RPT_210_OUTPUT_VALUETYPE._serialized_start = 936
    _DASH_CONTROLS_RIGHT_RPT_210_OUTPUT_VALUETYPE._serialized_end = 1167
    _DASH_CONTROLS_RIGHT_RPT_210_COMMANDED_VALUETYPE._serialized_start = 1170
    _DASH_CONTROLS_RIGHT_RPT_210_COMMANDED_VALUETYPE._serialized_end = 1422
    _DASH_CONTROLS_RIGHT_RPT_210_MANUAL_INPUTTYPE._serialized_start = 1425
    _DASH_CONTROLS_RIGHT_RPT_210_MANUAL_INPUTTYPE._serialized_end = 1656
    _DASH_CONTROLS_LEFT_CMD_10C._serialized_start = 1659
    _DASH_CONTROLS_LEFT_CMD_10C._serialized_end = 2163
    _DASH_CONTROLS_LEFT_CMD_10C_DASH_CONTROLS_BUTTONTYPE._serialized_start = 1876
    _DASH_CONTROLS_LEFT_CMD_10C_DASH_CONTROLS_BUTTONTYPE._serialized_end = 2163
    _STEERING_RPT_22C._serialized_start = 2166
    _STEERING_RPT_22C._serialized_end = 2429
    _TURN_AUX_RPT_330._serialized_start = 2432
    _TURN_AUX_RPT_330._serialized_end = 2592
    _HEADLIGHT_RPT_218._serialized_start = 2595
    _HEADLIGHT_RPT_218._serialized_end = 3357
    _HEADLIGHT_RPT_218_OUTPUT_VALUETYPE._serialized_start = 3017
    _HEADLIGHT_RPT_218_OUTPUT_VALUETYPE._serialized_end = 3125
    _HEADLIGHT_RPT_218_MANUAL_INPUTTYPE._serialized_start = 3127
    _HEADLIGHT_RPT_218_MANUAL_INPUTTYPE._serialized_end = 3235
    _HEADLIGHT_RPT_218_COMMANDED_VALUETYPE._serialized_start = 3237
    _HEADLIGHT_RPT_218_COMMANDED_VALUETYPE._serialized_end = 3357
    _HAZARD_LIGHTS_CMD_114._serialized_start = 3360
    _HAZARD_LIGHTS_CMD_114._serialized_end = 3498
    _DASH_CONTROLS_LEFT_RPT_20C._serialized_start = 3501
    _DASH_CONTROLS_LEFT_RPT_20C._serialized_end = 4680
    _DASH_CONTROLS_LEFT_RPT_20C_OUTPUT_VALUETYPE._serialized_start = 936
    _DASH_CONTROLS_LEFT_RPT_20C_OUTPUT_VALUETYPE._serialized_end = 1167
    _DASH_CONTROLS_LEFT_RPT_20C_COMMANDED_VALUETYPE._serialized_start = 1170
    _DASH_CONTROLS_LEFT_RPT_20C_COMMANDED_VALUETYPE._serialized_end = 1422
    _DASH_CONTROLS_LEFT_RPT_20C_MANUAL_INPUTTYPE._serialized_start = 1425
    _DASH_CONTROLS_LEFT_RPT_20C_MANUAL_INPUTTYPE._serialized_end = 1656
    _HEADLIGHT_AUX_RPT_318._serialized_start = 4683
    _HEADLIGHT_AUX_RPT_318._serialized_end = 5195
    _HEADLIGHT_AUX_RPT_318_HEADLIGHTS_MODETYPE._serialized_start = 5005
    _HEADLIGHT_AUX_RPT_318_HEADLIGHTS_MODETYPE._serialized_end = 5195
    _DASH_CONTROLS_RIGHT_CMD_110._serialized_start = 5198
    _DASH_CONTROLS_RIGHT_CMD_110._serialized_end = 5704
    _DASH_CONTROLS_RIGHT_CMD_110_DASH_CONTROLS_BUTTONTYPE._serialized_start = 1876
    _DASH_CONTROLS_RIGHT_CMD_110_DASH_CONTROLS_BUTTONTYPE._serialized_end = 2163
    _WIPER_CMD_134._serialized_start = 5707
    _WIPER_CMD_134._serialized_end = 6106
    _WIPER_CMD_134_WIPER_CMDTYPE._serialized_start = 5876
    _WIPER_CMD_134_WIPER_CMDTYPE._serialized_end = 6106
    _WIPER_RPT_234._serialized_start = 6109
    _WIPER_RPT_234._serialized_end = 7320
    _WIPER_RPT_234_OUTPUT_VALUETYPE._serialized_start = 6516
    _WIPER_RPT_234_OUTPUT_VALUETYPE._serialized_end = 6773
    _WIPER_RPT_234_COMMANDED_VALUETYPE._serialized_start = 6776
    _WIPER_RPT_234_COMMANDED_VALUETYPE._serialized_end = 7060
    _WIPER_RPT_234_MANUAL_INPUTTYPE._serialized_start = 7063
    _WIPER_RPT_234_MANUAL_INPUTTYPE._serialized_end = 7320
    _TURN_RPT_230._serialized_start = 7323
    _TURN_RPT_230._serialized_end = 8084
    _TURN_RPT_230_MANUAL_INPUTTYPE._serialized_start = 7725
    _TURN_RPT_230_MANUAL_INPUTTYPE._serialized_end = 7838
    _TURN_RPT_230_COMMANDED_VALUETYPE._serialized_start = 7841
    _TURN_RPT_230_COMMANDED_VALUETYPE._serialized_end = 7969
    _TURN_RPT_230_OUTPUT_VALUETYPE._serialized_start = 7971
    _TURN_RPT_230_OUTPUT_VALUETYPE._serialized_end = 8084
    _HEADLIGHT_CMD_118._serialized_start = 8087
    _HEADLIGHT_CMD_118._serialized_end = 8383
    _HEADLIGHT_CMD_118_HEADLIGHT_CMDTYPE._serialized_start = 8271
    _HEADLIGHT_CMD_118_HEADLIGHT_CMDTYPE._serialized_end = 8383
    _DOOR_RPT_417._serialized_start = 8386
    _DOOR_RPT_417._serialized_end = 8809
    _COMPONENT_RPT_20._serialized_start = 8812
    _COMPONENT_RPT_20._serialized_end = 9435
    _COMPONENT_RPT_20_COMPONENT_TYPETYPE._serialized_start = 9043
    _COMPONENT_RPT_20_COMPONENT_TYPETYPE._serialized_end = 9147
    _COMPONENT_RPT_20_COMPONENT_FUNCTYPE._serialized_start = 9150
    _COMPONENT_RPT_20_COMPONENT_FUNCTYPE._serialized_end = 9435
    _WHEEL_SPEED_RPT_407._serialized_start = 9438
    _WHEEL_SPEED_RPT_407._serialized_end = 9579
    _STEERING_MOTOR_RPT_3_406._serialized_start = 9581
    _STEERING_MOTOR_RPT_3_406._serialized_end = 9652
    _STEERING_MOTOR_RPT_2_405._serialized_start = 9654
    _STEERING_MOTOR_RPT_2_405._serialized_end = 9759
    _STEERING_MOTOR_RPT_1_404._serialized_start = 9761
    _STEERING_MOTOR_RPT_1_404._serialized_end = 9834
    _BRAKE_MOTOR_RPT_3_403._serialized_start = 9836
    _BRAKE_MOTOR_RPT_3_403._serialized_end = 9904
    _BRAKE_MOTOR_RPT_2_402._serialized_start = 9906
    _BRAKE_MOTOR_RPT_2_402._serialized_end = 10008
    _BRAKE_MOTOR_RPT_1_401._serialized_start = 10010
    _BRAKE_MOTOR_RPT_1_401._serialized_end = 10080
    _WIPER_AUX_RPT_334._serialized_start = 10083
    _WIPER_AUX_RPT_334._serialized_end = 10430
    _SHIFT_AUX_RPT_328._serialized_start = 10433
    _SHIFT_AUX_RPT_328._serialized_end = 10722
    _ACCEL_RPT_200._serialized_start = 10725
    _ACCEL_RPT_200._serialized_end = 10985
    _BRAKE_RPT_204._serialized_start = 10988
    _BRAKE_RPT_204._serialized_end = 11248
    _HORN_CMD_11C._serialized_start = 11251
    _HORN_CMD_11C._serialized_end = 11464
    _HORN_CMD_11C_HORN_CMDTYPE._serialized_start = 11415
    _HORN_CMD_11C_HORN_CMDTYPE._serialized_end = 11464
    _GLOBAL_RPT_10._serialized_start = 11467
    _GLOBAL_RPT_10._serialized_end = 12306
    _GLOBAL_RPT_10_PACMOD_SYSTEM_ENABLEDTYPE._serialized_start = 11952
    _GLOBAL_RPT_10_PACMOD_SYSTEM_ENABLEDTYPE._serialized_end = 12066
    _GLOBAL_RPT_10_PACMOD_SYSTEM_OVERRIDE_ACTIVETYPE._serialized_start = 12069
    _GLOBAL_RPT_10_PACMOD_SYSTEM_OVERRIDE_ACTIVETYPE._serialized_end = 12200
    _GLOBAL_RPT_10_BRK_CAN_TIMEOUTTYPE._serialized_start = 12202
    _GLOBAL_RPT_10_BRK_CAN_TIMEOUTTYPE._serialized_end = 12306
    _ACCEL_AUX_RPT_300._serialized_start = 12309
    _ACCEL_AUX_RPT_300._serialized_end = 12503
    _CRUISE_CONTROL_BUTTONS_RPT_208._serialized_start = 12506
    _CRUISE_CONTROL_BUTTONS_RPT_208._serialized_end = 13926
    _CRUISE_CONTROL_BUTTONS_RPT_208_OUTPUT_VALUETYPE._serialized_start = 12981
    _CRUISE_CONTROL_BUTTONS_RPT_208_OUTPUT_VALUETYPE._serialized_end = 13286
    _CRUISE_CONTROL_BUTTONS_RPT_208_MANUAL_INPUTTYPE._serialized_start = 13289
    _CRUISE_CONTROL_BUTTONS_RPT_208_MANUAL_INPUTTYPE._serialized_end = 13594
    _CRUISE_CONTROL_BUTTONS_RPT_208_COMMANDED_VALUETYPE._serialized_start = 13597
    _CRUISE_CONTROL_BUTTONS_RPT_208_COMMANDED_VALUETYPE._serialized_end = 13926
    _VEHICLE_SPEED_RPT_400._serialized_start = 13929
    _VEHICLE_SPEED_RPT_400._serialized_end = 14157
    _VEHICLE_SPEED_RPT_400_VEHICLE_SPEED_VALIDTYPE._serialized_start = 14068
    _VEHICLE_SPEED_RPT_400_VEHICLE_SPEED_VALIDTYPE._serialized_end = 14157
    _BRAKE_AUX_RPT_304._serialized_start = 14160
    _BRAKE_AUX_RPT_304._serialized_end = 14472
    _MEDIA_CONTROLS_CMD_120._serialized_start = 14475
    _MEDIA_CONTROLS_CMD_120._serialized_end = 15047
    _MEDIA_CONTROLS_CMD_120_MEDIA_CONTROLS_CMDTYPE._serialized_start = 14680
    _MEDIA_CONTROLS_CMD_120_MEDIA_CONTROLS_CMDTYPE._serialized_end = 15047
    _CRUISE_CONTROL_BUTTONS_CMD_108._serialized_start = 15050
    _CRUISE_CONTROL_BUTTONS_CMD_108._serialized_end = 15654
    _CRUISE_CONTROL_BUTTONS_CMD_108_CRUISE_CONTROL_BUTTONTYPE._serialized_start = 15277
    _CRUISE_CONTROL_BUTTONS_CMD_108_CRUISE_CONTROL_BUTTONTYPE._serialized_end = 15654
    _PARKING_BRAKE_CMD_124._serialized_start = 15657
    _PARKING_BRAKE_CMD_124._serialized_end = 15795
    _HORN_RPT_21C._serialized_start = 15798
    _HORN_RPT_21C._serialized_end = 16396
    _HORN_RPT_21C_OUTPUT_VALUETYPE._serialized_start = 16200
    _HORN_RPT_21C_OUTPUT_VALUETYPE._serialized_end = 16261
    _HORN_RPT_21C_COMMANDED_VALUETYPE._serialized_start = 16263
    _HORN_RPT_21C_COMMANDED_VALUETYPE._serialized_end = 16333
    _HORN_RPT_21C_MANUAL_INPUTTYPE._serialized_start = 16335
    _HORN_RPT_21C_MANUAL_INPUTTYPE._serialized_end = 16396
    _SHIFT_RPT_228._serialized_start = 16399
    _SHIFT_RPT_228._serialized_end = 17452
    _SHIFT_RPT_228_MANUAL_INPUTTYPE._serialized_start = 16806
    _SHIFT_RPT_228_MANUAL_INPUTTYPE._serialized_end = 17031
    _SHIFT_RPT_228_COMMANDED_VALUETYPE._serialized_start = 17034
    _SHIFT_RPT_228_COMMANDED_VALUETYPE._serialized_end = 17224
    _SHIFT_RPT_228_OUTPUT_VALUETYPE._serialized_start = 17227
    _SHIFT_RPT_228_OUTPUT_VALUETYPE._serialized_end = 17452
    _SHIFT_CMD_128._serialized_start = 17455
    _SHIFT_CMD_128._serialized_end = 17772
    _SHIFT_CMD_128_SHIFT_CMDTYPE._serialized_start = 17624
    _SHIFT_CMD_128_SHIFT_CMDTYPE._serialized_end = 17772
    _ACCEL_CMD_100._serialized_start = 17774
    _ACCEL_CMD_100._serialized_end = 17896
    _PARKING_BRAKE_RPT_224._serialized_start = 17899
    _PARKING_BRAKE_RPT_224._serialized_end = 18167
    _BRAKE_CMD_104._serialized_start = 18169
    _BRAKE_CMD_104._serialized_end = 18291
    _MEDIA_CONTROLS_RPT_220._serialized_start = 18294
    _MEDIA_CONTROLS_RPT_220._serialized_end = 19724
    _MEDIA_CONTROLS_RPT_220_OUTPUT_VALUETYPE._serialized_start = 18737
    _MEDIA_CONTROLS_RPT_220_OUTPUT_VALUETYPE._serialized_end = 19056
    _MEDIA_CONTROLS_RPT_220_COMMANDED_VALUETYPE._serialized_start = 19059
    _MEDIA_CONTROLS_RPT_220_COMMANDED_VALUETYPE._serialized_end = 19402
    _MEDIA_CONTROLS_RPT_220_MANUAL_INPUTTYPE._serialized_start = 19405
    _MEDIA_CONTROLS_RPT_220_MANUAL_INPUTTYPE._serialized_end = 19724
    _STEERING_AUX_RPT_32C._serialized_start = 19727
    _STEERING_AUX_RPT_32C._serialized_end = 19967
    _LAT_LON_HEADING_RPT_40E._serialized_start = 19970
    _LAT_LON_HEADING_RPT_40E._serialized_end = 20171
    _YAW_RATE_RPT_40D._serialized_start = 20173
    _YAW_RATE_RPT_40D._serialized_end = 20209
    _DATE_TIME_RPT_40F._serialized_start = 20212
    _DATE_TIME_RPT_40F._serialized_end = 20349
    _VIN_RPT_414._serialized_start = 20351
    _VIN_RPT_414._serialized_end = 20427
    _OCCUPANCY_RPT_415._serialized_start = 20430
    _OCCUPANCY_RPT_415._serialized_end = 20865
    _INTERIOR_LIGHTS_RPT_416._serialized_start = 20868
    _INTERIOR_LIGHTS_RPT_416._serialized_end = 21562
    _INTERIOR_LIGHTS_RPT_416_DIM_LEVELTYPE._serialized_start = 21190
    _INTERIOR_LIGHTS_RPT_416_DIM_LEVELTYPE._serialized_end = 21562
    _TURN_CMD_130._serialized_start = 21565
    _TURN_CMD_130._serialized_end = 21872
    _TURN_CMD_130_TURN_SIGNAL_CMDTYPE._serialized_start = 21744
    _TURN_CMD_130_TURN_SIGNAL_CMDTYPE._serialized_end = 21872
    _DETECTED_OBJECT_RPT_411._serialized_start = 21874
    _DETECTED_OBJECT_RPT_411._serialized_end = 21978
    _VEH_SPECIFIC_RPT_1_412._serialized_start = 21980
    _VEH_SPECIFIC_RPT_1_412._serialized_end = 22046
    _VEH_DYNAMICS_RPT_413._serialized_start = 22048
    _VEH_DYNAMICS_RPT_413._serialized_end = 22092
    _REAR_LIGHTS_RPT_418._serialized_start = 22095
    _REAR_LIGHTS_RPT_418._serialized_end = 22238
    _LEXUS._serialized_start = 22241
    _LEXUS._serialized_end = 25848