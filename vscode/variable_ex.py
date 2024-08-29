variable1 = "this is test string"
print(variable1)
variable2 = 10
print(variable2)
variable2 = "new value"
print(variable2)
variable2 = variable1
print(variable2)
print(variable2.title())
print(variable2.upper())
print(variable2.lower())
first_name = "Peiyang"
last_name = "Li"
full_name=f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")
name=f"\nHello, {full_name.title()}"
print(name)
favorite_color = "  blue  "
print(favorite_color)
print(favorite_color.rstrip())
print(favorite_color.lstrip())
print(favorite_color.strip())
nostarch_url = "https://nostarch.com"
print(nostarch_url)
nostarch_url = nostarch_url.removeprefix("https://")
print(nostarch_url)
filename="python_notes.txt"
print(filename)
filename=filename.removesuffix(".txt")
print(filename)