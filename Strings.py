message = 'Hello World'
multiple_line = """Hello Python grind
para kay sa aking Future"""

print(multiple_line)

print(message) # simple print
print(message[0]) # accessing individual characters of the string using index
print(message[0:5]) # access a range of character using colon start:stop but not including the stop
print(message[6:]) # blank means start: means at the end and :stop meaning from the begininng to at a point
print(len(message)) # total characters even the whitespace

# STRING METHODS
print(message.lower())
print(message.upper())
print(message.count('l')) # count a certain characters on a string
print(message.find('World'))# find index of ceratin characters if not found it will return -1

message = message.replace('World', 'Universe') # needs to be assign because it counts as a new string or word
print(message)

greeting = 'Hello'
name = 'Celestia'

#concatanating string
message = greeting + ", " +name # add multiple and concatenating them using '+'
message = '{}, {}. Welcome!'.format(greeting,name) # for longer string USE STRING FORMAT
message = f'{greeting}, {name.upper()}. Welcomeeee!' # latest versions of python introduce f method
print(message)

print(dir(name)) # shows possible methods you can use
print(help(str)) # shows detailed information of methods
