# scratching-evm

## TODOs

### Opcodes (opcodes.py)
- [ ] Add memory expansion cost to SHA3 dynamic gas calculation (line 250)
- [ ] Implement warm/cold address tracking for EXTCODECOPY (line 355)
- [ ] Fix MSTORE to be right-aligned (line 413)
- [ ] Implement gas refunds for SSTORE (line 459)

### Log Operations (log.py)
- [ ] Add memory expansion cost to LOG0 gas calculation (line 29)
- [ ] Add memory expansion cost to LOG1 gas calculation (line 40)
- [ ] Add memory expansion cost to LOG2 gas calculation (line 51)
- [ ] Add memory expansion cost to LOG3 gas calculation (line 64)
- [ ] Add memory expansion cost to LOG4 gas calculation (line 78)

### Unimplemented Opcodes
The following opcodes are stubbed and raise NotImplementedError:
- [ ] NUMBER - Block number
- [ ] DIFFICULTY - Block difficulty
- [ ] GASLIMIT - Gas limit
- [ ] CHAINID - Chain ID
- [ ] SELFBALANCE - Self balance
- [ ] BASEFEE - Base fee
- [ ] CREATE - Create contract
- [ ] CALL - Call another contract
- [ ] CALLCODE - Call code
- [ ] RETURN - Return from contract
- [ ] DELEGATECALL - Delegate call
- [ ] CREATE2 - Create contract with deterministic address
- [ ] STATICCALL - Static call
- [ ] INVALID - Invalid opcode
- [ ] SELFDESTRUCT - Self destruct contract
