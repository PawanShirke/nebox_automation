from netbox_session import get_netbox_session

def get_sites(nb_session): #Gets the list of sites 
    if nb_session is not None:
        site_name = list(nb_session.dcim.sites.all())
        print(site_name)
        return site_name
    else:
        print("Failed to get NetBox session.")
        return []

def get_devices_and_ids_by_site(nb_session, site_name): #Gets the list of devices by sites
    if nb_session is not None:
        devices = list(nb_session.dcim.devices.filter(site_id=site_name))
        print(devices)
        device_ids = [device.id for device in devices]
        print(f"Here is list of devices {devices} with there device_ids {device_ids} ")
        for device, device_id in zip(devices, device_ids):
            print(f"{device.name} | {device_id}")
        
        return devices, device_ids


def get_vid_from_vlans(nb_session):
    vlans = list(nb_session.ipam.vlans.all())
    for id in vlans:
        print(id.id)
        #print(id.vid)
        print(f"Vlan name {id.name}| VID {id.vid}")
    return vlans





if __name__ == "__main__":
    nb_session = get_netbox_session()
    if nb_session is not None:
        sites = get_sites(nb_session)
        if sites:
            for site in sites:
                print(f"Devices for site {site.name} has site_id <> {site.id}")
                devices = get_devices_and_ids_by_site(nb_session, site.id)  # Pass the site ID to the function
                get_vid_from_vlans(nb_session)
                