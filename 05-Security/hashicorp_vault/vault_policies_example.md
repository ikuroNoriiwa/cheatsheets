# Vault policy example 

## Allow userpass account to authent and change password 
```hcl
path "sys/auth" {
  capabilities = ["read"]
}
path "auth/userpass/users/*" {
  capabilities = ["list"]
}
path "auth/userpass/users/{{identity.entity.aliases.<auth_method_mountpoint>.name}}" {
  capabilities = ["read", "update"]
  allowed_parameters = {
    "password" = []
  }
}
```
Where `auth_method_mountpoint` can be retrieve with the command `vault auth list` and it is in the column accessor 
Check (official documentation)[https://developer.hashicorp.com/vault/docs/concepts/policies#parameters] 



