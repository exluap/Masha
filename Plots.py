import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from Poke import Poke, PokeL, frame
import seaborn as sb

# Для каждого основного умения свой цвет
type1_colours = ['#6890F0',  # Water
                 '#A8A878',  # Normal
                 '#A8B820',  # Bug
                 '#78C850',  # Grass
                 '#F08030',  # Fire
                 '#F85888',  # Psychic
                 '#F8D030',  # Electric
                 '#B8A038',  # Rock
                 '#705898',  # Ghost
                 '#A040A0',  # Poison
                 '#E0C068',  # Ground
                 '#705848',  # Dark
                 '#C03028',  # Fighting
                 '#98D8D8',  # Ice
                 '#B8B8D0',  # Steel
                 '#7038F8',  # Dragon
                 '#EE99AC',  # Fairy
                 '#A890F0',  # Flying
                 ]
# Для каждого дополнительного умения тоже
type2_colours = ['#78C850',  # None
                 '#A890F0',  # Flying
                 '#A040A0',  # Poison
                 '#E0C068',  # Ground
                 '#78C850',  # Grass
                 '#F85888',  # Psychic
                 '#B8B8D0',  # Steel
                 '#C03028',  # Fighting
                 '#EE99AC',  # Fairy
                 '#705848',  # Dark
                 '#B8A038',  # Rock
                 '#6890F0',  # Water
                 '#705898',  # Ghost
                 '#7038F8',  # Dragon
                 '#98D8D8',  # Ice
                 '#F08030',  # Fire
                 '#F8D030',  # Electric
                 '#A8A878',  # Normal
                 '#A8B820',  # Bug
                 ]

########## Сравниваем атаку и защиту по сравнению с доп параметрами ########
sb.set()
AttvTot = sb.lmplot(x='Attack', y='Sp.Atk', data=Poke,
                    fit_reg=False, size=9, aspect=1)
plt.ylim(0, 150)
plt.xlim(0, 175)
plt.title('Attack and Sp.Atk', fontsize=25)
plt.xlabel('Attack', fontsize=18)
plt.ylabel('Sp.Atk', fontsize=18)
AttvTot.savefig("Two-dimensional distribution Attack and Sp.Atk.png")

sb.set()
AttvTot = sb.lmplot(x='Defense', y='Sp.Def', data=Poke,
                    fit_reg=False, size=9, aspect=1)
plt.ylim(0, 175)
plt.xlim(0, 200)
plt.title('Defense and Sp.Defense', fontsize=25)
plt.xlabel('Defense', fontsize=18)
plt.ylabel('Sp.Def', fontsize=18)
AttvTot.savefig("Two-dimensional distribution Defense and Sp.Def.png")

sb.set()
AttvTot = sb.lmplot(x='Attack', y='Speed', data=Poke,
                    fit_reg=False, size=9, aspect=1)
plt.ylim(0, 175)
plt.xlim(0, 175)
plt.title('Attack and Speed', fontsize=25)
plt.xlabel('Attack', fontsize=18)
plt.ylabel('Speed', fontsize=18)
AttvTot.savefig("Two-dimensional distribution Attack and Speed.png")


sb.set()


#sb.set()
#AttvDef = sb.lmplot(x='Speed', y='Type1', data=Poke,
#                    fit_reg=False, size=9, aspect=1)
#plt.title('Primary types and speed', fontsize=25)
#plt.xlabel('Types', fontsize=18)
#plt.ylabel('Speed', fontsize=18)
#AttvDef.savefig("Types & Speed.png")

sb.set()
dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=dims)
vp = sb.violinplot(x='Generation', y='Total', data=Poke, ax=ax)
plt.title('Violin plot of Generation base stat total', fontsize=18)
plt.xlabel('Generation', fontsize=12)
plt.ylabel('Total', fontsize=12)
figVP = vp.get_figure()
figVP.savefig("Violin_Gen.png")

sb.set()
dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=dims)
bp = sb.boxplot(x='Generation', y='Total', data=Poke, ax=ax)
plt.title('Box plot of Generation base stat total', fontsize=18)
plt.xlabel('Generation', fontsize=12)
plt.ylabel('Total', fontsize=12)
figBP = bp.get_figure()
figBP.savefig("Box_Gen.png")

sb.set()
fig, ax = plt.subplots(figsize=dims)
TySplit = [Poke['Type1'].count() - Poke['Type2'].count(), Poke['Type2'].count()]
TypePie = plt.pie(TySplit, labels=['Primary only', 'Primary and Secondary'], autopct='%1.1f%%', radius=1.1, startangle=90,
                  shadow=False, explode=(0, 0))
plt.title('Single Type vs Dual Type Pokemon', fontsize=18)
plt.savefig("TypePie.png")

Type1 = pd.value_counts(Poke['Type1'])
sb.set()
dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x=Type1.index, y=Type1, data=Poke, palette=type1_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation=75, fontsize=12)
BarT.set(xlabel='Pokemon Primary Types', ylabel='Quantity')
BarT.set_title('Distribution of Primary Pokemon Types')
FigBar = BarT.get_figure()
FigBar.savefig("Primary types distribution.png")

##########for row in Poke.loc[Poke.Type2.isnull(), 'Type2'].index:
##########    Poke.at[row, 'Type2'] = 'None'



Type2 = pd.value_counts(Poke['Type2'])
sb.set()
dims = (11.7, 8.27)
fig, ax = plt.subplots()
BarT = sb.barplot(x=Type2.index, y=Type2, data=Poke, palette=type2_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation=75, fontsize=12)
BarT.set(xlabel='Pokemon Secondary Types', ylabel='Freq')
BarT.set_title('Distribution of Secondary Pokemon Types')
FigBar = BarT.get_figure()
FigBar.savefig("Secondary types distribution.png")


LSplit = [Poke['Name'].count(), PokeL['Name'].count()]
LegendPie = plt.pie(LSplit, labels=['Not Legendary', 'Legendary'], autopct='%1.1f%%', shadow=True, startangle=90,
                    explode=(0, 0.1))
plt.title('Legendary Split', fontsize=12)
fig = plt.gcf()
fig.set_size_inches(11.7, 8.27)
plt.savefig("LegendPie.png")

Corr = Poke[['Total', 'HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']]

sb.set()
dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=dims)
CorrelationMap = sb.heatmap(Corr.corr(), annot=True, ax=ax)
CorrelationMap.set(title='HeatMap to show Correlation between Base Stats')
FigMap = CorrelationMap.get_figure()
FigMap.savefig("HeatMapCorr.png")

dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=dims)
Atthist = sb.distplot(Poke['Attack'], color='r', hist=False, ax=ax)
SpAhist = sb.distplot(Poke['Sp.Atk'], color='b', hist=False, ax=ax)
SpAhist.set(title='Distribution of Attack and Sp.Atk', xlabel='Attack:r , Sp.Atk:b')
FigHist = SpAhist.get_figure()
FigHist.savefig("Hist.png")

DS = Corr.describe()
print(DS)
