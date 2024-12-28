"""
Given root directory find the total sizes for the files in the sub-directories.
"""
from pathlib import Path

def get_subdirectory_sizes(root_dir):
    """
    Calculate the total sizes of files in each subdirectory of the root directory using pathlib.

    :param root_dir: Path to the root directory as a string.
    :return: Dictionary mapping subdirectory paths to their total file sizes in bytes.
    """
    root_path = Path(root_dir)
    if not root_path.is_dir():
        raise ValueError(f"{root_dir} is not a valid directory")

    subdir_sizes = {}

    # Iterate through all subdirectories and files
    for subdir in root_path.rglob("*"):
        if subdir.is_dir():
            # Compute total size for this subdirectory
            total_size = sum(f.stat().st_size for f in subdir.rglob("*") if f.is_file())
            subdir_sizes[subdir] = total_size

    return subdir_sizes

# Example usage
root_directory = "/path/to/root/directory"  # Replace with the actual root directory path
sizes = get_subdirectory_sizes(root_directory)

# Print sizes
for subdir, size in sizes.items():
    print(f"{subdir}: {size / (1024**2):.2f} MB")  # Size in MB


# USING OS

import os

def get_subdirectory_sizes(root_dir):
    """
    Calculate the total sizes of files in each subdirectory of the root directory.

    :param root_dir: Path to the root directory.
    :return: Dictionary mapping subdirectory paths to their total file sizes in bytes.
    """
    subdir_sizes = {}

    # Walk through each directory and its subdirectories
    for subdir, _, files in os.walk(root_dir):
        total_size = 0
        for file in files:
            file_path = os.path.join(subdir, file)
            try:
                # Accumulate the file sizes
                total_size += os.path.getsize(file_path)
            except (OSError, FileNotFoundError):
                # Handle files that cannot be accessed
                print(f"Warning: Could not access file {file_path}")
        subdir_sizes[subdir] = total_size

    return subdir_sizes

# Example usage
root_directory = "/path/to/root/directory"  # Replace with the actual root directory path
sizes = get_subdirectory_sizes(root_directory)

# Print sizes
for subdir, size in sizes.items():
    print(f"{subdir}: {size / (1024**2):.2f} MB")  # Size in MB