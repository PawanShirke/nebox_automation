from dcim.models import Manufacturer, DeviceType, DeviceRole, Device, Interface

def create_manufacturer(name, slug):
    manufacturer, created = Manufacturer.objects.get_or_create(
        name=name,
        defaults={'slug': slug}
    )
    return manufacturer

def create_device_type(manufacturer, model, slug, u_height, part_number):
    device_type, created = DeviceType.objects.get_or_create(
        manufacturer=manufacturer,
        model=model,
        defaults={
            'slug': slug,
            'u_height': u_height,
            'part_number': part_number
        }
    )
    return device_type

def create_device_role(name, slug, color):
    device_role, created = DeviceRole.objects.get_or_create(
        name=name,
        defaults={'slug': slug, 'color': color}
    )
    return device_role

def create_device(name, device_type, device_role, site, rack):
    device, created = Device.objects.get_or_create(
        name=name,
        device_type=device_type,
        device_role=device_role,
        site=site,
        rack=rack
    )
    return device

def create_interfaces(device, port_count, port_type='10gbase-t', prefix='ge-'):
    interfaces = []
    for port in range(1, port_count + 1):
        interface_name = f"{prefix}{port}/0/0"
        interface, created = Interface.objects.get_or_create(
            device=device,
            name=interface_name,
            type=port_type
        )
        interfaces.append(interface)
    return interfaces
