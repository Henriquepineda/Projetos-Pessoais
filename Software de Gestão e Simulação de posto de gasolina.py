import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from google.colab import files
import io
# %matplotlib inline

modo=0

print("Bem-vindo ao software de gerenciamento e simulação de postos de gasolina V1.0")

while modo!=4:
  modo=int(input("Digite o número para selecionar o modo: 1-Gerenciamento; 2-Análise de dados; 3-Simulador; 4-Desligar "))
  while modo==1:
    aberto=1
    automoveis=0
    litros_vendidos_gasolina=0
    litros_vendidos_etanol=0
    ganho=0
    custo=0
    print("Modo Gerenciamento selecionado")
    print("Esse modo consiste em auxiliar no controle de ganhos e quantia de combustível que foi vendido, trazendo o resumo do dia com todos valores utéis.")
    print("Encerre esse modo somente no final de toda operação do dia!")
    custo_gasolina=float(input("Informe o valor do quanto você está gastando por litro da gasolina "))
    preço_gasolina=float(input("Informe o valor do quanto você está vendendo o litro da gasolina "))
    custo_etanol=float(input("Informe o valor do quanto você está gastando por litro do etanol "))
    preço_etanol=float(input("Informe o valor do quanto você está vendendo o litro do etanol "))
    while aberto==1:
      print("Você ja abasteceu",automoveis,"automóveis hoje")
      menu_1=int(input("Digite o número para realizar a operação: 1-Venda Gasolina; 2-Venda Etanol; 3-Fechar o dia "))
      if menu_1==1:
        litros=float(input("Litros vendidos: "))
        litros_vendidos_gasolina=litros_vendidos_gasolina+litros
        automoveis=automoveis+1
        print("Venda registrada")
      elif menu_1==2:
        litros=float(input("Litros vendidos: "))
        litros_vendidos_etanol=litros_vendidos_etanol+litros
        automoveis=automoveis+1
        print("Venda registrada")
      elif menu_1!=3:
        print("Operação inválida")
      else:
        aberto=0
        modo=909
        print("Resumo do dia:")
        print("Você abasteceu",automoveis,"automóveis hoje")
        print("Você vendeu",litros_vendidos_gasolina,"litros de gasolina e",litros_vendidos_etanol,"litros de etanol")
        ganho=litros_vendidos_gasolina*preço_gasolina+litros_vendidos_etanol*preço_etanol
        custo=litros_vendidos_gasolina*custo_gasolina+litros_vendidos_etanol*custo_etanol
        lucro=ganho-custo
        print("Você lucrou",lucro,"reais, ganhando em media",lucro/automoveis,"por automóvel!")

  while modo==2:
    modo=4
    print("Modo Análise de dados selecionado")
    print("Esse modo monta um gráfico sobre o lucro mensal dos últimos 12 meses, alem de calcular dados relevantes com informações da planilha")
    print("OBS: Para pleno funcionamento desse modo, é importante não alterar a estrutura da planilha exemplo que foi enviada junto com o programa! Apenas alterar apenas os valores")
    arquivos = files.upload()
    df=pd.read_csv(io.BytesIO(arquivos["Dados_vendas.csv"]))
    x=df["Mes:"]
    y=df["Lucro:"]
    print(plt.plot(x,y,'g.-'))
    plt.title("Lucro mensal")
    plt.grid()
    plt.xlabel("Meses")
    plt.ylabel("Lucro")
    print("No melhor mês você lucrou:",df["Lucro:"].max())
    print("No pior mês você lucrou:",df["Lucro:"].min())
    print("Sua média de lucrou:",df["Lucro:"].mean())
  while modo==3:
    modo=909
    litros_vendidos_gasolina=0
    litros_vendidos_etanol=0
    ganho=0
    custo=0
    print("Modo Simulador selecionado")
    print("Esse modo Simula 1 mês de trabalho no posto de gasolina com preços fixos dos combustíveis. Auxiliando o planejamento financeiro do posto.")
    automoveis=int(input("Informe quantos automoveis por dia abastecem em média no posto: "))
    n=automoveis*30
    custo_gasolina=float(input("Informe o valor do quanto você está gastando por litro da gasolina "))
    preço_gasolina=float(input("Informe o valor do quanto você está vendendo o litro da gasolina "))
    custo_etanol=float(input("Informe o valor do quanto você está gastando por litro do etanol "))
    preço_etanol=float(input("Informe o valor do quanto você está vendendo o litro do etanol "))
    print("Simulando...")
    for i in range(0,n):
      abastecida=rd.randint(1,4)
      if abastecida==1:
        litros_vendidos_gasolina=litros_vendidos_gasolina+50
      if abastecida==2:
        litros_vendidos_gasolina=litros_vendidos_gasolina+25
      if abastecida==3:
        litros_vendidos_etanol=litros_vendidos_etanol+50
      else:
        litros_vendidos_etanol=litros_vendidos_etanol+25
    ganho=litros_vendidos_gasolina*preço_gasolina+litros_vendidos_etanol*preço_etanol
    custo=litros_vendidos_gasolina*custo_gasolina+litros_vendidos_etanol*custo_etanol
    lucro=ganho-custo
    print("Você lucrou",lucro,"reais, ganhando em media",lucro/n,"por automóvel!")

  if modo==4:
    modo=4
  elif modo==909:
    print("Voltando ao menu")
  else:
    print("Modo inválido")

print("Encerrando operação...")
