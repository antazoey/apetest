Test repo to show how eth-ape faults on my computer.

### Environment information

- OS: macOS / arm64
- Python Version: 3.11.4
- `ape` and plugin versions:

```sh
$ ape --version
0.6.27

$ ape plugins list
Installed Plugins
  ens          0.6.2
  etherscan    0.6.10
  ganache      0.6.9
  hardhat      0.6.13
  solidity     0.6.0
```

- Contents of your `ape-config.yaml` (NOTE: do not post anything private like RPC urls or secrets!):

```sh
$ cat ape-config.yaml
name: sismondi_nft

contracts-folder: "contracts"

plugins:
  - name: solidity
    version: 0.6.0
  - name: hardhat
  - name: ens
  - name: etherscan
    version: ">=0.6.2,<0.7"
  - name: ape-ganache

dependencies:
  - OpenZeppelin/openzeppelin-contracts@4.4.1
```

### What went wrong?

I installed a new environment using devbox with the following configuration:

```
$ cat devbox.json
{
  "packages": [
    "git@latest",
    "which@latest",
    "nodePackages.ganache-cli@latest",
    "cmake@latest",
    "nodejs@latest",
    "solc@latest",
    "vim@latest",
    "python311Packages.pip@latest",
    "python311@latest"
  ],
  "shell": {
    "init_hook": [
      ". $VENV_DIR/bin/activate"
    ],
  }
}
```

And I'm running it like this:

```
$ devbox shell --pure
$ pip install eth-ape
$ ape plugins install .
$ ape compile .
Segmentation fault: 11
```
