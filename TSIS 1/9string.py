#example1
print("Hello")
print('Hello')

#example2   
a = "Hello"
print(a)

#example3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#example4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#example5
a = "Hello, World!"
print(a[1])

#example6
for x in "banana":
  print(x)

#example7
a = "Hello, World!"
print(len(a))

#example8
txt = "The best things in life are free!"
print("free" in txt)    

#example9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#example10
txt = "The best things in life are free!"
print("expensive" not in txt)       

#example11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")