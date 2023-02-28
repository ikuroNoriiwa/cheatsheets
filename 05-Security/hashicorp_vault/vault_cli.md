# Vault Cli 

## authentication with vault cli using user/password method 
vault login -tls-skip-verify -method=userpass -path=userpass/ username=<USERNAME>


## Retrieve secret stored at secrets/kv/test 
On the UI, the secret is stored at secrets--> kv/test but his application real path will be kv/data/test  
```hcl
vault kv get -tls-skip-verify  -mount=kv/ -version=2 test
```