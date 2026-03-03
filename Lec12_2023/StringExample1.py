a = 'hello'

print(a)
print(type(a))

# Something strange happens here...
print(a[0])
print(type(a[0]))

# 'hello' is correctly typecast as 'str', but 'h' is also typeclassed as 'str', even though it is a character.