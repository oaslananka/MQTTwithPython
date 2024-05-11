# MQTT Broker Installation on macOS

This guide explains how to install the Mosquitto MQTT broker on macOS.

## Prerequisites
- Homebrew installed (Visit https://brew.sh for installation instructions)

## Installation Steps
1. **Install Mosquitto using Homebrew**:
   ```bash
   brew install mosquitto
   ```
2. **Link and start the Mosquitto service**:
   ```bash
   brew services start mosquitto
   ```

## Testing the Installation
- Use the command below to ensure Mosquitto is running:
  ```bash
  brew services list
  ```
- Publish a test message:
  ```bash
  mosquitto_pub -h localhost -t test -m "Hello MQTT"
  ```
- Subscribe to the test topic in a new terminal:
  ```bash
  mosquitto_sub -h localhost -t test
  ```

Mosquitto is now ready to use on your macOS device!
