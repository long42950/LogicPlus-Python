NAND = lambda l1,l2:not(l1 and l2)
NOR = lambda l1,l2:not(l1 or l2)

def XOR(l1,l2):
    if l1 or l2:
        if l1 and l2:
            return False
        return True
    return False

XNOR = lambda l1,l2:not(XOR(l1,l2))

while True:
    logic = input("So which logic did you forget: ").upper()
    match logic:
        case "NAND":
            print("==================")
            print("|      NAND      |")
            print("==================")
            print("| A | B | result |")
            print("==================")
            print("| 0 | 0 |   True |")
            print("| 0 | 1 |   True |")
            print("| 1 | 0 |   True |")
            print("| 1 | 1 |  False |")
            print("==================")
        case "NOR":
            print("==================")
            print("|       NOR      |")
            print("==================")
            print("| A | B | result |")
            print("==================")
            print("| 0 | 0 |   True |")
            print("| 0 | 1 |  False |")
            print("| 1 | 0 |  False |")
            print("| 1 | 1 |  False |")
            print("==================")
        case "XOR":
            print("==================")
            print("|       XOR      |")
            print("==================")
            print("| A | B | result |")
            print("==================")
            print("| 0 | 0 |  False |")
            print("| 0 | 1 |   True |")
            print("| 1 | 0 |   True |")
            print("| 1 | 1 |  False |")
            print("==================")
        case "XNOR":
            print("==================")
            print("|      XNOR      |")
            print("==================")
            print("| A | B | result |")
            print("==================")
            print("| 0 | 0 |   True |")
            print("| 0 | 1 |  False |")
            print("| 1 | 0 |  False |")
            print("| 1 | 1 |   True |")
            print("==================")
        case _:
            print("This is either not a gate at all or one you shouldn't forget about...")
