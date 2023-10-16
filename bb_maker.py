#Bibite_maker
import json
from tkinter import *
from random import randint

def read():
    with open('basic.bb8', 'r') as file:
        ddict = json.load(file)
    return dict(ddict)

def write():
    global data
    with open('new_bibite.bb8', 'w') as file:
        json.dump(data, file, indent=4)

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
def set(vnames, value):
    global data
    for elenum in range(len(vnames)):
        vnames[elenum] = vnames[elenum].strip('-')
    if len(vnames) == 1:
        data[vnames[0]] = value
    elif len(vnames) == 2:
        data[vnames[0]][vnames[1]] = value
    elif len(vnames) == 3:
        data[vnames[0]][vnames[1]][vnames[2]] = value
    elif len(vnames) == 4:
        data[vnames[0]][vnames[1]][vnames[2]][vnames[3]] = value

def new_conn(IN, OUT, WEIGHT, inov = 0):
    global data
    if type(IN) == str:
        for Node in data["brain"]["Nodes"]:
            if Node["Desc"] == IN:
                if Node["TypeName"] in ['ReLu',"Input"]:
                    IN = int(Node["Index"])
                else:
                    raise Exception(f'\'{IN}\' is not a type of input.')
        if type(IN) == str:
            raise Exception(f'\'{IN}\' is not in Nodes.')
    if type(OUT) == str:
        for Node in data["brain"]["Nodes"]:
            if Node["Desc"] == OUT:
                if Node["TypeName"] != "Input":
                    OUT = int(Node["Index"])
    data["brain"]["Synapses"].append({
        "Inov": inov,
        "NodeIn": IN,
        "NodeOut": OUT,
        "Weight": WEIGHT,
        "En": True
      })