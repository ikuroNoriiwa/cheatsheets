# Vault cli 

## Init vault server 
```
vault operator init -tls-skip-verify
```

## unseal vault server 
```
vault operator unseal 
```
This operation has to be done for every unseal keys


# Request Hashicorp vault with curl 


## Get connection token Using cert autentication
```
TOKEN=$(curl -s -X POST --header "X-Vault-Namespace: PATH/Namespace" --cert /path/to/file.crt --key /path/to/file.key -d '{"name":"policy"}' https://<HVAULTURL>/v1/auth/cert/login | jq -r ".auth.client_token")
```

## Get connection token using userpass authentication 
```
TOKEN=$(curl -s -X POST -d '{"password": "mathieu"}' https://192.168.56.106:8200/v1/auth/userpass/login/mathieu --noproxy '*' -k | jq -r ".auth.client_token")
```


## request specific token 
```
curl -s --request GET --header "X-Vault-Namespace: <PATH/Namespace>" --header "X-Vault-Token: ${TOKEN}" https://<HVAULTURL>/v1/secret/data/path/to/secret | jq -r '.data.data.usr'
```