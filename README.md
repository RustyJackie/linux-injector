# Linux Injector Script

## Overview

This Python script allows you to inject a shared library (.so files) into any running process on a Linux system using gdb. It is designed to be generic and can be used with any process.

## Features

- Works with any running process.
- Simple injection process using gdb.

## Prerequisites

- Python 3.x
- gdb installed
- Sudo privileges

## Installation

Clone this repository and make the script executable:

```bash
git clone https://github.com/yourusername/linux-injector.git
cd linux-injector
chmod +x injector.py

## Usage

To use the injector, follow these steps:

1. **Ensure Prerequisites**: Make sure you have the necessary permissions to inject libraries into the target process. You may need to run the injector with superuser privileges.

2. **Compile the Injector**: If you are using the Python version of the injector, ensure you have Python 3 installed. For other programming languages, follow their respective compilation instructions.

3. **Run the Injector**: Use the following command to inject the library into the desired process:
   ```bash
   sudo python3 injector.py <pid> <path_to_library>
