from platform import processor, version, python_implementation, python_version_tuple
print(processor())
print(version())

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
