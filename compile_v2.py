import re

def compile_program(my_cpu, program_file):
    with open(program_file, "r") as program:
        line_num = 1
        instruction = {}
        address = 0
        op_code = 0xFF
        jump_names = {}
        unknown_jumps = {}
        pc_change_ops = [0x11, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x27]
        for line in program:
            #print(line)
            x = re.search(r"^([a-zA-Z_]+)\s*([0-9]*);", line)
            y = re.search(r"^([a-zA-Z_]+):", line)
            z = re.search(r"^JMP\s([a-zA-Z_]+);", line)
            a = re.search(r"^(BR[nzp]+)\s([a-zA-Z_]+);", line)
            b = re.search(r"^.STRING ([0-9]+)\s\"(.+)\"", line)
            c = re.search(r"^JSR\s([a-zA-Z_]+);", line)
            d = re.search("^\n", line)
            e = re.search("^#", line)
            f = re.search(r"^.VALUE ([0-9]+)\s\"(.+)\"", line)
            if x: #normal command
                if x.group(2) != "":
                    op_code = my_cpu.luts.names_to_op_codes[x.group(1)]
                    instruction[address] = [op_code , int(x.group(2))]
                    address = address + 2
                else:
                    op_code = my_cpu.luts.names_to_op_codes[x.group(1)]
                    instruction[address] = [op_code]
                    address = address + 1
            elif y: #label
                if y.group(1) in jump_names:
                    raise Exception(f"Line {line_num}: {y.group(1)} is already being used!")
                else:
                    jump_names[y.group(1)] = address #store the address where a label jumps to {label : addr}
            elif z: #jmp command
                instruction[address] = [0x11, None] #store the jump command without the label, fill in label at the end
                unknown_jumps[address] = z.group(1) #store the name of the label for that jump command address {addr : label}
                address = address + 2
            elif a: #branch command
                op_code = my_cpu.luts.names_to_op_codes[a.group(1)]
                instruction[address] = [op_code, None] #store the jump command without the label, fill in label at the end
                unknown_jumps[address] = a.group(2) #store the name of the label for that jump command address {addr : label}
                address = address + 2
            elif b: #put string in memory
                location = int(b.group(1))
                my_string = b.group(2)
                for char in my_string:
                    my_cpu.data_mem.store_value(location, ord(char))
                    location = location + 1
            elif c: #jsr
                instruction[address] = [0x27, None] #store the jump command without the label, fill in label at the end
                unknown_jumps[address] = c.group(1) #store the name of the label for that jump command address {addr : label}
                address = address + 2
            elif d: #blank line
                continue
            elif e: #comment line
                continue
            elif f: #put value in memory
                location = int(f.group(1))
                my_value = int(f.group(2))
                #print(f"Address = {location}, Value = {my_value}")
                my_cpu.data_mem.store_value(location, my_value)
            else:
                print(f"No valid instruction on line {line_num}")
            line_num = line_num + 1
        
        address = 0
        for addr, inst in instruction.items():
            if inst[0] in pc_change_ops:
                if unknown_jumps[addr] in jump_names:
                    inst[1] = jump_names[unknown_jumps[addr]]
                else:
                    raise Exception(f"Address {addr}: There is no label {unknown_jumps[addr]}!")
            
        address = 0
        #write instructions to memory
        for key, list in instruction.items():
            for item in list:
                my_cpu.inst_mem.store_value(address, item)
                address = address + 1
        my_cpu.inst_mem.store_value(address, 0xFF)
        #my_cpu.inst_mem.dumb_memory()