#Bibite_maker


import json
from tkinter import *
from random import randint

def printlogo():
    Logo = [   
 "         _  __          ____                   _               _    _                            ",
 "        | |/ /  ___    |  _ \  _ __  ___    __| | _   _   ___ | |_ (_)  ___   _ __   ___         ",
 " _____  | ' /  / _ \   | |_) || '__// _ \  / _` || | | | / __|| _ || | / _ \ | '_ \ / __|  _____ ",
 "|_____| | . \ | (_) |  |  __/ | |  | (_) || (_| || |_| || (__ | |_ | || (_) || | | |\__ \ |_____|",
 "        |_|\_(_)___(_) |_|    |_|   \___/  \____| \____| \___| \__||_| \___/ |_| |_||___/        ",
 "                                                                                                 ",
 "                                                                                                 ",
 "                      --------------- made by Kellerossel ---------------                      "
        ]
    for line in Logo:
        print(line)
printlogo()

def read(bibname='basic.bb8'):
    with open(bibname, 'r') as file:
        ddict = json.load(file)
    return dict(ddict)

def write(name = 'Pyinstein.bb8'):
    global data
    with open(name, 'w') as file:
        json.dump(data, file, indent=4)

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
