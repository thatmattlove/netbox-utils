#!/usr/bin/env python3
import pynetbox
from netbox_config import netbox_url, netbox_token

nb = pynetbox.api(url=netbox_url,token=netbox_token)
# Ask the user for tenant information
tenant_name = input("Company Name: ")
# Input CRM unique identifer
tenant_id = input("ConnectWise Company_RecID: ")
tenant_description = str.join(" - ", (tenant_id, tenant_name))
tenant_group_search_term = input("Company Partner: ")
# Search for tenant groups by name input from above
tenant_group_search_result = nb.tenancy.tenant_groups.get(name = tenant_group_search_term)

tenant_create = nb.tenancy.tenants.create(
    name=tenant_name,
    # set slug to CRM unique identifier
    slug=tenant_id,
    # return search result for tenant group as group id
    group=tenant_group_search_result.id,
    description=tenant_description,
    comments='Automated by `mlove` python script'
)
print("Successfully added", tenant_create)
