from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

def scan_azure_secrets(tenant_id: str, client_id: str, client_secret: str, vault_url: str):
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    client = SecretClient(vault_url=vault_url, credential=credential)

    secrets = []
    for secret_prop in client.list_properties_of_secrets():
        metadata = client.get_secret(secret_prop.name)
        secrets.append({
            'name': secret_prop.name,
            'created_on': secret_prop.created_on,
            'updated_on': secret_prop.updated_on,
            'enabled': secret_prop.enabled
        })
    return secrets
