import seaborn as sns
import pandas as pd
gasolina = pd.read_csv('gasolina.csv', sep=',')
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(x='dia', y='venda', data=gasolina)
  grafico.set(title='Preço da gasolina nos primeiros dias de julho/2021', xlabel='Dias', ylabel='Preço R$');
  grafico.get_figure().savefig('gasolina.png')