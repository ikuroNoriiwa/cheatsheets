# Docker Cheatsheet 

## Restart all containers 
for dc in `docker ps -q`; do echo -e "\n\nid : $dc\n\n" ; docker restart $dc; done

## Delete images startwith <start_string> 
for im in `docker images --format '{{.Repository}}'`; do  if [[ $im == <start_string>* ]];  then  docker rmi $im ; fi ; done