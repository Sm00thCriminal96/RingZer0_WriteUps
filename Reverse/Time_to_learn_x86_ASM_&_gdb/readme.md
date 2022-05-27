# Steps used to find the flags:
1. Download the file (will be downloaded as a zip file).
2. Unzip it to get the executable file. Running it will print two lines, 'loading..' & 'Where is the flag?'
3. Open the executable in gdb. From disassembling the main function you can see a big function.
4. But the flag is in one of the local variables of the main function. This will take a couple of breakpoints to locate the address and its content.
5. The below screenshot shows the places breakpoint are to be set to get the flag,

![First Breakpoint](https://github.com/Sm00thCriminal96/RingZer0_WriteUps/blob/main/Reverse/Time_to_learn_x86_ASM_&_gdb/images/eax_screenshot.jpg)

6. Set the breakpoint at the highlighted address

![Second Breakpoint](https://github.com/Sm00thCriminal96/RingZer0_WriteUps/blob/main/Reverse/Time_to_learn_x86_ASM_&_gdb/images/leave_screenshot.jpg)

7. After these breakpoints are set, run the executable inside the gdb with 'run' or 'r' command.
8. When the first breakpoint is reached, print the value of eax in hexadecimal format. This is the address where the flag string is being loaded throughout the main function.
9. Continue the execution of the executable with the 'continue' or 'c' command.
10. Now, when the second breakpoint is reached, we are at the end of main function. Now use 'examine' or 'x' command as 's' format to print in string form, from the address we found above (in the first breakpoint).
11. This will print the flag value.
