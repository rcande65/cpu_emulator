from cpu import cpu
from compile_v2 import compile_program

DEBUG = 0

my_cpu = cpu("My CPU", inst_mem_size=2048, data_mem_size=2048)
my_cpu.reset(debug=DEBUG)

program_file = "./Programs/program_4.txt"

compile_program(my_cpu, program_file)
my_cpu.run_program(print_instruction=DEBUG),
print("")
if DEBUG:
    my_cpu.dump_memory()
    my_cpu.dump_regs()