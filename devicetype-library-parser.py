import csv
import os
import yaml

path_devicetype_library = "C:\\Git\\devicetype-library\\device-types\\Cisco"
output_file = "devicetypes.csv"

with open(output_file, 'w') as csvfile:
    fieldnames = ['filename', 'model', 'slug', 'part_number', 'u_height', 'is_full_depth', 'device_bays', 'interfaces', 'mgmt_interfaces', 'console_ports', 'power_ports', ]
    writer = csv.DictWriter(csvfile,
                            fieldnames=fieldnames,
                            delimiter=';',
                            lineterminator='\n'
                            )
    writer.writeheader()

    for file in os.listdir(path_devicetype_library):
        if file.endswith(('.yml', '.yaml')):
            with open(path_devicetype_library + "\\" + file) as stream:
                try:
                    yamloutput = yaml.safe_load(stream)
                    # print(yamloutput['model'])
                    device_model = yamloutput['model']
                    device_slug = yamloutput['slug']
                    if "part_number" in yamloutput:
                        device_part_number = yamloutput['part_number']
                    else:
                        device_part_number = "not set"
                    if "u_height" in yamloutput:
                        device_u_height = yamloutput['u_height']
                    else:
                        device_u_height = "not set"
                    if "is_full_depth" in yamloutput:
                        device_is_full_depth = yamloutput['is_full_depth']
                    else:
                        device_is_full_depth = "not set"
                    if "device-bays" in yamloutput:
                        device_device_bays = "yes"
                    else:
                        device_device_bays = "no"
                    if "console-ports" in yamloutput:
                        device_console_ports = yamloutput['console-ports']
                    else:
                        device_console_ports = "not set"
                    if "power-ports" in yamloutput:
                        device_power_ports = yamloutput['power-ports']
                    else:
                        device_power_ports = "not set"
                    mgmt_interfaces = []
                    if "interfaces" in yamloutput:
                        device_interfaces = len(yamloutput['interfaces'])
                        for interface in yamloutput['interfaces']:
                            if "mgmt_only" in interface:
                                if interface['mgmt_only']:
                                    del interface['mgmt_only']
                                    mgmt_interfaces.append(interface)
                                    # print(interface)
                    else:
                        device_interfaces = "not set"

                    writer.writerow({'filename': file,
                                     'model': device_model,
                                     'slug': device_slug,
                                     'part_number': device_part_number,
                                     'u_height': device_u_height,
                                     'is_full_depth': device_is_full_depth,
                                     'device_bays': device_device_bays,
                                     'interfaces': device_interfaces,
                                     'mgmt_interfaces': mgmt_interfaces,
                                     'console_ports': device_console_ports,
                                     'power_ports': device_power_ports

                                     })
                except yaml.YAMLError as exc:
                    print(exc)
