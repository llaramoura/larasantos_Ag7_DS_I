
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo opcional do custo estimado (ex: R$ 0,75 por kWh)
custo_estimado = consumo_mensal * 0.75

print("\n--- Consumo de Energia ---")
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")