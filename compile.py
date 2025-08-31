import re

def compile_program(my_cpu):
    with open("program.txt", "r") as program:
        line_num = 1
        address = 0
        op_code = 0xFF
        value = 0x00
        jump_names = {}
        for line in program:
            x = re.search(r"^([a-zA-Z_]+)\s*([0-9]*);", line)
            y = re.search(r"^([a-zA-Z_]+):", line)
            z = re.search(r"^JMP\s([a-zA-Z]+);", line)
            if x: #normal command
                if x.group(2) != "":
                    #print(x.group(1) + " " + x.group(2))
                    op_code = my_cpu.luts.names_to_op_codes[x.group(1)]
                    my_cpu.inst_mem.store_value(address, op_code)
                    address = address + 1
                    value = int(x.group(2))
                    my_cpu.inst_mem.store_value(address, value)
                    address = address + 1
                else:
                    #print(x.group(1))
                    op_code = my_cpu.luts.names_to_op_codes[x.group(1)]
                    my_cpu.inst_mem.store_value(address, op_code)
                    address = address + 1
            elif y: #label
                if y.group(1) in jump_names:
                    raise Exception(f"Line {line_num}: {y.group(1)} is already being used!")
                else:
                    #jump_names[y.group(1)] = address - 2
                    jump_names[y.group(1)] = address
            elif z: #jmp command
                if z.group(1) in jump_names:
                   my_cpu.inst_mem.store_value(address, 0x11)
                   address = address + 1
                   my_cpu.inst_mem.store_value(address, jump_names[z.group(1)])
                   print(jump_names[z.group(1)])
                   address = address + 1
                else:
                    raise Exception(f"Line {line_num}: {z.group(1)} is not a valid label!")
            else:
                print(f"No valid instruction on line {line_num}")
            line_num = line_num + 1
        my_cpu.inst_mem.store_value(address, 0xFF)
        my_cpu.inst_mem.dumb_memory()