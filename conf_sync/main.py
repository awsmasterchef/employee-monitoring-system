from conf_sync.iot_core_subscribe import config_change_listener
from conf_sync.s3_version_check import config_checker


def conf_sync_process():
    config_checker()
    config_change_listener()

