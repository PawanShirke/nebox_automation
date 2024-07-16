from fetch_data import get_netbox_session

def get_vlans_by_site():
    netbox_session = get_netbox_session()
    vlans = list(netbox_session.ipam.vlans.all())
    return vlans
