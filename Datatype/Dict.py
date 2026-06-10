#Key & Value
soumo = {"name":"soumyajit","address":"Bahirtafa","Village":"Rampur"}

print(" Dictionary = ",soumo)
print("Datatype = ",type(soumo))

#adding new elements
soumo ["Police station"] = "Jagannathpur"
print(soumo)

#update elements
soumo.update({"Police station":"Srirampur"})
print(soumo)

soumo.update({"address":"uluberia"})
print(soumo)