# CVSS 3.0 (Common Vulnerability Scoring System)

## Score explanation 
## ![Documentation](https://www.cert-ist.com/public/fr/SO_detail?code=cvss%20v3&format=html)
## ![Nist CVSS v3 Calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)

Example : CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

## Attack Vector (AV)
Previously _Access Vector_
reflects the remoteness of the attacker relative to the vulnerable components 
### Possible Values 
N : Network 
? : Adjacent Network
L : Local 
P : Physical 

## Attack Complexity (AC)
Measure the complexity depending on conditions (hardware, software, network) that must exist in order to exploit the vulnerability 
### Possible values 
L : Low 
H : High 

## Privileges Required (PR)
consider the level of authentication required to exploit the vulnerability, rahter than the required number of authentication 
### Possible values 
N : None 
L : Low 
H : High 

## User Interaction (UI)
Indicates if the vulnerability exploitation requeires that a user must perform some action 
### Possible values 
N : None
R : Required

## Scope (S)
consider the cases where the vulnerability of a software component has an impact on resources located beyond the perimeter of this components 
Some typical cases of scope change are:
    - A vulnerability in a virtualized guest system, which has an impact on the host system.
    - A vulnerability in a software running in a sandbox , which has an impact outside this sandbox.
    - A Cross-site scripting vulnerability allowing to use a vulnerable system as a bounce, to attack another system.
### Possible values 
U : Unchanged 
C : Changed 

## Confidentiality Impact (C)
metrics related to the impact related to the vulnerability in terms ou confidentiality 
### Possible Values 
N : None 
L : Low 
H : High 

## Integrity Impact (I)
metrics related to the impact related to the vulnerability in terms of integrity
### Possible Values 
N : None 
L : Low 
H : High 

## Availability Impact (A)
metrics related to the impact related to the vulnerability in terms of avalability 
### Possible Values 
N : None 
L : Low 
H : High 


