import pynetbox
import config

nb = pynetbox.api(url=config.url, token=config.token)

# Create RIRs
rirs = list()
rirs.append(dict(name="RFC 1918", slug="rfc-1918", is_private="true"))
rirs.append(dict(name="AFRINIC", slug="afrinic"))
rirs.append(dict(name="APNIC", slug="apnic"))
rirs.append(dict(name="ARIN", slug="arin"))
rirs.append(dict(name="LACNIC", slug="lacnic"))
rirs.append(dict(name="RIPE", slug="ripe"))

try:
    result = nb.ipam.rirs.create(rirs)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get RIR ID
rir_rfc1918 = nb.ipam.rirs.get(slug="rfc-1918")

# Create RFC 1918 aggregates
aggregates = list()
aggregates.append(dict(prefix="10.0.0.0/8", rir=rir_rfc1918.id))
aggregates.append(dict(prefix="172.16.0.0/12", rir=rir_rfc1918.id))
aggregates.append(dict(prefix="192.168.0.0/16", rir=rir_rfc1918.id))

try:
    result = nb.ipam.aggregates.create(aggregates)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Create Regions
regions = list()
regions.append(dict(name="EMEA", slug="emea"))
regions.append(dict(name="NA", slug="na"))
regions.append(dict(name="SA", slug="sa"))

try:
    result = nb.dcim.regions.create(regions)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get Region ID
region_emea = nb.dcim.regions.get(slug="emea")

# Create Countries
countries = list()
countries.append(dict(name="DE", slug="de", parent=region_emea.id))
countries.append(dict(name="FR", slug="fr", parent=region_emea.id))

try:
    result = nb.dcim.regions.create(countries)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get Country ID
country_de = nb.dcim.regions.get(slug="de")

# Create Site
sites = list()
sites.append(dict(name="DE-Musterstadt-1", slug="de-musterstadt-1", region=country_de.id))

try:
    result = nb.dcim.sites.create(sites)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get Site ID
site_musterstadt = nb.dcim.sites.get(slug="de-musterstadt-1")

# Create Racks
racks = list()
racks.append(dict(name="Rack1", site=site_musterstadt.id))
racks.append(dict(name="Rack2", site=site_musterstadt.id))

try:
    result = nb.dcim.racks.create(racks)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get Rack IDs
rack1 = nb.dcim.racks.get(name="Rack1", site_id=site_musterstadt.id)
rack2 = nb.dcim.racks.get(name="Rack2", site_id=site_musterstadt.id)

# Create Manufactures
manufacturers = list()
manufacturers.append(dict(name="Cisco", slug="cisco"))

try:
    result = nb.dcim.manufacturers.create(manufacturers)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get Manufacture ID
manufacturer_cisco = nb.dcim.manufacturers.get(slug="cisco")

# Create Platforms
platforms = list()
platforms.append(dict(name="IOS", slug="ios", manufacturer=manufacturer_cisco.id, napalm_driver="ios"))
platforms.append(dict(name="IOS XE", slug="iosxe", manufacturer=manufacturer_cisco.id, napalm_driver="ios"))
platforms.append(dict(name="NX-OS", slug="nxos", manufacturer=manufacturer_cisco.id, napalm_driver="nxos_ssh"))

try:
    result = nb.dcim.platforms.create(platforms)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Create Device Roles
device_roles = list()
device_roles.append(dict(name="Core", slug="core"))
device_roles.append(dict(name="Distribution", slug="distribution"))
device_roles.append(dict(name="Access", slug="access"))

try:
    result = nb.dcim.device_roles.create(device_roles)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get Device Roles
device_role_core = nb.dcim.device_roles.get(slug="core")
device_role_distribution = nb.dcim.device_roles.get(slug="distribution")
device_role_access = nb.dcim.device_roles.get(slug="access")

# Create Device Types
device_types = list()
device_types.append(dict(model="C9500-32C", manufacturer=manufacturer_cisco.id, slug="c9500-32c", u_height=1))
device_types.append(dict(model="C9500-48Y4C", manufacturer=manufacturer_cisco.id, slug="c9500-48y4c", u_height=1))
device_types.append(dict(model="C9300-48P", manufacturer=manufacturer_cisco.id, slug="c9300-48p", u_height=1))

try:
    result = nb.dcim.device_types.create(device_types)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Get Device Types IDs
device_type_core = nb.dcim.device_types.get(slug="c9500-32c")
device_type_distribution = nb.dcim.device_types.get(slug="c9500-48y4c")
device_type_access = nb.dcim.device_types.get(slug="c9300-48p")

# Create Device
devices = list()
devices.append(dict(name="Core1", device_type=device_type_core.id, device_role=device_role_core.id, site=site_musterstadt.id, rack=rack1.id, position=40, face="front"))
devices.append(dict(name="Core2", device_type=device_type_core.id, device_role=device_role_core.id, site=site_musterstadt.id, rack=rack2.id, position=40, face="front"))

try:
    result = nb.dcim.devices.create(devices)

except pynetbox.core.query.RequestError as e:
    print(e.error)

# Add Prefixes
prefixes = list()
prefixes.append(dict(prefix="10.1.0.0/16", site=site_musterstadt.id))
prefixes.append(dict(prefix="10.1.1.0/24", site=site_musterstadt.id))
prefixes.append(dict(prefix="10.1.2.0/24", site=site_musterstadt.id))
prefixes.append(dict(prefix="1.2.3.0/27", site=site_musterstadt.id))

try:
    result = nb.ipam.prefixes.create(prefixes)

except pynetbox.core.query.RequestError as e:
    print(e.error)
