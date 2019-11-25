message = 'Hello World!'
print(len(message))
print(message[11])
print(message[0:5])  # 0 is inclusive but 5 is not.
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))

new_message = message.replace('World','Universe')
print(new_message)

greeting = 'Hello'
name = 'Nachiket'
message = greeting + ' ' + name + '!'
print(message)
name = 'Nick'
message = "{0} {1}!".format(greeting, name)
print(message)
name = 'Nicholas'
message = f"{greeting} {name.upper()}!"
print(message)

print(dir(name))
print(help(str))
print(help(str.encode()))