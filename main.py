from pathlib import Path
from subprocess import run


def add_file(file_name):
    filepath = Path(file_name).resolve()
    command = ["ipfs", "add", "-Q", filepath]

    result = run(command, capture_output=True, text=True)

    ipfs_hash = result.stdout.strip()

    return {ipfs_hash: filepath}


def find_file_locations(ipfs_hash):
    command = ["ipfs", "dht", "findprovs", ipfs_hash]
    result = run(command, capture_output=True, text=True)
    ipfs_hash = result.stdout.strip()
    return ipfs_hash


if __name__ == '__main__':
    example_file_name = "hello"
    file_added = add_file(example_file_name)
    ipfs_hash_val, file_path = [(k, v) for k, v in file_added.items()][0]
    file_added = find_file_locations(ipfs_hash_val)
    file_added.splitlines()
