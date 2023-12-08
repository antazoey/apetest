from ape import accounts, compilers

CODE = """
pragma solidity >=0.4.16 <0.9.0;

contract SimpleStorage {
    uint storedData;

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
"""

container = compilers.compile_source(
   "vyper",
   CODE,
   settings={"vyper": {"version": "0.3.7"}}, 
   contractName="MyContract",
)

owner = accounts.test_accounts[0]

instance = container.deploy(sender=owner)
