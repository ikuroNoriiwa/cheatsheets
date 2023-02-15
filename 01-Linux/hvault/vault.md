# Request Hashicorp vault with curl 


# Get connection token 
TOKEN=$(curl -s -X POST --header "X-Vault-Namespace: PATH/Namespace" --cert /path/to/file.crt --key /path/to/file.key -d '{"name":"policy"}' https://<HVAULTURL>/v1/auth/cert/login | jq -r ".auth.client_token")

# request specific token 
curl -s --request GET --header "X-Vault-Namespace: <PATH/Namespace>" --header "X-Vault-Token: ${TOKEN}" https://<HVAULTURL>/v1/secret/data/path/to/secret | jq -r '.data.data.usr'