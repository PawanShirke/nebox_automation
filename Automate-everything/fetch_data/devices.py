from fetch_data import get_netbox_session

def get_device_by_site_and_name(site_name, device_name):
    netbox_session = get_netbox_session()
    site = netbox_session.dcim.sites.get(name=site_name)
    site_id = site.id
    if not site:
        return None
    
    devices = list(netbox_session.dcim.devices.filter(site_id=site.id, name=device_name))
    devices_id = [device.id for device in devices]
    return devices,devices_id, site_id