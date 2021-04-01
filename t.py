import sys

s = open(sys.argv[1], 'r').read().replace(' ', '').replace('\n', '').replace('}', '}\n')

s = s.replace(',', '').split('\n')[:-1]

for i in s:
    ss = i.split('{')[0].split('.')[1:]
    print(f""".replace(/class\=\"({'|'.join(ss)})\"/g, 'style="{i.split('{')[1][:-1]}"')""")
