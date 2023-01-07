
# User's config file
import config


def get_moisture_threshold_for_position(position):
    if isinstance(config.SOIL_WET_THRESHOLD, int):
        return config.SOIL_WET_THRESHOLD
    else:
        return config.SOIL_WET_THRESHOLD[position]
