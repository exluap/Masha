###### Массив данных для получения статистики ####
stats = ['Total','HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed']

#### Ищем максимальное и минимальное среди датасета ####
def maxStat(Poke, column):
    statement = ''
    for col in column:
        stat = Poke[col].max()
        name = Poke[Poke[col]==Poke[col].max()]['Name'].values[0]
        gen = Poke[Poke[col]==Poke[col].max()]['Generation'].values[0]
        statement += name+' of Generation '+str(gen)+' has the best '+col+' stat of '+str(stat)+'.\n'
    return statement


def minStat(Poke, column):
    statement = ''
    for col in column:
        stat = Poke[col].min()
        name = Poke[Poke[col]==Poke[col].min()]['Name'].values[0]
        gen = Poke[Poke[col]==Poke[col].min()]['Generation'].values[0]
        statement += name+' of Generation '+str(gen)+' has the worst '+col+' stat of '+str(stat)+'.\n'
    return statement



