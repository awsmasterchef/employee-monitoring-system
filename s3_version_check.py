import json

import boto3

from config_updater import update_configuration
from helper import read_config_file
from settings import *

s3 = boto3.client('s3', region_name=region_name, aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)


def config_checker():
    response = s3.list_object_versions(Bucket=config_bucket_name, Prefix=config_file_name)
    if 'Versions' in response:
        latest_version = response['Versions'][1]['VersionId']
        current_version = read_config_file('current_version')
        if current_version != latest_version:
            response = s3.get_object(Bucket=config_bucket_name, Key=config_file_name, VersionId=latest_version)
            content = response['Body'].read().decode('utf-8')
            updated_data = json.loads(content)
            updated_data["current_version"] = latest_version
            update_configuration(updated_data)

    else:
        print(f"No versions found")

config_checker()