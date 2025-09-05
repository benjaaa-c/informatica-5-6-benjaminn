independence_stages = ["inicio", "organizacion", "resistencia", "consumacion"]
print(independence_stages[0])
print(independence_stages[1:3])
print(len(independence_stages))

#List Methos
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("vicente Guerrero")
# leaders.extend(independence_stages) | Mix lists together
leaders.insert(1,"Jose Maria Morelos")
# leaders.remove("vicente Guerero") | remove the rist match of a specific item
leaders.append("Agustin de Iturbide")
#leaders.pop(1) | Remove certain indexes

print(leaders)