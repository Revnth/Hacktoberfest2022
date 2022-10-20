// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./SimpleStorage.sol";
contract StorageFactory{ //class name
    SimpleStorage[] public simpleStorageArray; // an array of type SimpleStorage

    function createSimpleStorageContract() public {
        SimpleStorage simple = new SimpleStorage(); // similar to C++ -> Node* root = new Node();
        simpleStorageArray.push(simple); // push simple into array
    }

    function sfStore(uint256 _ind, uint256 _num) public { // stores a number into the contract 
        simpleStorageArray[_ind].store(_num);
    }

    function sfGet(uint256 _ind) public view returns(uint256){ // shows the number
        return simpleStorageArray[_ind].retrieve();
    }
}
