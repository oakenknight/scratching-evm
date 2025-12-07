# evmstate.py
from memory import Memory
from storage import Storage
from stack import Stack

class State:
    def __init__(self,
                 sender,
                 program,
                 gas,
                 value,
                 calldata=[]):
        self.pc      = 0
        
        self.stack   = Stack()
        self.memory  = Memory()
        self.storage = Storage()
        
        self.sender   = sender
        self.program  = program
        self.gas      = gas
        self.value    = value
        self.calldata = calldata
        
        self.stop_flag   = False
        self.revert_flag = False
        
        self.returndata = []
        self.logs       = []