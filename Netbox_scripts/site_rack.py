from dcim.models import Site, Rack

def create_site(name):
    site, created = Site.objects.get_or_create(
        name=name,
        defaults={'slug': name.lower().replace(' ', '-')}
    )
    return site

def create_racks(site, num_racks):
    racks = []
    for i in range(1, num_racks + 1):
        rack, created = Rack.objects.get_or_create(
            name=f"Rack {i}",
            site=site,
            defaults={'u_height': 42}
        )
        racks.append(rack)
    return racks
