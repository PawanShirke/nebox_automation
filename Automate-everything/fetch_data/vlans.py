from fetch_data import get_netbox_session

def get_vlans_by_site(site_id):
    netbox_session = get_netbox_session()
    vlans = list(netbox_session.ipam.vlans.filter(site_id=site_id))
    return vlans
