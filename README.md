**Initially intended for my personal use. You can try it if you think it might be useful to you!**

# Discord Clipboard Manager

Tired of not being able to synchronise your clipboard across devices? Look no further. With DCM, you will be able to use a private Discord server as your encrypted clipboard manager.

I had enough of using wacky techniques for sharing my clipboard from my Android device to my MacOs computer.

This Discord Clipboard Manager is a Python-based tool that securely manages your clipboard contents using cryptography with Fernet encryption. It provides seamless integration with Termux and Tasker on Android devices, as well as with Raycast and a small Bash script on macOS.

## Features

- Encrypts clipboard contents for secure storage and transmission.
- Integrates with Termux and Tasker on Android devices.
- Compatible with Raycast on macOS.

## Requirements

- Python 3.x
- Termux (for Android)
- Tasker (for Android, optional)
- Raycast (for macOS)

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/carnetdethese/discord-clipboard-manager.git
   ```

2. Install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```

3. Follow platform-specific instructions for setup:
   - **Android (Termux and Tasker):**
     - Copy the Python script to your Termux directory.
     - Configure Tasker to execute the script when desired.
   - **macOS (Raycast):**
     - Copy the Bash script to a location accessible by Raycast.
     - Configure Raycast to execute the script.

## Usage

1. Run the Python script on your desired platform.
2. Clipboard contents will be encrypted and securely managed.
3. Integration with Tasker or Raycast allows for convenient access and management of clipboard contents.

## Security

- This clipboard manager utilizes Fernet encryption to ensure the security of your clipboard data.
- Ensure that you keep your encryption key secure to prevent unauthorized access to your clipboard contents.

## Contributing

I don't plan on improving the script more than just refactoring some of the code. It is what it is.

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.
