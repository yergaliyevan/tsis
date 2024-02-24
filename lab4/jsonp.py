import json
print("Interface status")
print("="*80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN","Description", "Speed","MTU"))
print("-"*50, "-"*20,"-"*8,"-"*6)
with open("sample-data.json") as file:
    data=json.load(file)
dataim=data["imdata"]
for i in dataim:
    l1=i["l1PhysIf"]
    att=l1["attributes"]
    dn=att["dn"]
    descrip=att["descr"]
    speed=att["speed"]
    mtu=att["mtu"]
    
    
    
    print("{:<50}{:<20}{:<8}{:<6}".format(dn,descrip,speed,mtu))
        
    
    
    
