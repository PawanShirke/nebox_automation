from fetch_data import get_netbox_session

## Option 1
""" 
def get_config_context_for_bgp_neighbor_info(site_name):
    netbox_session = get_netbox_session()
    filter = site_name+'-BGP_neighbor'  # This is to match the name as per the netbox configuration
    cf_context_get = netbox_session.extras.config_contexts.get(name=filter) #API call with get()will match only name attribute
    if not cf_context_get:
        return []

    bgp_neighbors = cf_context_get.data.get('bgp_neighbors', [])
    return bgp_neighbors """

## Option 2

def get_config_context_for_bgp_neighbor_info(site_name):
    netbox_session = get_netbox_session()
    cf_context_filter = list(netbox_session.extras.config_contexts.filter(site_name)) #API call with get()will match only name attribute
    if not cf_context_filter:
        return []

    bgp_neighbors = cf_context_filter[0].data.get('bgp_neighbors', [])
    print(bgp_neighbors)
    return bgp_neighbors
