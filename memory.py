class memory:

    def __init__(self, num_bytes, name):
        self.name = name
        self.memory_data = [0x00] * num_bytes
        self.size = num_bytes
        print(f"{name} Size: {num_bytes} bytes")
        #stack pointer
        self.SP = None 

    def reset(self):
        self.SP = 0xC0
        for byte in self.memory_data:
            self.memory_data[byte] = 0x00

    def gen_hex_mem(self):
        for i in self.memory_data:
            self.memory_data_hex[i] = hex(self.memory_data[i])

    def dumb_memory(self):
        print(f"{self.name} contents:")
        for i in range(0,self.size//16):
            print(f"\t{hex(i*16)}:\t{self.memory_data[i*16:i*16+16]}")
        print("")
    
    def store_value(self, address, value):
        self.memory_data[address] = value
    
    def load_value(self, address):
        return self.memory_data[address]
    
    def push_to_stack(self, reg_val):
        #print(f"Pushing {reg_val} to stack at address {self.SP}")
        self.store_value(self.SP, reg_val)
        self.SP = self.SP + 1

    def pop_from_stack(self):
        value = self.load_value(self.SP - 1)
        #print(f"Popping {value} from stack at address {self.SP - 1}")
        self.SP = self.SP - 1
        return value
        
