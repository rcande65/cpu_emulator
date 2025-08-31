import registers
import memory
import instruction_counts as info

class cpu:

    def __init__(self, name, inst_mem_size=256, data_mem_size=256):
        self.name = name
        self.inst_mem_size = inst_mem_size
        self.data_mem_size = data_mem_size
        self.regs = registers.registers()
        self.inst_mem = memory.memory(inst_mem_size, "Instruction Memory")
        self.data_mem = memory.memory(data_mem_size, "Data Memory")
        self.luts = info.instruction_info()
    
    def run_program(self, print_instruction=0):
        op_code = 0x00
        pc_counts = 0
        pc_change_ops = [0x11, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x27, 0x28]
        
        print("Running Program...")
        while op_code != 0xFF:
            op_code = self.inst_mem.load_value(self.regs.PC)
            #print(op_code)
            pc_counts = self.luts.instr_pc_counts[op_code]          
            self.run_instruction(op_code, print_instruction)
            try:
                if op_code not in pc_change_ops:
                    self.regs.PC = self.regs.PC + pc_counts
                if self.regs.PC > self.inst_mem_size - 1:
                    raise ValueError(f"Ran out of memory! {self.regs.PC} > {self.inst_mem_size - 1}!")
            except ValueError:
                return

    ########################################################

    # Reset CPU
    def reset(self, debug=0):
        print("Resetting Computer...")
        self.regs.reset()
        self.inst_mem.reset()
        self.data_mem.reset()
        if debug:
            self.dump_memory()
            self.dump_regs()
        print("Reset Complete!")


    #dump data
    def dump_memory(self):
        self.inst_mem.dumb_memory()
        self.data_mem.dumb_memory()

    def dump_regs(self):
        print(self.regs)

    ########################################################

    #instructions
    #run instruction 
    def run_instruction(self, op_code, print_instruction):
        instruction_name = ""
        instruction_name =  self.luts.op_codes_to_names[op_code]
        if op_code == 0x00:
            self.sta(self.inst_mem.memory_data[self.regs.PC+1])
            if print_instruction:
                print(f"{instruction_name} {hex(self.regs.PC+1)}")          
        elif op_code == 0x01:
            self.sta_x()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x02:
            self.sta_y()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x03:
            self.lda(self.inst_mem.memory_data[self.regs.PC+1])
            if print_instruction:
                print(f"{instruction_name} {hex(self.regs.PC+1)}")   
        elif op_code == 0x04:
            self.lda_mem(self.inst_mem.memory_data[self.regs.PC+1])
            if print_instruction:
                print(f"{instruction_name} {hex(self.regs.PC+1)}")   
        elif op_code == 0x05:
            self.lda_x()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x06:
            self.lda_y()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x07:
            self.max()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x08:
            self.may()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x09:
            self.mxa()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x0A:
            self.mxy()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x0B:
            self.mya()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x0C:
            self.myx()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x0D:
            self.out()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x0E:
            self.inc_a()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x0F:
            self.inc_x()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x10:
            self.inc_y()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x11:           
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.jmp(self.inst_mem.memory_data[self.regs.PC+1])  
        elif op_code == 0x12:
            self.add(self.inst_mem.memory_data[self.regs.PC+1])
            if print_instruction:
                print(f"{instruction_name} {hex(self.regs.PC+1)}") 
        elif op_code == 0x13:
            self.add_a()
            if print_instruction:
                print(f"{instruction_name}")   
        elif op_code == 0x14:
            self.add_x()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x15:
            self.add_y()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x16:
            self.sub(self.inst_mem.memory_data[self.regs.PC+1])
            if print_instruction:
                print(f"{instruction_name} {hex(self.regs.PC+1)}") 
        elif op_code == 0x17:
            self.sub_a()
            if print_instruction:
                print(f"{instruction_name}")   
        elif op_code == 0x18:
            self.sub_x()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x19:
            self.sub_y()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x1A:
            self.inv()
            if print_instruction:
                print(f"{instruction_name}")   
        elif op_code == 0x1B:
            self.mca()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x1C:
            self.mcx()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x1D:
            self.mcy()
            if print_instruction:
                print(f"{instruction_name}")
        elif op_code == 0x1E:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.br_nzp(self.inst_mem.memory_data[self.regs.PC+1])
        elif op_code == 0x1F:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.br_n(self.inst_mem.memory_data[self.regs.PC+1])  
        elif op_code == 0x20:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.br_nz(self.inst_mem.memory_data[self.regs.PC+1])  
        elif op_code == 0x21:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.br_np(self.inst_mem.memory_data[self.regs.PC+1]) 
        elif op_code == 0x22:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.br_z(self.inst_mem.memory_data[self.regs.PC+1])
        elif op_code == 0x23:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.br_zp(self.inst_mem.memory_data[self.regs.PC+1])  
        elif op_code == 0x24:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.br_p(self.inst_mem.memory_data[self.regs.PC+1]) 
        elif op_code == 0x25:
            self.clr()
            if print_instruction:
                print(f"{instruction_name}")    
        elif op_code == 0x26:
            self.in_char(self.inst_mem.memory_data[self.regs.PC+1])
            if print_instruction:
                print(f"{instruction_name} {hex(self.regs.PC+1)}") 
        elif op_code == 0x27:
            if print_instruction:
                print(f"{instruction_name} {hex(self.inst_mem.memory_data[self.regs.PC+1])}")
            self.jsr(self.inst_mem.memory_data[self.regs.PC+1])
        elif op_code == 0x28:
            self.ret()
            if print_instruction:
                print(f"{instruction_name}")  
        elif op_code == 0xFF:
            return 0xFF
        else:
            raise Exception("Invalid Op Code!")

    #store instructions
    def sta(self, address):
        self.data_mem.store_value(address, self.regs.RegA)
    
    def sta_x(self):
        self.data_mem.store_value(self.regs.RegX, self.regs.RegA)
    
    def sta_y(self):
        self.data_mem.store_value(self.regs.RegY, self.regs.RegA)  

    ########################################################

    #load instructions
    def lda(self, value):
        self.regs.RegA = value & 0xFF
       
    def lda_mem(self, address):
        self.regs.RegA = self.data_mem.load_value(address)

    def lda_x(self):
        self.regs.RegA = self.data_mem.load_value(self.regs.RegX)

    def lda_y(self):
        self.regs.RegA = self.data_mem.load_value(self.regs.RegY)
    
    ########################################################

    #move from A to X 
    def max(self):
        self.regs.RegX = self.regs.RegA

    #move from A to Y 
    def may(self):
        self.regs.RegY = self.regs.RegA

    #move from X to A 
    def mxa(self):
        self.regs.RegA = self.regs.RegX

    #move from X to Y 
    def mxy(self):
        self.regs.RegY = self.regs.RegX

    #move from Y to A 
    def mya(self):
        self.regs.RegA = self.regs.RegY

    #move from Y to X 
    def myx(self):
        self.regs.RegX = self.regs.RegY

    #print char from A register
    def out(self):
        #print(self.regs.RegA)
        print(chr(self.regs.RegA), end="")
        #self.dump_regs()

    #Increment instructions
    #increment A register 
    def inc_a(self):
        self.regs.RegA = (self.regs.RegA + 1) & 0xFF

    #increment X register 
    def inc_x(self):
        self.regs.RegX = (self.regs.RegX + 1) & 0xFF

    #increment Y register 
    def inc_y(self):
        self.regs.RegY = (self.regs.RegY + 1) & 0xFF

    #jump
    def jmp(self, address):
        self.regs.PC = address

    #ALU Commands
    #add immediate to ACC
    def add(self, im):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b1:          
            if acc_value > im:
                answer = ((acc_value - im) | 0x80) & 0xFF
            else:
                answer = (im - acc_value) & 0xFF
        else:
            answer = (acc_value + im) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #add RegA to ACC
    def add_a(self):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b1:           
            if acc_value > self.regs.RegA:
                answer = ((acc_value - self.regs.RegA) | 0x80) & 0xFF
            else:
                answer = (self.regs.RegA - acc_value) & 0xFF
        else:
            answer = (acc_value + self.regs.RegA) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #add RegX to ACC
    def add_x(self):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b1:           
            if acc_value > self.regs.RegX:
                answer = ((acc_value - self.regs.RegX) | 0x80) & 0xFF
            else:
                answer = (self.regs.RegX - acc_value) & 0xFF
        else:
            answer = (acc_value + self.regs.RegX) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #add RegY to ACC
    def add_y(self):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b1:
            if acc_value > self.regs.RegY:
                answer = ((acc_value - self.regs.RegY) | 0x80) & 0xFF
            else:
                answer = (self.regs.RegY - acc_value) & 0xFF
        else:
            answer = (acc_value + self.regs.RegY) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #subtract commands
    #sub immediate from ACC
    def sub(self, im):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b0:
            if acc_value >= im:
                answer = (acc_value - im) & 0xFF
            else:
                answer = ((im - acc_value) | 0x80) & 0xFF
        else:
            answer = ((acc_value + im) | 0x80) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #add RegA to ACC
    def sub_a(self):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b0:
            if acc_value >= self.regs.RegA:
                answer = (acc_value - self.regs.RegA) & 0xFF
            else:
                answer = ((self.regs.RegA - acc_value) | 0x80) & 0xFF
        else:
            answer = ((acc_value + self.regs.RegA) | 0x80) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #add RegX to ACC
    def sub_x(self):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b0:
            if acc_value >= self.regs.RegX:
                answer = (acc_value - self.regs.RegX) & 0xFF
            else:
                answer = ((self.regs.RegX - acc_value) | 0x80) & 0xFF
        else:
            answer = ((acc_value + self.regs.RegX) | 0x80) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #add RegY to ACC
    def sub_y(self):
        answer = 0
        acc_value = self.regs.ACC & 0x7F
        if self.regs.Neg == 0b0:
            if acc_value >= self.regs.RegY:
                answer = (acc_value - self.regs.RegY) & 0xFF
            else:
                answer = ((self.regs.RegY - acc_value) | 0x80) & 0xFF
        else:
            answer = ((acc_value + self.regs.RegY) | 0x80) & 0xFF
        self.regs.ACC = answer
        self.regs.set_flags()

    #invert acc command
    def inv(self):
        self.regs.ACC = (~self.regs.ACC) & 0xFF
        self.regs.set_flags()

    #move acc commands
    #move acc register to RegA
    def mca(self):
        self.regs.RegA = self.regs.ACC

    #move acc register to RegX
    def mcx(self):
        self.regs.RegX = self.regs.ACC 

    #move acc register to RegY
    def mcy(self):
        self.regs.RegY = self.regs.ACC

    #branch instructions
    def br_nzp(self, address):
        if self.regs.Neg or self.regs.Zer or self.regs.Pos:
            self.regs.PC = address
        else:
            self.regs.PC = self.regs.PC + 2

    def br_n(self, address):
        if self.regs.Neg:
            self.regs.PC = address
        else:
            self.regs.PC = self.regs.PC + 2

    def br_nz(self, address):
        if self.regs.Neg or self.regs.Zer:
            self.regs.PC = address
        else:
            self.regs.PC = self.regs.PC + 2

    def br_np(self, address):
        if self.regs.Neg or self.regs.Pos:
            self.regs.PC = address
        else:
            self.regs.PC = self.regs.PC + 2

    def br_z(self, address):
        if self.regs.Zer:
            self.regs.PC = address
        else:
            self.regs.PC = self.regs.PC + 2

    def br_zp(self, address):
        if self.regs.Zer or self.regs.Pos:
            self.regs.PC = address
        else:
            self.regs.PC = self.regs.PC + 2

    def br_p(self, address):
        if self.regs.Pos:
            self.regs.PC = address
        else:
            self.regs.PC = self.regs.PC + 2

    #clear acc register
    def clr(self):
        self.regs.ACC = 0x00
        self.regs.set_flags()

    #get input char
    def in_char(self, address):
        input_string = input()
        for char in input_string:
            self.data_mem.store_value(address, ord(char))
            address = address + 1

    #subroutines
    #jump to subroutine
    def jsr(self, address):
        #push registers to the stack
        self.data_mem.push_to_stack(self.regs.PC)
        self.data_mem.push_to_stack(self.regs.ACC)
        self.data_mem.push_to_stack(self.regs.RegA)
        self.data_mem.push_to_stack(self.regs.RegX)
        self.data_mem.push_to_stack(self.regs.RegY)
        
        #setup next registers
        self.regs.reset()
        self.regs.PC = address

    #return from subroutine
    def ret(self):
        #reset regs
        self.regs.reset()

        #pop from stack
        self.regs.RegY = self.data_mem.pop_from_stack()
        self.regs.RegX = self.data_mem.pop_from_stack()
        self.regs.RegA = self.data_mem.pop_from_stack()
        self.regs.ACC  = self.data_mem.pop_from_stack()
        self.regs.PC   = self.data_mem.pop_from_stack()

        #move PC to next instruction
        self.regs.PC = self.regs.PC + 2

        #set flags
        self.regs.set_flags()

       