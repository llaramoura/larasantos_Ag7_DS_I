Markdown
#  Sistema de Classificação de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Conscientização Ambiental](https://img.shields.io/badge/Meio%20Ambiente-Conscientiza%C3%A7%C3%A3o-brightgreen?style=for-the-badge)

##  Sobre o Projeto
Este sistema foi desenvolvido para a campanha de conscientização ambiental da companhia de saneamento local. O programa em Python classifica o perfil de consumo de água de imóveis (comerciais, casas ou apartamentos) com base no consumo em metros cúbicos ($m^3$) e emite alertas educativos aos moradores.

---

##  Regras de Negócio

* **Comercial:** Aplica tarifa comercial padrão.
* **Apartamento (< 10 $m^3$):** Consumo econômico.
* **Apartamento ou Casa ($\le 25\ m^3$):** Consumo moderado dentro do padrão residencial.
* **Outros casos (Consumo alto):** Alerta de consumo excessivo e instrução para verificação de vazamentos.

---

##  Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Navegue até a pasta do projeto no terminal:
   ```bash
   cd consumo-agua