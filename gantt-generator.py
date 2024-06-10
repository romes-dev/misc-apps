import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Definir datas de início e fim para cada tarefa
tasks = [
    {"Task": "Definição de Requisitos", "Start": "2024-06-01", "End": "2024-06-07"},
    {"Task": "Pesquisa de Mercado", "Start": "2024-06-08", "End": "2024-06-14"},
    {"Task": "Criação do Plano de Projeto", "Start": "2024-06-15", "End": "2024-06-21"},
    {"Task": "Criação de Wireframes", "Start": "2024-06-22", "End": "2024-06-28"},
    {"Task": "Design de Interface de Usuário (UI)", "Start": "2024-06-29", "End": "2024-07-05"},
    {"Task": "Avaliação de Design", "Start": "2024-07-06", "End": "2024-07-12"},
    {"Task": "Configuração do Ambiente de Desenvolvimento", "Start": "2024-07-13", "End": "2024-07-19"},
    {"Task": "Desenvolvimento do Backend", "Start": "2024-07-20", "End": "2024-08-02"},
    {"Task": "Desenvolvimento do Frontend", "Start": "2024-08-03", "End": "2024-08-16"},
    {"Task": "Integração de API", "Start": "2024-08-17", "End": "2024-08-23"},
    {"Task": "Testes Unitários", "Start": "2024-08-24", "End": "2024-08-30"},
    {"Task": "Testes de Integração", "Start": "2024-08-31", "End": "2024-09-06"},
    {"Task": "Testes de Usabilidade", "Start": "2024-09-07", "End": "2024-09-13"},
    {"Task": "Preparação para Lançamento", "Start": "2024-09-14", "End": "2024-09-20"},
    {"Task": "Lançamento Beta", "Start": "2024-09-21", "End": "2024-09-27"},
    {"Task": "Correções de Bugs", "Start": "2024-09-28", "End": "2024-10-04"},
    {"Task": "Lançamento Final", "Start": "2024-10-05", "End": "2024-10-11"},
    {"Task": "Monitoramento e Suporte", "Start": "2024-10-12", "End": "2024-10-18"},
    {"Task": "Coleta de Feedback dos Usuários", "Start": "2024-10-19", "End": "2024-10-25"},
    {"Task": "Atualizações e Melhorias", "Start": "2024-10-26", "End": "2024-11-01"}
]

# Criar um DataFrame
df = pd.DataFrame(tasks)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Duration'] = df['End'] - df['Start']

# Plotar o diagrama de Gantt
fig, ax = plt.subplots(figsize=(10, 8))

# Adicionar barras ao gráfico
for idx, row in df.iterrows():
    ax.barh(row['Task'], row['Duration'].days, left=row['Start'], color='skyblue')

# Configurar o eixo x para mostrar datas
ax.set_xlim([df['Start'].min() - datetime.timedelta(days=2), df['End'].max() + datetime.timedelta(days=2)])
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%Y-%m-%d"))
ax.xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=7))

# Adicionar labels e título
plt.xlabel('Data')
plt.ylabel('Tarefa')
plt.title('Diagrama de Gantt do Projeto de Desenvolvimento de App de Delivery')
plt.grid(True)

# Exibir gráfico
plt.show()
