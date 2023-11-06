name="Bob"

print(f"Hello,{name}")
name="Rolf"
print(f"Hello,{name}")     

name="Bob"
greeting="Hello.{}"
with_name=greeting.format(name) # Calling format function in greeting 
print(with_name)

longer_phrase="Hello ,{}.Today is {}"
formated=longer_phrase.format("Kapil","Monday")
print(formated)