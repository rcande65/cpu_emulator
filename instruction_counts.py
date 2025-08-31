class instruction_info:

    #define op_codes
    def __init__(self):
        self.names_to_op_codes =  {#store
                                "STA"     : 0x00,
                                "STA_X"   : 0x01,
                                "STA_Y"   : 0x02,
                                #load
                                "LDA"     : 0x03,
                                "LDA_MEM" : 0x04,
                                "LDA_X"   : 0x05,
                                "LDA_Y"   : 0x06,
                                #move
                                "MAX"     : 0x07,
                                "MAY"     : 0x08,
                                "MXA"     : 0x09,
                                "MXY"     : 0x0A,
                                "MYA"     : 0x0B,
                                "MYX"     : 0x0C,
                                #character out
                                "OUT"     : 0x0D,
                                #increment
                                "INC_A"   : 0x0E,
                                "INC_X"   : 0x0F,
                                "INC_Y"   : 0x10,
                                #jump
                                "JMP"     : 0x11,
                                #add
                                "ADD"     : 0x12,
                                "ADD_A"   : 0x13,
                                "ADD_X"   : 0x14,
                                "ADD_Y"   : 0x15,
                                #sub
                                "SUB"     : 0x16,
                                "SUB_A"   : 0x17,
                                "SUB_X"   : 0x18,
                                "SUB_Y"   : 0x19,
                                #inv
                                "INV"     : 0x1A,
                                #move from acc
                                "MCA"     : 0x1B,
                                "MCX"     : 0x1C,
                                "MCY"     : 0x1D,
                                #branch
                                "BRnzp"   : 0x1E,
                                "BRn"     : 0x1F,
                                "BRnz"    : 0x20,
                                "BRnp"    : 0x21,
                                "BRz"     : 0x22,
                                "BRzp"    : 0x23,
                                "BRp"     : 0x24,
                                #clear acc
                                "CLR"     : 0x25,
                                #get char in 
                                "IN"      : 0x26,
                                #jsr/ret
                                "JSR"     : 0x27,
                                "RET"     : 0x28,
                                #code Terminator
                                "END"     : 0xFF
                                }
        self.op_codes_to_names =  {#store
                                0x00  : "STA",
                                0x01  : "STA_X",
                                0x02  : "STA_Y",
                                #load
                                0x03  : "LDA",
                                0x04  : "LDA_MEM",
                                0x05  : "LDA_X",
                                0x06  : "LDA_Y",
                                #move
                                0x07  : "MAX",
                                0x08  : "MAY",
                                0x09  : "MXA",
                                0x0A  : "MXY",
                                0x0B  : "MYA",
                                0x0C  : "MYX",
                                0x0D  : "OUT",
                                #increment
                                0x0E  : "INC_A",
                                0x0F  : "INC_X",
                                0x10  : "INC_Y",
                                #jump
                                0x11  : "JMP",
                                #add
                                0x12  : "ADD",
                                0x13  : "ADD_A",
                                0x14  : "ADD_X",
                                0x15  : "ADD_Y",
                                #sub
                                0x16  : "SUB",
                                0x17  : "SUB_A",
                                0x18  : "SUB_X",
                                0x19  : "SUB_Y",
                                #inv
                                0x1A  : "INV",
                                #move from acc
                                0x1B  : "MCA",
                                0x1C  : "MCX",
                                0x1D  : "MCY",
                                #branch
                                0x1E  : "BRnzp",
                                0x1F  : "BRn",
                                0x20  : "BRnz",
                                0x21  : "BRnp",
                                0x22  : "BRz",
                                0x23  : "BRzp",
                                0x24  : "BRp",
                                #clear acc
                                0x25  : "CLR",
                                #get char in
                                0x26  : "IN",
                                #jsr/ret
                                0x27  : "JSR",
                                0x28  : "RET",
                                #code terminator
                                0xFF  : "END"
                                }
        self.instr_pc_counts =  {#store
                                0x00  : 2,
                                0x01  : 1,
                                0x02  : 1,
                                #load
                                0x03  : 2,
                                0x04  : 2,
                                0x05  : 1,
                                0x06  : 1,
                                #move
                                0x07  : 1,
                                0x08  : 1,
                                0x09  : 1,
                                0x0A  : 1,
                                0x0B  : 1,
                                0x0C  : 1,
                                0x0D  : 1,
                                #increment
                                0x0E  : 1,
                                0x0F  : 1,
                                0x10  : 1,
                                #jump
                                0x11  : 2,
                                #add
                                0x12  : 2,
                                0x13  : 1,
                                0x14  : 1,
                                0x15  : 1,
                                #sub
                                0x16  : 2,
                                0x17  : 1,
                                0x18  : 1,
                                0x19  : 1,
                                #inv
                                0x1A  : 1,
                                #move from acc
                                0x1B  : 1,
                                0x1C  : 1,
                                0x1D  : 1,
                                #branch
                                0x1E  : 2,
                                0x1F  : 2,
                                0x20  : 2,
                                0x21  : 2,
                                0x22  : 2,
                                0x23  : 2,
                                0x24  : 2,
                                #clear acc
                                0x25  : 1,
                                #get char in
                                0x26  : 2,
                                #jsr/ret
                                0x27  : 2,
                                0x28  : 1,
                                #code terminator
                                0xFF  : 1
                                }
        