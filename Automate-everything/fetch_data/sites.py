from fetch_data import get_netbox_session

def get_site(site_name):
    netbox_session = get_netbox_session()
    site = netbox_session.dcim.sites.get(name=site_name)
    return site
