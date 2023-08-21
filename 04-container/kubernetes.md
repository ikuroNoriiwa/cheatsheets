# Kubernetes 

## Delete static pods 
delete yaml in /etc/kubernetes/manifest

If not present, check in kubelet services configuration (/etc/systemd/system/kubelet.d/<config_name>) if a --pod-manifest-path is present to override manifest directory 


## Filter pod by last created 
```
kubectl get pod --sort-by=.status.startTime
```

