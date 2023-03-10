# Grep Example 

## split string by '/' and get last item 
```
echo "https://cdimage.debian.org/cdimage/cloud/bullseye/latest/debian-11-genericcloud-amd64.qcow2" | grep -o '[^/]*$'
```
* -o (--only-matching) only outputs the part of the input that matches the pattern (the default is to print the entire line if it contains a match).
* [^,] is a character class that matches any character other than a comma.
* * matches the preceding pattern zero or more time, so [^,]* matches zero or more non‑comma characters.
* $ matches the end of the string.
* Putting this together, the pattern matches zero or more non-comma characters at the end of the string.
* When there are multiple possible matches, grep prefers the one that starts earliest. So the entire last field will be matched.
