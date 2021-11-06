# ipfs
Deal with ipfs to permanently store NFTs

# Install ipfs for console 
https://docs.ipfs.io/install/command-line/#linux


# Start ipfs daemon in console and let it running

```shell
ipfs daemon
```

# Python interface

You can interface with the ipfs system with python with the following functions:
```python
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


```