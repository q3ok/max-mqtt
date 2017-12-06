from maxcube.device import MaxDevice


class MaxThermostat(MaxDevice):
    def __init__(self):
        super(MaxThermostat, self).__init__()
        self.mode = None
        self.min_temperature = None
        self.max_temperature = None
        self.ActualTemperature = None
        self.TargetTemperature = None
        self.ValvePosition = None

    def device_mode_name(self):
        device_mode_names = (
            'AUTO', 'MANUAL', 'VACATION', 'BOOST'
        )
        if self.type < len(device_mode_names):
            return device_mode_names[self.mode]
        return None
