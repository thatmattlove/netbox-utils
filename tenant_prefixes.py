#!/usr/bin/env python3
import sys
import pynetbox
from netbox_config import netbox_url, netbox_token

nb = pynetbox.api(url=netbox_url,token=netbox_token)

# Get Tenant ID from command-line argument, assign variable
tenant_id = str(sys.argv[1])
# Get Prefix Role from command-line argument, assign variable
prefix_role = str(sys.argv[2])
# Query Netbox for prefixes assigned to tenant matching role
prefix_search = nb.ipam.prefixes.filter(tenant=tenant_id, role=prefix_role)
# Index results
prefix_result = prefix_search[0]
# Format Output
fmt = "{:<30}{:<20}{:<10}{:<10}{:<40}"
header = ("Tenant", "Prefix Status", "Site", "Protocol", "Prefix")
# Print Output in pretty-ish table
print(fmt.format(*header))
for key in prefix_search:
    val = key
    print(
    fmt.format(
        val.tenant.name,
        str(val.status),
        str(val.site),
        str(val.family),
        str(val),
    )
)
