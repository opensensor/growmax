import config  # User's config file


def get_config_value(key, default=None):
    if hasattr(config, key):
        return getattr(config, key)
    return default


def get_moisture_threshold_for_position(position):
    if isinstance(config.SOIL_WET_THRESHOLD, int):
        return config.SOIL_WET_THRESHOLD
    else:
        return config.SOIL_WET_THRESHOLD[position]
