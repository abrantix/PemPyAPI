#!/usr/bin/python3

from enum import IntEnum;

class Command(IntEnum):
    
    """
    Get device information of type \ref InfoMessage.
    Can be sent as UDP broadcast to enumerate all devices within one network
    """
    INFO = 1
    
    """
    Stores the MAC address into EEPROM of the device. 
    The MAC-address according device label is already factory-programmed, so there is no need to call this method at any time by customer.
    """
    SET_MAC_ADDRESS = 2,

    """
    Error message received from device. 
    See message data for given \ref CommandError
    """
    ERROR = 3,