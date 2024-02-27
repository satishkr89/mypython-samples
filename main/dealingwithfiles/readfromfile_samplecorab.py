sample_brd = open("/Users/satishkumar/Library/CloudStorage/Dropbox/Mac/Downloads/sample_board.txt")


#line = sample_brd.readline() 
pwn=0
# while True:
#    line = sample_brd.readline().strip()
#    if(line == ""):
#        break
#    #pwn=line.count('p') + line.count('P')
#    pwn += line.lower().count('p')
#    print(f"line is {line}, pawn in this line: {pwn}")

# print(f"Pawn on this board are: {pwn}")  

lines = sample_brd.readlines()
for line in lines:
   line = line.strip()
   #pwn=line.count('p') + line.count('P')
   pwn += line.lower().count('p')
   print(f"line is {line}, pawn in this line: {pwn}")

print(f"Pawn on this board are: {pwn}")  

# no need for if , as while line is checing that
# file = open("C:/Users/hania/Downloads/sample_board.txt")
# line = file.readline()
# while line:
#     line = line.strip()
#     print(line) #process
#     line = file.readline() #reads the next line