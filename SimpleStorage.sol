// SPDX-License-Identifier: MIT
pragma solidity 0.8.8;
// pragma solidity ^0.8.8 any version above 0.8.8 is okay
// pragma solidity >=0.8.8 <0.9.0 any version above 0.8.8 but less than 0.9.0 is okay

contract SimpleStorage{
    uint256 public num = 10;

    struct People {
        uint256 n;
        string name;
    }

    People[] public people;

    function showNum(uint256 num2) public{
        num = num+num2;
        num = num*10;
    }

    function addPerson(uint256 _n, string memory _name) public{
        people.push(People(_n, _name));
    }
}
