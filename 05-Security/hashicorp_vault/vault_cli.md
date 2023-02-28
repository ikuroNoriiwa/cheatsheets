# Vault Cli 

## authentication with vault cli using user/password method 
vault login -tls-skip-verify -method=userpass -path=userpass/ username=<USERNAME>


## Retrieve secret stored at secret/kv/test 
vault kv get -tls-skip-verify  -mount=kv/ -version=2 test