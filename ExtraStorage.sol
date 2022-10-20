// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./SimpleStorage.sol";
contract ExtraStorage is SimpleStorage{ // inheritance
    function store(uint256 _favoriteNumber) public override { // override keyword added to functions in child contract function declaration which we want to override
        favoriteNumber = _favoriteNumber + 5;
    }
}
