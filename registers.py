class registers:
    def __init__(self):
        #Registers
        self.PC     = 0x00 
        self.ACC    = 0x00
        self.RegA   = 0x00
        self.RegX   = 0x00
        self.RegY   = 0x00
        #Flags
        self.Neg    = 0b0
        self.Pos    = 0b0
        self.Zer    = 0b0

    def __str__(self):
        return f"Register Contents:\n \
                 Program Counter        : {hex(self.PC)}\n \
                 Accumulator Register   : {hex(self.ACC)}\n \
                 Data Register A        : {hex(self.RegA)}\n \
                 Data Register X        : {hex(self.RegX)}\n \
                 Data Register Y        : {hex(self.RegY)}\n \
                 Flag Contents:\n \
                 Negative Flag          : {hex(self.Neg)}\n \
                 Positive Flag          : {hex(self.Pos)}\n \
                 Zero Flag              : {hex(self.Zer)}\n"

    def reset(self):
        self.PC     = 0x00
        self.ACC    = 0x00
        self.RegA   = 0x00
        self.RegX   = 0x00
        self.RegY   = 0x00
        self.Neg    = 0b0
        self.Pos    = 0b0
        self.Zer    = 0b1

    def set_flags(self):
        if self.ACC & 0x80:
            self.Neg = 0b1
            self.Pos = 0b0
            self.Zer = 0b0
        elif self.ACC != 0x00:
            self.Neg = 0b0
            self.Pos = 0b1
            self.Zer = 0b0
        else:
            self.Neg = 0b0
            self.Pos = 0b0
            self.Zer = 0b1               
