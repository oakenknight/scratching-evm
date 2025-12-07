from evm import Evm
from bytecodes import *

GAS = 21_000



for name, code in return_simple_bytecodes().items():
    print("Running EVM...")
    print("Initial gas:", GAS)
    print(f"Executing program {name}: {[hex(x) for x in code]}")

    evm = Evm(code, GAS, 0)

    # Run the program
    evm.run()

    print(f"\nExecution complete!")
    print(f"EVM gas left: {evm.gas}")
    print(f"Stack: {evm.stack}")
    print(f"Result (top of stack): {evm.stack.items[-1] if evm.stack.items else 'empty'}")
    
    print("\n" + "="*40 + "\n")

