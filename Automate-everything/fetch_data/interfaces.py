from fetch_data import get_netbox_session

def get_interfaces_by_device(device_id):
    netbox_session = get_netbox_session()
    interfaces = list(netbox_session.dcim.interfaces.filter(device_id=device_id))
    return interfaces
