import csv
import os
import yaml

# PATH_DEVICETYPE_LIBRARY = "C:\\Git\\devicetype-library\\device-types\\Cisco"
PATH_DEVICETYPE_LIBRARY = "/Users/mikl/Development/devicetype-library/device-types/Cisco"
OUTPUT_FILE = "devicetypes.csv"

with open(OUTPUT_FILE, 'w', encoding="utf8") as csvfile:
    fieldnames = ['filename', 'model', 'slug', 'part_number', 'u_height', 'is_full_depth', 'device_bays', 'interfaces', 'mgmt_interfaces', 'console_ports', 'power_ports', ]
    writer = csv.DictWriter(csvfile,
                            fieldnames=fieldnames,
                            delimiter=';',
                            lineterminator='\n'
                            )
    writer.writeheader()

    for file in os.listdir(PATH_DEVICETYPE_LIBRARY):
        if file.endswith(('.yml', '.yaml')):
            with open(PATH_DEVICETYPE_LIBRARY + "/" + file, encoding="utf8") as stream:
                try:
                    yamloutput = yaml.safe_load(stream)
                    # print(yamloutput['model'])
                    device_model = yamloutput['model']
                    device_slug = yamloutput['slug']
                    if "part_number" in yamloutput:
                        device_part_number = yamloutput['part_number']
                    else:
                        DEVICE_PART_NUMBER = "not set"
                    if "u_height" in yamloutput:
                        DEVICE_U_HEIGHT = yamloutput['u_height']
                    else:
                        DEVICE_U_HEIGHT = "not set"
                    if "is_full_depth" in yamloutput:
                        DEVICE_IS_FULL_DEPTH = yamloutput['is_full_depth']
                    else:
                        DEVICE_IS_FULL_DEPTH = "not set"
                    if "device-bays" in yamloutput:
                        DEVICE_DEVICE_BAYS = "yes"
                    else:
                        DEVICE_DEVICE_BAYS = "no"
                    if "console-ports" in yamloutput:
                        DEVICE_CONSOLE_PORTS = yamloutput['console-ports']
                    else:
                        DEVICE_CONSOLE_PORTS = "not set"
                    if "power-ports" in yamloutput:
                        DEVICE_POWER_PORTS = yamloutput['power-ports']
                    else:
                        DEVICE_POWER_PORTS = "not set"
                    mgmt_interfaces = []
                    if "interfaces" in yamloutput:
                        DEVICE_INTERFACES = len(yamloutput['interfaces'])
                        for interface in yamloutput['interfaces']:
                            if "mgmt_only" in interface:
                                if interface['mgmt_only']:
                                    del interface['mgmt_only']
                                    mgmt_interfaces.append(interface)
                                    # print(interface)
                    else:
                        DEVICE_INTERFACES = "not set"

                    writer.writerow({'filename': file,
                                     'model': device_model,
                                     'slug': device_slug,
                                     'part_number': DEVICE_PART_NUMBER,
                                     'u_height': DEVICE_U_HEIGHT,
                                     'is_full_depth': DEVICE_IS_FULL_DEPTH,
                                     'device_bays': DEVICE_DEVICE_BAYS,
                                     'interfaces': DEVICE_INTERFACES,
                                     'mgmt_interfaces': mgmt_interfaces,
                                     'console_ports': DEVICE_CONSOLE_PORTS,
                                     'power_ports': DEVICE_POWER_PORTS

                                     })
                except yaml.YAMLError as exc:
                    print(exc)
