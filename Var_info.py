import json
from tkinter import *

tk = Tk()

def read():
    with open('basic.bb8', 'r') as file:
        ddict = json.load(file)
    return dict(ddict)

data = read()
ntext = ''
for Node in data["brain"]["Nodes"]:
    desc = Node["Desc"]
    tname = Node["TypeName"]
    index = Node["Index"]
    print(f'{desc}{" "*(16 - len(desc))} -{tname}{" "*(16 - (len(tname)+len(str(index))))} -{index}')
    ntext += f'{desc}{" "*(16 - len(desc))} -{tname}{" "*(16 - (len(tname)+len(str(index))))} -{index}\n'

vs = ''
for element in data['transform']:
    vs += f'transform -{element}\n'
for element in data['genes']['genes']:
    vs += f'genes -genes -{element}\n'
for element in data['genes']:
    if not element == 'genes':
        vs += f'genes -{element}\n'
for element in data['body']['mouth']:
    vs += f'body -mouth -{element}\n'
for element in data['body']['stomach']:
    vs += f'body -stomach -{element}\n'
for element in data['body']:
    if not element in ['mouth', 'stomach']:
        vs += f'body -{element}\n'
Nodes = Text(tk,
    width = 40,
    height = 50,
    state = "disabled")
Nodes.configure(state = "normal")
Nodes.insert(END, ntext)
Nodes.configure(state = "disabled")
Nodes.pack( side = "right")
commands = Text(tk,
    width = 40,
    height = 3,
    state = "disabled")
commands.configure(state = "normal")
commands.insert(END, '''
set: [dictionary index names]|value
new_conn: input side|output side|weight
''')
commands.configure(state = "disabled")
commands.pack(side = "top")

variables = Text(tk,
    width = 40,
    height = 47,
    state = "disabled")
variables.configure(state = "normal")
variables.insert(END, vs)
variables.configure(state = "disabled")
variables.pack(side = "bottom")
