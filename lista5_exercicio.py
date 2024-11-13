clientes_A = {"Alice", "Bob", "Cesar", "Anderson"}
clientes_B = {"Cesar", "Anderson", "Gabriel", "Bruno"}

clientes_em_ambos = clientes_A & clientes_B
clientes_apenas_A = clientes_A - clientes_B
clientes_apenas_um_conjunto = clientes_A ^ clientes_B
clientes_unicos = clientes_A | clientes_B
percentual_clientes_unicos = (len(clientes_apenas_um_conjunto) / len(clientes_unicos)) * 100

print(f"Clientes em ambos os conjuntos: {clientes_em_ambos}")
print(f"Clientes apenas em clientes_A: {clientes_apenas_A}")
print(f"Clientes em apenas um dos conjuntos: {clientes_apenas_um_conjunto}")
print(f"Porcentagem de clientes únicos: {percentual_clientes_unicos:.1f} %")
