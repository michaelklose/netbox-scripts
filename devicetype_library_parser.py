import csv
import os
import pathlib
import yaml


def get_list_of_files(dir_name):
    """For the given path, get the List of all files in the directory tree"""
    # create a list of file and sub directories
    # names in the given directory
    list_of_files = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    all_files.sort()
    return all_files


# PATH_DEVICETYPE_LIBRARY = "C:\\Git\\devicetype-library\\device-types\\Cisco"
PATH_DEVICETYPE_LIBRARY = "/Users/mikl/Development/devicetype-library"
OUTPUT_FILE = "devicetypes.csv"

PATH_DEVICETYPE_LIBRARY = os.path.join(PATH_DEVICETYPE_LIBRARY, 'device-types')

with open(OUTPUT_FILE, 'w', encoding="utf8") as csvfile:
    fieldnames = ['folder', 'filename', 'manufacturer', 'model', 'slug', 'part_number', 'u_height', 'is_full_depth',
                  'device_bays', 'module_bays', 'interfaces', 'mgmt_interfaces', 'console_ports', 'power_ports', 'inventory_items']
    writer = csv.DictWriter(csvfile,
                            fieldnames=fieldnames,
                            delimiter=';',
                            lineterminator='\n'
                            )
    writer.writeheader()

    files = get_list_of_files(PATH_DEVICETYPE_LIBRARY)
    for file in files:
        if file.endswith(('.yml', '.yaml')):
            with open(file, encoding="utf8") as stream:
                try:
                    yamloutput = yaml.safe_load(stream)
                    # print(yamloutput['model'])
                    device_manufacturer = yamloutput['manufacturer']
                    device_model = yamloutput['model']
                    device_slug = yamloutput['slug']
                    if "part_number" in yamloutput:
                        DEVICE_PART_NUMBER = yamloutput['part_number']
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
                        DEVICE_DEVICE_BAYS = yamloutput['device-bays']
                    else:
                        DEVICE_DEVICE_BAYS = "no"
                    if "module-bays" in yamloutput:
                        DEVICE_MODULE_BAYS = yamloutput['module-bays']
                    else:
                        DEVICE_MODULE_BAYS = "no"
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
                            if "mgmt_only" in interface and interface['mgmt_only']:
                                del interface['mgmt_only']
                                mgmt_interfaces.append(interface)
                    else:
                        DEVICE_INTERFACES = "not set"
                    if "inventory-items" in yamloutput:
                        DEVICE_INVENTORY_ITEMS = yamloutput['inventory-items']
                    else:
                        DEVICE_INVENTORY_ITEMS = "no"
                    path = pathlib.PurePath(file)
                    writer.writerow({'folder': path.parent.name,
                                     'filename': os.path.basename(file),
                                     'manufacturer': device_manufacturer,
                                     'model': device_model,
                                     'slug': device_slug,
                                     'part_number': DEVICE_PART_NUMBER,
                                     'u_height': DEVICE_U_HEIGHT,
                                     'is_full_depth': DEVICE_IS_FULL_DEPTH,
                                     'device_bays': DEVICE_DEVICE_BAYS,
                                     'module_bays': DEVICE_MODULE_BAYS,
                                     'interfaces': DEVICE_INTERFACES,
                                     'mgmt_interfaces': mgmt_interfaces,
                                     'console_ports': DEVICE_CONSOLE_PORTS,
                                     'power_ports': DEVICE_POWER_PORTS,
                                     'inventory_items': DEVICE_INVENTORY_ITEMS

                                     })
                except yaml.YAMLError as exc:
                    print(exc)
