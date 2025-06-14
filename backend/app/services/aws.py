import boto3

def scan_aws_secrets(access_key: str, secret_key: str, region: str):
    client = boto3.client(
        'secretsmanager',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )

    secrets = []
    paginator = client.get_paginator('list_secrets')

    for page in paginator.paginate():
        for secret in page.get('SecretList', []):
            metadata = client.describe_secret(SecretId=secret['ARN'])
            secrets.append({
                'name': secret.get('Name'),
                'arn': secret.get('ARN'),
                'last_rotated': metadata.get('LastChangedDate'),
                'created_date': secret.get('CreatedDate')
            })
    return secrets
