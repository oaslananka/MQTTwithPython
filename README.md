# MQTT Setup Project

This project provides detailed documentation and scripts for setting up and configuring an MQTT broker across various operating systems. The repository is designed to help with quick setup and troubleshooting of MQTT environments.

## Documentation
- Windows: `docs/Windows_Installation.md`
- macOS: `docs/macOS_Installation.md`
- Linux: `docs/Linux_Installation.md`
- Configuration: `docs/General_Configuration_Guide.md`

## Scripts
- MQTT Sender: `src/python/mqtt_client_publish.py`
- MQTT Listener : `src/python/mqtt_client.py`

## Sample usage 
- MQTT Sender : `python src/python/mqtt_client_publish.py --broker <broker_address> --port <broker_port> --topic "sensor/data" --message "Hello MQTT" --username "user" --password "pass"`
- MQTT Listener: `python src/python/mqtt_client.py --broker <broker_address> --port <broker_port> --topic "sensor/data" --username "user" --password "pass"`

  
## Author
- Osman ASLAN

## GitHub
- [oaslananka](https://github.com/oaslananka)
