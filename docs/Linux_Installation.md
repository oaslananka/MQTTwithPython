# MQTT Broker Installation on Linux

This guide covers the installation of the Mosquitto MQTT broker on Linux operating systems.

## Prerequisites
- Access to a terminal
- sudo privileges

## Installation Steps
1. **Update your package list**:
   ```bash
   sudo apt-get update
   ```
2. **Install Mosquitto**:
   ```bash
   sudo apt-get install mosquitto mosquitto-clients
   ```
3. **Start and enable the Mosquitto service**:
   ```bash
   sudo systemctl start mosquitto
   sudo systemctl enable mosquitto
   ```

## Testing the Installation
- Use the command below to check if Mosquitto is active:
  ```bash
  sudo systemctl status mosquitto
  ```
- Publish a test message:
  ```bash
  mosquitto_pub -h localhost -t test -m "Hello MQTT"
  ```
- Subscribe to the test topic in a new terminal:
  ```bash
  mosquitto_sub -h localhost -t test
  ```

Congratulations! You have successfully installed Mosquitto on your Linux system.
