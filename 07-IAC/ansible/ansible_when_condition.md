# Ansible Using When condition 

## use when condition with vars 
```yaml
- name: 
    ...
  when: "{{ item.key }} != 'root'" # --> should not use Jinja2 template ({{}}, or {% %})
  with_items: my_var
```
Correct form :
```yaml
- name: 
    ...
  when: 'item.key | string not in "root"' # --> don't use jinja tempalte 
  with_items: my_var
```