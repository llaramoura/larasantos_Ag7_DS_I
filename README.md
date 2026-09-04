Markdown
# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## 📌 Sobre o Projeto

Este projeto foi desenvolvido em Python com o objetivo de calcular o consumo mensal estimado de energia elétrica de um aparelho com base em dados de uso diário.

## 🧮 Fórmula Utilizada

O consumo mensal em kWh é calculado através da fórmula:

$$\text{consumoMensal} = \frac{\text{potência} \times \text{horasDia} \times 30}{1000}$$

Where:
- **potência**: Potência do aparelho em Watts (W)
- **horasDia**: Tempo médio de uso diário em horas
- **30**: Quantidade aproximada de dias no mês
- **1000**: Fator de conversão de Watts para Quilowatts (kWh)

## ▶️ Como Executar

1. Certifique-se de ter o **Python** instalado.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
   ```bash
   python app.py