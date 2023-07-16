""" Export all NetBox devices to CSV """

import csv
import pynetbox
import config

OUTPUT = "devices.csv"

nb = pynetbox.api(url=config.url, token=config.token)

devices = nb.dcim.devices.all()

with open(OUTPUT, "w", encoding="utf-8", newline="") as csvfile:
    fields = [
        "id",
        "name",
        "status",
        "device_role",
        "device_manufacturer",
        "device_type",
        "platform",
        "description",
        "serial",
        "asset_tag",
        "tenant",
        "site",
        "location",
        "rack",
        "position",
        "face",
        "created",
        "last_updated",
        "comments",
        "tags",
        "url",
        "airflow",
        "primary_ip",
        "primary_ip4",
        "primary_ip6",
        "cluster",
        "virtual_chassis",
        "vc_position",
        "vc_priority",
        "custom_fields",
        "config_context",
        "config_template",
        "parent_device",
    ]
    export = csv.DictWriter(
        csvfile, delimiter=";", quoting=csv.QUOTE_MINIMAL, fieldnames=fields
    )
    export.writeheader()

    for device in devices:
        export.writerow(
            {
                "id": device.id,
                "name": device.name,
                "status": device.status.value,
                "tenant": device.tenant,
                "site": device.site,
                "location": device.location,
                "rack": device.rack,
                "position": device.position,
                "face": device.face,
                "device_role": device.device_role,
                "device_manufacturer": device.device_type.manufacturer,
                "device_type": device.device_type,
                "platform": device.platform,
                "serial": device.serial,
                "asset_tag": device.asset_tag,
                "created": device.created,
                "last_updated": device.last_updated,
                "airflow": device.airflow,
                "description": device.description,
                "comments": (device.comments).replace("\r\n", "\\r\\n"),
                "tags": device.tags,
                "url": device.url,
                "primary_ip": device.primary_ip,
                "primary_ip4": device.primary_ip4,
                "primary_ip6": device.primary_ip6,
                "cluster": device.cluster,
                "virtual_chassis": device.virtual_chassis,
                "vc_position": device.vc_position,
                "vc_priority": device.vc_priority,
                "custom_fields": device.custom_fields,
                "config_context": device.config_context,
                "config_template": device.config_template,
                "parent_device": device.parent_device,
            }
        )
