# Terraform 

## list Workspace 
```
terraform workspace list 
```

## Create workspace 
```
terraform workspace new <WORKSPACE_NAME>
```

## Reformat Terraform code 
```
terraform fmt
```

## Apply terraform with higher log level
```
TF_LOG=TRACE terraform apply -var-file="secret.tfvars"
```

## Get output after deployment 
```
terraform output -raw <OUTPUT_NAME>
```