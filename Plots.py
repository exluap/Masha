import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import concat

from Poke import Poke, PokeL, frame, Gen1, Gen2, Gen3, Gen4, Gen5, Gen6
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

sb.set(font_scale=2)


## Среднее значение скорости для каждого типа

dims = (15.0, 10.0)
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x='Type1', y='Speed', data=Poke, palette=type1_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation=75, fontsize=11)
BarT.set(xlabel='Pokemon Types', ylabel='Quantity')
BarT.set_title('Speed means', fontsize=20)
FigBar = BarT.get_figure()
FigBar.savefig("SpeedMeans.png")


dims = (15.0, 10.0)
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x='Type1', y='Attack', data=Poke, palette=type1_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation=75, fontsize=11)
BarT.set(xlabel='Pokemon Types', ylabel='Quantity')
BarT.set_title('Attack means', fontsize=20)
FigBar = BarT.get_figure()
FigBar.savefig("AttackMeans.png")


dims = (15.0, 10.0)
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x='Type1', y='Defense', data=Poke, palette=type1_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation=75, fontsize=11)
BarT.set(xlabel='Pokemon Types', ylabel='Quantity')
BarT.set_title('Defense means', fontsize=20)
FigBar = BarT.get_figure()
FigBar.savefig("DefenseMeans.png")



########## Сравниваем атаку и защиту по сравнению с доп параметрами ########

AttvTot = sb.lmplot(x='Attack', y='Sp.Atk', data=Poke,
                    fit_reg=False, height=9, aspect=1)
plt.ylim(0, 150)
plt.xlim(0, 175)
plt.title('Attack and Sp.Atk', fontsize=25)
plt.xlabel('Attack', fontsize=18)
plt.ylabel('Sp.Atk', fontsize=18)
AttvTot.savefig("Two-dimensional distribution Attack and Sp.Atk.png")


AttvTot = sb.lmplot(x='Defense', y='Sp.Def', data=Poke,
                    fit_reg=False, height=9, aspect=1)
plt.ylim(0, 175)
plt.xlim(0, 200)
plt.title('Defense and Sp.Defense', fontsize=25)
plt.xlabel('Defense', fontsize=18)
plt.ylabel('Sp.Def', fontsize=18)
AttvTot.savefig("Two-dimensional distribution Defense and Sp.Def.png")


AttvTot = sb.lmplot(x='Attack', y='Speed', data=Poke,
                    fit_reg=False, height=9, aspect=1)
plt.ylim(0, 175)
plt.xlim(0, 175)
plt.title('Attack and Speed', fontsize=25)
plt.xlabel('Attack', fontsize=18)
plt.ylabel('Speed', fontsize=18)
AttvTot.savefig("Two-dimensional distribution Attack and Speed.png")



#
# AttvDef = sb.lmplot(x='Speed', y='Type1', data=Poke,
#                    fit_reg=False, size=9, aspect=1)
# plt.title('Primary types and speed', fontsize=25)
# plt.xlabel('Types', fontsize=18)
# plt.ylabel('Speed', fontsize=18)
# AttvDef.savefig("Types & Speed.png")

dims=(15.0, 10.0)
fig, ax = plt.subplots(figsize=dims)
TySplit = [Poke['Type1'].count() - Poke['Type2'].count(), Poke['Type2'].count()]
TypePie = plt.pie(TySplit, labels=['Primary only', 'Primary and Secondary'], autopct='%1.1f%%', radius=1.1,
                  startangle=90,
                  shadow=False, explode=(0, 0))
plt.title('Single Type vs Dual Type Pokemon', fontsize=18)
plt.savefig("TypePie.png")

Type1 = pd.value_counts(Poke['Type1'])

dims = (15, 10)
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x=Type1.index, y=Type1, data=Poke, palette=type1_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation=75, fontsize=11)
BarT.set(xlabel='Pokemon Primary Types', ylabel='Quantity')
BarT.set_title('Distribution of Primary Pokemon Types', fontsize=20)
FigBar = BarT.get_figure()
FigBar.savefig("Primary types distribution.png")

QE = Poke[['Type1', 'Attack', 'Defense']]

Type2 = pd.value_counts(Poke['Type2'])

dims = (15.0, 10.0)
fig, ax = plt.subplots(figsize=dims)
BarT = sb.barplot(x=Type2.index, y=Type2, data=Poke, palette=type2_colours, ax=ax)
BarT.set_xticklabels(BarT.get_xticklabels(), rotation=75, fontsize=11)
BarT.set(xlabel='Pokemon Secondary Types', ylabel='Freq')
BarT.set_title('Distribution of Secondary Pokemon Types', fontsize=18)
FigBar = BarT.get_figure()
FigBar.savefig("Secondary types distribution.png")

LSplit = [Poke['Name'].count(), PokeL['Name'].count()]
fig, ax = plt.subplots()
LegendPie = plt.pie(LSplit, labels=['Not Legendary', 'Legendary'], autopct='%1.1f%%', shadow=False, startangle=90,
                    explode=(0, 0))
plt.title('Legendary Split', fontsize=20)
fig = plt.gcf()
fig.set_size_inches(15, 10)
plt.savefig("LegendPie.png")



GenSplit = [Gen1['Type1'].count(), Gen2['Type1'].count(), Gen3['Type1'].count(), Gen4['Type1'].count(), Gen5['Type1'].count(), Gen6['Type1'].count()]
fig, ax = plt.subplots()
GenPie = plt.pie(GenSplit, labels=["First generation", "Secondary Generation", "Third Generation", "Fourth Generation", "Fith Generation", "Six Generation"], autopct='%1.1f%%', shadow=False, startangle=90)
plt.title('Generation Split', fontsize=12)
fig = plt.gcf()
fig.set_size_inches(11.7, 8.27)
plt.savefig("GenerationPie.png")

SpeedMean = Poke[['Type1', 'Speed']]

Corr = Poke[['Total', 'HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']]


dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=dims)
CorrelationMap = sb.heatmap(Corr.corr(), annot=True, ax=ax)
CorrelationMap.set(title='HeatMap to show Correlation between Base Stats')
FigMap = CorrelationMap.get_figure()
FigMap.savefig("HeatMapCorr.png")


DS = Corr.describe()
print("\n MEANS OF MAIN DESCRIPTIONS")
print(DS.mean())

EQ = Poke[['Type1', 'Defense', 'Attack']]

EQ = EQ.loc[(EQ['Defense'] - EQ['Attack'] < 10)]
#print(EQ)

print("\n Types in which defense approximately equal attack")
print(EQ['Type1'].value_counts())

TopTotal = Poke[['Name', 'Total']]
print("\n THE BEST OF THE BEST TOTAL POKEMON")
print(TopTotal.nlargest(1, 'Total'))
