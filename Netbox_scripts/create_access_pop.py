from extras.scripts import Script, StringVar, IntegerVar
from .site_rack import create_site, create_racks
from .devices import create_manufacturer, create_device_type, create_device_role
from .device_setup import setup_devices_and_cabling

class CreateAccessPop(Script):
    class Meta:
        name = "Create Access POP"
        description = "Creates a site, devices, rack elevation, and cabling matrix for an Access POP."

    site_name = StringVar(
        description="Enter the name of the new site"
    )
    num_racks = IntegerVar(
        description="Enter the number of racks"
    )

    def run(self, data, commit=True):
        site_name = data['site_name']
        num_racks = data['num_racks']

        # Create the site
        site = create_site(site_name)
        self.log_success(f"Site '{site_name}' created or already exists.")

        # Create manufacturer Cisco
        manufacturer = create_manufacturer('Cisco', 'cisco')

        # Create device types
        router_type = create_device_type(manufacturer, 'ASR920', 'asr920', 1, 'ASR920')
        switch_type = create_device_type(manufacturer, 'Nexus 3200', 'nexus-3200', 1, 'Nexus 3200')

        # Create device roles
        router_role = create_device_role('Access POP Router', 'access-pop-router', 'ff0000')
        switch_role = create_device_role('Access POP Switch', 'access-pop-switch', '00ff00')

        # Create racks
        racks = create_racks(site, num_racks)
        self.log_success(f"{num_racks} racks created successfully in site '{site_name}'.")

        # Setup devices and cabling
        setup_devices_and_cabling(site, racks, site_name, router_type, router_role, switch_type, switch_role)
        self.log_success("Devices and cabling setup complete for Access POP.")
