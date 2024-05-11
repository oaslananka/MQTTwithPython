# MQTT Broker Installation on Windows

This guide provides steps for installing the Mosquitto MQTT broker on Windows.

## Prerequisites
- Administrator access
- Download the Mosquitto installer from https://mosquitto.org/download/

## Installation Steps
1. **Run the installer**:
   - Execute the downloaded `.exe` file and follow the installation prompts.
2. **Add Mosquitto to your system path**:
   - During installation, select 'Add Mosquitto to PATH'.
3. **Start the Mosquitto service**:
   - Open Command Prompt as Administrator and type:
   ```cmd
   net start mosquitto
   ```

## Testing the Installation
- Open another Command Prompt window and publish a test message:
  ```cmd
  mosquitto_pub -h localhost -t test -m "Hello MQTT"
  ```
- Subscribe to the test topic:
  ```cmd
  mosquitto_sub -h localhost -t test
  ```

Mosquitto is now installed and ready on your Windows system.
