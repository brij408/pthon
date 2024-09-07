txt="my name is brij"
a=txt.capitalize()
print(a)

txt="My name"
a=txt.casefold()
print(a)

txt="name"
a=txt.center(20)
print(a)

txt="yo yo honey singh"
a=txt.count("yo")
print(a)

txt="yo man."
a=txt.endswith(".")
print(a)

txt="yo\tman"
a=txt.expandtabs(7)
print(a)

txt="yo man"
a=txt.find("man")
print(a)


txt="dollor {price:.2f}"
a=txt.format(price=46)
print(a)

txt="company12"
a=txt.isalnum()
print(a)

txt="companyx"
a=txt.isalpha()
print(a)