
prop = input("Introduceti sintaxa abstracta data de programul ce returneaza sub forma de lista formula propozitionala: ")
print()
p = input("Introduceti formula propozitionala originala: ")
p = [char for char in p if char != ' ']

prop = prop.split()
rez = "null"

for i in range(len(prop)):
    if prop[i] == '~':
        prop[i] = '⇒'
    elif prop[i] == '/':
        prop[i] = '∨'
    elif prop[i] == '=':
        prop[i] = '⇔'
    elif prop[i] == '&' or prop[i] == '^':
        prop[i] = '∧'

for i in range(len(p)):
    if p[i] == '~':
        p[i] = '⇒'
    elif p[i] == '/':
        p[i] = '∨'
    elif p[i] == '=':
        p[i] = '⇔'
    elif p[i] == '&' or p[i] == '^':
        p[i] = '∧'

p = ''.join(p)

interpreters = {}

for i in prop:
    if 'A'<= i <= 'Z':
        if i not in interpreters:
            interpreters[i] = "null"

for i in sorted(interpreters):
    print("Interpretarea lui", i, "este: ", end = '')
    interpreters[i] = int(input())

for i in range(len(prop)):
    if prop[i] in interpreters:
        prop[i] = interpreters[prop[i]]

# print(prop) # - debug

for i in range(len(prop)-1, -1, -1):
    # Warning approach
    if prop[i] == '!':
        prop[i+1] = int(not(prop[i+1]))
        rez = prop[i+1]
        for j in range(i, len(prop)):
            if prop[i] != 0 or prop[i] != 1:
                prop[i] = '*'
        # print(prop)# - debug

    elif prop[i] in ['⇒','∨','⇔','∧']:
        if prop[i] == '∧':
            a, b = '*', '*'
            for j in range(i+1, len(prop)):
                if prop[j] == 1 or prop[j] == 0:
                    if a == '*':
                        a = prop[j]
                        prop[j] = '*'
                        continue
                    else:
                        b = prop[j]
                        prop[j] = '*'
                        break
            # print(a, b)# - debug
            prop[i] = int(int(a) and int(b))
            rez = prop[i]
            # print(prop)# - debug

        elif prop[i] == '⇔':
            a, b = '*', '*'
            for j in range(i+1, len(prop)):
                if prop[j] == 0 or prop[j] == 1:
                    if a == '*':
                        a = prop[j]
                        prop[j] = '*'
                        continue

                    else:
                        b = prop[j]
                        prop[j] = '*'
                        break
            # print(a,b)# - debug
            prop[i] = int(a == b)
            rez = prop[i]
            # print(prop)# - debug

        elif prop[i] == '⇒':
            a, b = '*', '*'
            for j in range(i+1, len(prop)):
                if prop[j] == 1 or prop[j] == 0:
                    if a == '*':
                        a = prop[j]
                        prop[j] = '*'
                        continue
                    else:
                        b = prop[j]
                        prop[j] = '*'
                        break
            # print(a,b)# - debug
            prop[i] = int(not(a) or b)
            rez = prop[i]
            # print(prop)# - debug

        if prop[i] == '∨':
            a, b = '*', '*'
            for j in range(i+1, len(prop)):
                if prop[j] == 1 or prop[j] == 0:
                    if a == '*':
                        a = prop[j]
                        prop[j] = '*'
                        continue
                    else:
                        b = prop[j]
                        prop[j] = '*'
                        break
            # print(a,b)# - debug
            prop[i] = int(a or b)
            rez = prop[i]
            # print(prop)# - debug

# print(prop)# - debug
print()
print("Valoarea propozitiei", p, "sub intepretarea I₀:", [interpreters[x] for x in interpreters], "este", rez, '(', 'True' if rez == 1 else 'False', ')')
