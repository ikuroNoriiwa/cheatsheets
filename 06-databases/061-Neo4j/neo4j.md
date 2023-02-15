
## Importer un fichier CSV du dossier import, en créant un node par asset
LOAD CSV WITH HEADERS FROM"file:///csvfilename.csv" as row FIELDTERMINATOR ';'
CREATE  (:Asset {name: row.HOSTNAME, os: row.OS})
RETURN row;


## Renvoyer tous les nodes précédemment créé commencant par
MATCH (n:Asset) WHERE n.name STARTS WITH "startServerName"
RETURN n LIMIT 25

## Importer le csv et construire les premières relations
LOAD CSV WITH HEADERS FROM"file:///csvfilename.csv" as row FIELDTERMINATOR ';'
MERGE (host:Asset {name: row.HOSTNAME, os_assetdb: row.OS_ASSETDB, os_aesio: row.OS_AESIO, env: row.ENVIRONNEMENT, etat: row.ETAT_HOSTNAME, ip: row.IP})
MERGE (u:Upm {name: row.CENTRE_OPERANT})
MERGE (ap:App {code_ap: row.APPLICATIONS, lib: row.LIBELLE_APP, lib_long: row.LIBELLE_LONG})
MERGE (n2:Datacenter {name: row.LOCALISATION_NIV_2})
MERGE (n3:Salle {name: row.LOCALISATION_NIV_3})
MERGE (empl:Emplacement {name: row.EMPLACEMENT_GRID_NO})

MERGE (n2)-[:SALLE]->(n3)
MERGE (n3)-[:EMPLACEMENT]->(empl)
MERGE (empl)-[:HEBERGE]->(host)
MERGE (u)-[:OPERE]->(host)
MERGE (host)-[:POSSEDE_APP]->(ap)

RETURN row;

## Chercher le lien d'un code APP jusqu'au datacenter
MATCH (host:Asset)-[:POSSEDE_APP]-(ap:App) WHERE ap.code_ap = "code_ap" MATCH (host:Asset)-[:HEBERGE]-(empl:Emplacement)-[:EMPLACEMENT]-(s:Salle)-[:SALLE]-(dc:Datacenter) RETURN host,empl,s, dc, ap

## Double condition
MATCH (host:Asset)-[:POSSEDE_APP]-(ap:App) WHERE ap.code_ap = "" AND host.env = "PRODUCTION"
MATCH (host:Asset)-[:HEBERGE]-(empl:Emplacement)-[:EMPLACEMENT]-(s:Salle)-[:SALLE]-(dc:Datacenter)

RETURN host,empl,s, dc, ap



## Add databases
LOAD CSV WITH HEADERS FROM"file:///csvfilename.csv" as row FIELDTERMINATOR ';'
MATCH (host:Asset) WHERE host.name = row.HOSTNAME
CREATE (db:Middleware {type: row.TYPE, instance: row.INSTANCE, version: row.VO, score:row.SCORE})
MERGE (host)-[:DATABASE]->(db)
RETURN host, db


## Add CFT
LOAD CSV WITH HEADERS FROM"file:///csvfilename.csv" as row FIELDTERMINATOR ';'
MATCH (host:Asset) WHERE host.name = row.HOSTNAME
CREATE (cft:Middleware {type: "CFT", version: row.VERSION_CFT, score:row.SCORE})
MERGE (host)-[:CFT]->(cft)
RETURN host, cft

## MATCH Optionnal match
MATCH (host:Asset)-[:POSSEDE_APP]-(ap:App) WHERE ap.code_ap = "code_ap"
MATCH (host:Asset)-[:HEBERGE]-(empl:Emplacement)-[:EMPLACEMENT]-(s:Salle)-[:SALLE]-(dc:Datacenter)
OPTIONAL MATCH (host:Asset)-[:DATABASE]-(db:Middleware)
OPTIONAL MATCH (host:Asset)-[:CFT]-(cft:Middleware)
RETURN host,empl,s, dc, ap, db, cft

## APP info
LOAD CSV WITH HEADERS FROM"file:///csvfilename.csv" as row FIELDTERMINATOR ";"
MATCH (ap:App) WHERE ap.code_ap = row.CODE_AP
SET ap.responsable = row.RESP_MOE, ap.dpp = row.DPP, ap.continuity_level = row.CONTINUITY_LEVEL_LIBELLE, ap.confidentialite = row.CONFIDENTIALITE_LIBELLE, ap.criticite = row.CRITICITE_METIER_LIBELLE
RETURN ap


## Condiotionnal merge
MATCH (n:App) WHERE n.code_ap = "code_ap"
MERGE (n)-[:TEST]->(u:Responsable {name: "Nom", uid: "uid"})
WITH count(n) as nodesAltered
WHERE nodesAltered = 0
RETURN nodesAltered


## Search
MATCH (ap:App)<-[:HEBERGE]-(host:Asset)<-[:HEBERGE]-(empl:Emplacement)<-[:EMPLACEMENT]-(s:Salle)-[:SALLE]-(dc:Datacenter) WHERE ap.code_ap = "code_ap" AND host.env = "QUALIFICATION"
OPTIONAL MATCH (ap)<-[:OWN]-(pr:EntiteProd)
OPTIONAL MATCH (ap)<-[:OWN]-(moe:EntiteMOE)
OPTIONAL MATCH (ap)<-[:OWN]-(res:Responsable)
OPTIONAL MATCH (pr2:EntiteProd)<-[:WORK_IN]-(res)
OPTIONAL MATCH (moe2:EntiteMOE)<-[:WORK_IN]-(res)
OPTIONAL MATCH (host)-[:DATABASE]->(db:Middleware)
OPTIONAL MATCH (host)-[:ILLUMIO_NAME]->(label:Label)
RETURN ap, host, empl, s, dc, pr, moe, res, pr2, moe2, db, label


## Search asset with CFT and DB and link to AP
MATCH (host:Asset)-[:DATABASE]->(db:Middleware)
MATCH (host)-[:CFT]->(cft:Middleware)
MATCH (ap:App)<-[:HEBERGE]-(host)
RETURN host, cft,db, ap


## CHECK duplicates hostnames
MATCH (n:Asset)
WITH n.name as name, collect(n) as nodes
WHERE size(nodes) > 1
RETURN [ nn in nodes | {name: nn.name,ip: size((nn)--())}] AS ids, size(nodes)
ORDER BY size(nodes) DESC


## DELETE DUPlicates
MATCH (n:Asset)
WITH n.name as name, collect(n) as nodes
WHERE size(nodes) > 1
UNWIND nodes[1..] as t
DETACH DELETE t



MATCH (host:Asset)-[]-(mid:Middleware) WHERE mid.type = "WAS"
MATCH (lab:Label)-[]-(host)
RETURN host.name, mid.type, mid.version, lab.label_middleware
ORDER BY mid.version


MATCH (mid:Middleware) WHERE mid.type = "WAS" AND mid.version CONTAINS "8.5.5"
MATCH (mid)-[]-(host:Asset)
OPTIONAL MATCH (host)-[]->(app:App)
OPTIONAL MATCH (app)-[]-(res:Responsable)
RETURN host, app, mid, res

MATCH (ap:App)<-[:HEBERGE]-(host:Asset)<-[:HEBERGE]-(empl:Emplacement)<-[:EMPLACEMENT]-(s:Salle)-[:SALLE]-(dc:Datacenter) WHERE ap.code_ap = "code_ap" AND host.env = "QUALIFICATION"
OPTIONAL MATCH (ap)<-[:OWN]-(pr:EntiteProd)
OPTIONAL MATCH (ap)<-[:OWN]-(moe:EntiteMOE)
OPTIONAL MATCH (ap)<-[:OWN]-(res:Responsable)
OPTIONAL MATCH (pr2:EntiteProd)<-[:WORK_IN]-(res)
OPTIONAL MATCH (moe2:EntiteMOE)<-[:WORK_IN]-(res)
OPTIONAL MATCH (host)-[:DATABASE]->(db:Middleware)
OPTIONAL MATCH (host)-[:ILLUMIO_NAME]->(label:Label)
OPTIONAL MATCH (host)-[]-(mid:Middleware)
OPTIONAL MATCH (ap)<-[]-(ch:Change)
OPTIONAL MATCH (host)-[]-(p:Pool)-[]-(vip:Vip)-[]-(lb:LoadBalancer)
RETURN ap, host, empl, s, dc, pr, moe, res, pr2, moe2, db, label, ch, mid, p, vip, lb

MATCH (host:Asset) WHERE host.score_global < "3.0"
MATCH (host)-[]-(ap:App)
MATCH (ap)-[]-(re:Responsable)
RETURN host, ap, re

MATCH (ap:App)-[]-(ch:Change)
WHERE ap.code_ap = "code_ap"
RETURN ap, ch

MATCH (host:Asset) WHERE host.score_global = "3,5"
MATCH (host)-[]-(ap:App)
MATCH (ap)-[]-(re:Responsable)
RETURN host, ap, re


-----------------------------------------------------------------

LOAD CSV WITH HEADERS FROM"file:///csvfilename.csv" as row FIELDTERMINATOR ''
CREATE  (row._labels {env: row.env, etat: row.etat, ip: row.ip, label_status: row.label_status, name:row.name, os_aesio: row.os, os: row.os, score_global: row.score_global, row.score_materiel: row.score_materiel})
RETURN row;




LOAD CSV WITH HEADERS FROM "file:///csvfilename.csv" as row FIELDTERMINATOR ';'
MATCH (host:Asset) WHERE host.ip = row.`IP SERVER`
SET host.vip_port_open = row.`PORT SERVER`
MERGE (lbp:LoadBalancer {lb_name: row.`LB PRIMARY`, lb_tag: "Primary"})
FOREACH(ignoreMe IN CASE WHEN row.`LB SECONDARY` IS NOT NULL THEN [1] ELSE [] END |
	MERGE (lbs:LoadBalancer {lb_name: row.`LB SECONDARY`, lb_tag: "Secondary"})
    MERGE (lbp)<-[:BACKUP]-(lbs))
MERGE (v:Vip { vs_name: row.`VS NAME`, vip_ip: row.VIP, vs_state: row.`VS STATE`, vs_availability: row.`VS Availability`, vs_port: row.`VS PORT`})
SET v.dns = row.`VIP DNS`
MERGE (p:Pool {pool_name: row.`POOL NAME`})
SET p.monitor_server = row.`MONITOR SERVER`
