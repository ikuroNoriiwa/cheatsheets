# Using Hashicorp Vault with ansible 

## retrieve scret password located at kv/test using user/pass authentication method 
```yaml
- name: Return all secrets from a path
    ansible.builtin.set_fact:
    my_secret: "{{ lookup('community.hashi_vault.hashi_vault', 'secret=kv/data/test auth_method=userpass username=<USERNAME> password=<PASSWORD> url=<VAULT_URL> validate_certs=False') }}"
```