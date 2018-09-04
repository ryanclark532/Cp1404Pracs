from programming_language import ProgrammingLanguage

ruby=ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python=ProgrammingLanguage("python","Dynamic", True, 1991)
visual_basic=ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

mylist=[ruby,python,visual_basic]
for i in mylist:
    if i.typing=="Dynamic":
        print(i.name)