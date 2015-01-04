Keepalived
=========================

Add the following variables to the machine's host_vars/<inventory name>.yml

keepalived_priority: <priority | int>
keepalived_iface: <interface name | string>

Add the following variables to roles/keepalived/vars/main.yml

keepalived_virtual_ip: <ip address>
keepalived_password: <password | string>
keepalived_virtual_router_id: <id | int>