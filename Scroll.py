program = input()

string = [] # Totally a string
n = []

# Find matching brackets
left_brackets = {}
right_brackets = {}
open_brackets = []

index = 0
while index < len(program):
   if program[index] == "[":
      open_brackets.append(index)
   elif program[index] == "]":
      left_brackets[index] = open_brackets[-1]
      right_brackets[open_brackets[-1]] = index
      del open_brackets[-1]
   index += 1

if open_brackets:
   print("Error: Unexpected EOF")
   exit(-1)

# Execute the program
index = 0
while index < len(program):
   command = program[index]

   try:
      if command == '[':
         n.append(string[-1])
         del string[-1]

         if string[-1] == n[-1]:
           index = right_brackets[index]

      elif command == ']':
         if string[-1] != n[-1]:
            index = left_brackets[index]
         else:
            del n[-1]

      elif command == '$':
         string.insert(0, string[-1])
         del string[-1]

      elif command == '*':
         del string[-1]

      else:
         string.append(command)
   except IndexError: # Can append if the string or n is empty
      pass

   index += 1

print(''.join(string))
