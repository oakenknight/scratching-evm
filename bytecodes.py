
SIMPLE_ADD = [0x60, 0x42, 0x60, 0xFF, 0x01]
SIMPLE_PUSH = [0x60, 0x42]

MUL_BY_ZERO     = [0x60, 0x42, 0x60, 0x00, 0x02] #  66*0 = 0

SIMPLE_MUL      = [0x60, 0x14, 0x60, 0x0A, 0x02] # 20*10=200

EXP_OVERFLOW = [0x60, 0xFF, 0x60, 0x02, 0x0A]  #2^255 mod 2^256

SDIV_ZERO       = [0x60, 0x00, 0x60, 0x0A, 0x05] #division by 0 = 0

SIMPLE_DIV      = [0x60, 0x0A, 0x60, 0x64, 0x04] #  100 / 10 = 10

def return_simple_bytecodes():
    return {
        "SIMPLE_ADD": SIMPLE_ADD,
        "SIMPLE_PUSH": SIMPLE_PUSH,
        "MUL_BY_ZERO": MUL_BY_ZERO,
        "SIMPLE_MUL": SIMPLE_MUL,
        "EXP_OVERFLOW": EXP_OVERFLOW,
        "SDIV_ZERO": SDIV_ZERO,
        "SIMPLE_DIV": SIMPLE_DIV,
    }

