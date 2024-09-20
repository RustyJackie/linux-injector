#!/usr/bin/env python3
import os
import sys
import subprocess


def find_process_pid(process_name):
    """Find the PID of the process based on its name."""
    try:
        pid = subprocess.check_output(["pidof", process_name]).decode().strip()
        if pid:
            return pid.split()[0]
        else:
            print(f"Error: Process {process_name} not found.")
            sys.exit(1)
    except subprocess.CalledProcessError:
        print(f"Error: Unable to find process with name {process_name}.")
        sys.exit(1)


def inject_library(pid, library_path):
    """Inject a shared library into the target process using gdb."""
    if not os.path.isfile(library_path):
        print(f"Error: Library file {library_path} does not exist.")
        sys.exit(1)

    try:
        # Use gdb to inject the library
        gdb_command = f'sudo gdb -batch-silent -p {pid} -ex "call (void*)dlopen(\\"{library_path}\\", 2)"'
        print(f"Running: {gdb_command}")
        result = os.system(gdb_command)

        if result == 0:
            print(f"Successfully injected {library_path} into process {pid}.")
        else:
            print("Error: Injection failed.")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("Usage: sudo python3 injector.py <process_name> <path_to_library.so>")
        sys.exit(1)

    process_name = sys.argv[1]
    library_path = os.path.abspath(sys.argv[2])

    # Find the process PID
    pid = find_process_pid(process_name)

    # Inject the shared library into the process
    inject_library(pid, library_path)


if __name__ == "__main__":
    main()