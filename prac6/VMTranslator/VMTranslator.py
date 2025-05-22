class VMTranslator:

    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        assembly = []
    
    if segment == "constant":
        # Push constant value to the stack
        assembly.append(f"@{offset}")  # Load the constant value
        assembly.append("D=A")          # D = value (constant)
        assembly.append("@SP")          # Point to the stack pointer
        assembly.append("A=M")          # A = address in SP
        assembly.append("M=D")          # Store the value in stack
        assembly.append("@SP")          # Point to SP again
        assembly.append("M=M+1")        # Increment SP

    elif segment in ["local", "argument", "this", "that"]:
        base_address = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT"
        }[segment]
        
        # Push value from local, argument, this, or that segment
        assembly.append(f"@{base_address}")  # Load the base address
        assembly.append("D=M")               # D = base address
        assembly.append(f"@{offset}")         # Load the index
        assembly.append("A=D+A")             # A = base + index
        assembly.append("D=M")               # D = value at segment[index]
        assembly.append("@SP")               # Point to SP
        assembly.append("A=M")               # A = address in SP
        assembly.append("M=D")               # Store value on the stack
        assembly.append("@SP")               # Increment SP
        assembly.append("M=M+1")

    elif segment == "static":
        assembly.append(f"@Static.{offset}")  # Load the static variable
        assembly.append("D=M")               # D = static variable
        assembly.append("@SP")               # Point to SP
        assembly.append("A=M")               # A = address in SP
        assembly.append("M=D")               # Store value on the stack
        assembly.append("@SP")               # Increment SP
        assembly.append("M=M+1")
        
    elif segment == "temp":
        assembly.append(f"@{5 + offset}")     # Temp segments start from R5
        assembly.append("D=M")               # D = value at temp[index]
        assembly.append("@SP")               # Point to SP
        assembly.append("A=M")               # A = address in SP
        assembly.append("M=D")               # Store value on the stack
        assembly.append("@SP")               # Increment SP
        assembly.append("M=M+1")
    
    elif segment == "pointer":
        pointer_address = 3 + offset  # Pointer segments start from R3
        assembly.append(f"@{pointer_address}")  # Load pointer address
        assembly.append("D=M")               # D = value at pointer[index]
        assembly.append("@SP")               # Point to SP
        assembly.append("A=M")               # A = address in SP
        assembly.append("M=D")               # Store value on the stack
        assembly.append("@SP")               # Increment SP
        assembly.append("M=M+1")
    
    return "\n".join(assembly)

    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        assembly = []

        assembly.append("@SP")
        assembly.append("M=M-1")
        assembly.append("A=M)
        assembly.append("D=M")

        if segment in ["local", "argument", "this", "that"]:
        base_address = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT"
        }[segment]

        assembly.append(f"@{base_address}")  # Load the base address
        assembly.append("D=M")               # D = base address
        assembly.append(f"@{offset}")         # Load the index
        assembly.append("D=D+A")             # D = base + index
        assembly.append("@R13")              # Use R13 as a temporary storage
        assembly.append("M=D")                # Store the address in R13
        assembly.append("@R13")              # Load address from R13
        assembly.append("A=M")               # A = address in segment
        assembly.append("M=D")  

    elif segment == "static":
        assembly.append(f"@Static.{offset}")  # Load the static variable
        assembly.append("A=M")               # A = address of static variable
        assembly.append("M=D")               # Store value on the static variable

    elif segment == "temp":
        assembly.append(f"@{5 + offset}")     # Temp segments start from R5
        assembly.append("M=D")               # Store value at the temp index

    elif segment == "pointer":
        pointer_address = 3 + offset  # Pointer segments start from R3
        assembly.append(f"@{pointer_address}")  # Load pointer address
        assembly.append("M=D")               # Store value at pointer

    return "\n".join(assembly)
                    

            

    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        return ""

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        return ""

    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        return ""

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        return ""

    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        return ""

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        return ""

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        return ""

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        return ""

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        return ""

    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        return ""

    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        return ""

    def vm_if(label):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        return ""

    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        return ""

    def vm_call(function_name, n_args):
        '''Generate Hack Assembly code for a VM call operation'''
        return ""

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        return ""

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        
