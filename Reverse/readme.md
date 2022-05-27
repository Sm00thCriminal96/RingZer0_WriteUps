# Steps used to find the flags:
*1. Download the file (will be downloaded as a zip file).
*2. Unzip it to get the executable file. Running it will print two lines, 'loading..' & 'Where is the flag?'
*3. Open the executable in gdb. From disassembling the main function you can see a big function.
*4. But the flag is in one of the local variables of the main function. This will take a couple of breakpoints to locate the address and its content.
