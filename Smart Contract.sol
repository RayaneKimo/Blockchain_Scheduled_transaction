// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyContract {


    address owner;

    event ident( bytes32  ID) ;

    struct transact {
        address payable receiver ;
        address sender;
        uint amount ;
        uint timestamp;
        bool done ;
    }


    mapping(bytes32 => transact) public tableau_transaction_remain ;
    mapping(bytes32 => transact) public tableau_transaction_done ;




    constructor() {
        owner = msg.sender;
    }

    receive() external payable {}



    function GetId (address  _dest, uint _timestamp, uint _amount , address _sender) public pure returns(bytes32){
        return keccak256(abi.encode(_dest, _timestamp, _amount, _sender)) ;
    }



    function ScheduleTo (address payable _dest, uint _timestamp) public payable {
        bytes32 ID =GetId(_dest,_timestamp,msg.value, msg.sender);
        tableau_transaction_remain[ID]= transact(_dest, msg.sender, msg.value,_timestamp, false) ;
        emit ident(ID)  ;
    }

    function SendWhenTime ( bytes32 ID ) payable public{

        address payable _dest = tableau_transaction_remain[ID].receiver;
        uint _timestamp = tableau_transaction_remain[ID].timestamp;
        uint amount = tableau_transaction_remain[ID].amount ;


        require(tableau_transaction_remain[ID].done == false , "not listed");
        require(block.timestamp > _timestamp, "you can't send now !");


        _dest.transfer(amount);

        tableau_transaction_remain[ID].done = true ;

        tableau_transaction_done[ID] = tableau_transaction_remain[ID] ;

        delete tableau_transaction_remain[ID];


    }


    function time() public view returns(uint) {
        return block.timestamp ;
    }




}

