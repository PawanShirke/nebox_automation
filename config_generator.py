from jinja2 import Environment, FileSystemLoader
from fetch_data.devices import get_device_by_site_and_name
from fetch_data.interfaces import get_interfaces_by_device
from fetch_data.vlans import get_vlans_by_site
from fetch_data.config_contex import get_config_context_for_bgp_neighbor_info
import argparse

# Setup Jinja2 environment with file loader
env = Environment(loader=FileSystemLoader('templates'))

def generate_config(template_name, site_name, device_name):
    devices, devices_id, site_id = get_device_by_site_and_name(site_name, device_name)
    if not devices:
        print(f"Device {device_name} in site {site_name} not found.")
        return

    hostname = devices[0] # This is avoid [AAA-RTR2]
    device_id = devices_id
    site_id = site_id
    #print(hostname)

    # Fetch VLANs data dynamically
    vlans = get_vlans_by_site()
    vlans_vid = [vlan.vid for vlan in vlans]
    #print(vlans_vid)

    # Fetch interfaces data dynamically
    interfaces = get_interfaces_by_device(device_id)

    # Separate uplink and access interfaces
    uplink_interface = next((iface for iface in interfaces if iface.description == 'UplinkInterface'), None)
    access_interfaces = [iface for iface in interfaces if iface.description == 'access_switchport']

    # Fetch BGP neighbors data dynamically
    bgp_neighbors = get_config_context_for_bgp_neighbor_info(site_name)

    # Render the template
    template = env.get_template(f'{template_name}.j2')
    config = template.render(
        hostname = hostname,
        interface = interfaces[0] if interfaces else {},
        uplink_interface = uplink_interface.name if uplink_interface else '',
        access_interfaces = access_interfaces,
        vlans_vid = vlans_vid,
        vlans = vlans,
        circuit_name = "CircuitName",  # Passing static value
        bgp_neighbors = bgp_neighbors  # Passing BGP neighbors data from config context

    )

    # Save the configuration to a file
    file_name = f"{hostname}_{template_name}.txt"
    with open(file_name, 'w') as f:
        f.write(config)

    print(f"Configuration saved to {file_name}")

def main():
    parser = argparse.ArgumentParser(description="Generate device configurations")
    parser.add_argument("device_name", help="Name of the device (e.g., XYZ-RTR1 , AAA-SWT1)")
    parser.add_argument("template_name", help="Name of the configuration template (e.g., router_interface, switch_interface, bgp)")

    args = parser.parse_args()

    device_name = args.device_name
    template_name = args.template_name

    # Derive site name from device name
    site_name = device_name.split('-')[0]

    generate_config(template_name, site_name, device_name)

if __name__ == "__main__":
    main()
