f = open("show_version.txt")
output = f.read()
print(output)
print(type(output))
f.close()
with open("show_version.txt") as f:
	more_output = f.readlines()

print(more_output)
print(type(more_output))
print(more_output[3])
	
