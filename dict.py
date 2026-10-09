students={
    101:{"Name":"Aditya","Scores":[20,10,30]},
    102:{"Name":"Soumya","Scores":[50,90,70]},
    103:{"Name":"Meghna","Scores":[96,90,970]},
    104:{"Name":"Raj","Scores":[0,10,70]}
}

for sid,details in students.items():
    avg=sum(details["Scores"])/len(details["Scores"])
    details["Average"]=avg
    details["Passed"]= avg>=30
    
for sid,details in students.items():
    if details["Passed"]:
        print(details["Name"])