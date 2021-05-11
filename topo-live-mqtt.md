# RTB Topo MQTT Protocol Spec (v0.1)

## MQTT Server Address

|   |   |
|:------------|:--------------------------------------------|
| Hostname        | mqtt.topo-web.com  |
| Port        | 8883 (TLS)  |
| API documentation | https://mqtt.topo-web.com/apidoc |
| Status/debugging web interface | https://mqtt.topo-web.com/debug  |


## Published topics

### topo/devices/[deviceId]/status/connected

Current device connection status.

#### Payload

| Payload        | Description                                  |
|:------------|:--------------------------------------------|
| 0        | Device is disconnected from broker     |
| 1        | Device is connected to broker    |

### topo/devices/[deviceId]/status

Collected device status, regularly updated

| MQTT flag        | value                                  |
|:------------|:--------------------------------------------|
| qos        | 0     |
| retain     | true     |

#### Payload

```javascript
{
  "last_update": 1605604726481,
  "fw_version": "V2.0.0.90",
  "voltage_main": 12.2, 
  "voltage_backup": 4.1, 
  "voltage_rtc": 3.1, 
  "temp": 31.0,
  "gps_lat": 51.753143, 
  "gps_lng": 8.669568, 
  "gps_hdop": 6.6, 
  "gps_pdop": 1.9,
  "gps_sats": 8
}
```

|  Name       |  Type |  Description | 
|:------------|:--------------------|:--------------------|
| last_update | integer | Timestamp of last status update in ms since epoch |
| fw_version | string | Firmware version of main cpu |
| voltage_main | float | Voltage of the main battery |
| voltage_backup | float | Voltage of the backup battery |
| voltage_rtc | float | Voltage of the RTC battery |
| temp | float | Board Temperature in deg celsius |
| gps_lat | float | GPS latitude in decimal degrees |
| gps_lng | float | GPS longitude in decimal degrees |
| gps_hdop | float | GPS horizontal dilution of precision |
| gps_pdop | float | GPS positional dilution of precision |
| gps_sats | integer | Number of GPS satellites used for latest measurement |



### topo/devices/[deviceId]/evt/vehicle

Vehicle detection event

| MQTT flag        | Value                                  |
|:------------|:--------------------------------------------|
| qos        | 0     |
| retain     | false     |

#### Payload
```javascript
{
  "uid": 1447240, 
  "t": 1604938229499,
  "c": 699769,
  "class": 4,
  "lane": 0,
  "dir": 0,
  "axles": 2,
  "speed": 64.0,
  "len": 7.0,
  "dist": 1.8, 
  "acc": 0, 
  "td_lane": 5600, 
  "angle": 45.0, 
  "sig_amp": 141, 
  "vol": 74
}
```

|  Name       |  Type |  Description | 
|:------------|:--------------------|:--------------------|
| uid | integer | Unique (per device) identifier of this event  |
| t | integer | Unix timestamp (in milliseconds since January 1, 1970)   |
| c | integer | Counter (incremented on each vehicle detection) |
| class | integer | RTB vehicle class code (see below) |
| lane | integer | Road lane  |
| dir | integer | Vehicle direction (0 - incoming, 1 - outgoing) |
| axles | integer | Number of vehicle axles |
| speed | float | Vehicle speed in km/h |
| len | float | Vehicle length in m |
| dist | float | Perpendicular distance from vehicle to detector in m |
| acc | float | Estimated detection accuracy in percent |
| td_lane | integer | Time delta between current and previous vehicle detection for current lane in ms |
| angle | float | Correction angle in deg |
| sig_amp | integer | Signal amplitude |
| vol | integer | Vehicle volume in dB |


### nosco/devices/[deviceId]/evt/vehicle

Nosco device family vehicle detection event

| MQTT flag        | Value                                  |
|:------------|:--------------------------------------------|
| qos        | 0     |
| retain     | false     |

#### Payload
```javascript
{
  "t": 1604938229499,
  "dir": 0,
  "c": 2,
}
```

|  Name       |  Type |  Description | 
|:------------|:--------------------|:--------------------|
| t | integer | Unix timestamp (in milliseconds since January 1, 1970)   |
| c | integer | Counter (incremented on each vehicle detection) |
| dir | integer | Vehicle direction (0 - incoming, 1 - outgoing) |

## RTB Vehicle Class Code Mappings

To support multiple worldwide classification standards, RTB uses a wide range of vehicle class codes alongside mapping tables:

### BASt TLS 8+1

| Name  |  8+1 class  |  RTB classes |
|:------------|:--------------------|:--------------------|
| Sonstige nk Kfz | 6 | 225, 230 - 234, 250, 256 |
| Krad | 10 | 235 | 
| Pkw | 7 | 1, 240 | 
| Lfw | 11 | 4 | 
| PkwA | 2  | 2, 3 |
| Lkw | 3 | 8 - 12 |
| LkwA | 8 | 32 - 69 |
| Sattel Kfz | 9 | 96 - 107 |
| Bus | 5 | 120 - 125 |

### BASt TLS 8+1 + Bicycle

| Name  |  8+1 class  |  RTB classes |
|:------------|:--------------------|:--------------------|
| Sonstige nk Kfz | 6 | 225, 250, 256 |
| Krad | 10 | 235 | 
| Pkw | 7 | 1, 240 | 
| Lfw | 11 | 4 | 
| PkwA | 2  | 2, 3 |
| Lkw | 3 | 8 - 12 |
| LkwA | 8 | 32 - 69 |
| Sattel Kfz | 9 | 96 - 107 |
| Bus | 5 | 120 - 125 |
| Bicycle | - | 230 - 234 |



