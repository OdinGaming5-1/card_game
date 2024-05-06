from config import *
import json

class CardData:
    Name=""
    Icon=""
    Description=""
    DamageType=""
    DamageDuration=0
    Damage=0
    Mana=0
    AreaOfEffect=False
    def __init__(self,damage_type,index):
        if damage_type=="Magical":
            with open(config.config("magicalcards"), 'r') as file:
                data = ' '.join(file.readlines())
                self.cards=json.loads(data)
        elif damage_type=="Physical":   
            with open(config.config("physicalcards"), 'r') as file:
                data = ' '.join(file.readlines())
                self.cards=json.loads(data)
                       
        card=self.cards[index]
        self.Name=card["Name"]
        self.Icon=card["Icon"]
        self.Description=card["Description"]
        self.DamageType=card["DamageType"]
        self.DamageDuration=card["DamageDuration"]
        self.Damage=card["Damage"]
        self.Mana=card["Mana"]
        self.AreaOfEffect=card["AreaOfEffect"]
