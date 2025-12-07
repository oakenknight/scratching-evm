# scratching-evm

A minimal Ethereum Virtual Machine implementation in Python for learning purposes. Supports basic EVM opcodes including arithmetic, logic, stack operations, memory, storage, and jumps with gas metering.

## Quick Start

```bash
python main.py
```

Runs a collection of simple bytecode programs and displays execution results:

- **SIMPLE_ADD**: `PUSH1 0x42, PUSH1 0xFF, ADD` → Adds 66 + 255 = 321
- **SIMPLE_PUSH**: `PUSH1 0x42` → Pushes 66 onto stack
- **MUL_BY_ZERO**: `PUSH1 0x42, PUSH1 0x00, MUL` → 66 × 0 = 0
- **SIMPLE_MUL**: `PUSH1 0x14, PUSH1 0x0A, MUL` → 20 × 10 = 200
- **EXP_OVERFLOW**: `PUSH1 0xFF, PUSH1 0x02, EXP` → 2^255 mod 2^256 (overflow test)
- **SDIV_ZERO**: `PUSH1 0x00, PUSH1 0x0A, SDIV` → 10 ÷ 0 = 0 (division by zero)
- **SIMPLE_DIV**: `PUSH1 0x0A, PUSH1 0x64, DIV` → 100 ÷ 10 = 10

## TODOs

**Gas & Memory:**
- [ ] Memory expansion costs for SHA3 and LOG operations
- [ ] Gas refunds for SSTORE
- [ ] Right-align MSTORE values
- [ ] Warm/cold address tracking for EXTCODECOPY

**Unimplemented Opcodes:**
- [ ] Block info (NUMBER, DIFFICULTY, GASLIMIT, CHAINID, SELFBALANCE, BASEFEE)
- [ ] Contract operations (CREATE, CREATE2, CALL, CALLCODE, DELEGATECALL, STATICCALL, RETURN, SELFDESTRUCT, INVALID)
