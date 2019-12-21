import pandas as pd # To read csv
import re # Regex
import seaborn as sb # Statistical data visualization
import matplotlib.pyplot as plt


# Получаем файл и вытаскиваем данные
frame = pd.read_csv('data.csv') # Копируем данные в датафрейм

###### Переименовываем назавания ######
frame = frame.set_index('#')
frame.columns = ['Name','Type1', 'Type2','Total', 'HP', 'Attack','Defense','Sp.Atk','Sp.Def','Speed', 'Generation', 'Legendary']
##### Названия перед Mega и Primal удаляем для удобства.  переименовываем HoopaHoopa в Hoopa#####
frame.Name = frame.Name.apply(lambda x: re.sub(r'(.+)(Mega.+)',r'\2',x))
frame.Name = frame.Name.apply(lambda x: re.sub(r'(.+)(Primal.+)',r'\2',x))
frame.Name = frame.Name.apply(lambda x: re.sub(r'(HoopaHoopa)(.+)','Hoopa'+r'\2',x))

#### Удаляем лишные пробелы и наименования
All = frame.loc[(frame['Name'].str.contains('Mega ')==False) & (frame['Name'].str.contains('Primal')==False)] # фильтруем всех покемонов по Mega и Primal
Poke = All.loc[(All['Legendary']==False)]
PokeL = All.loc[(All['Legendary']==True)]

# Save all values to key-value map for next using in Plots
KeyValueMap = {}
Speed = frame.loc[ : , ['Type1', 'Speed']]
Speed.to_string(index=False)

SelectedType = Speed.loc[(Speed['Type1'].str.contains('Grass') == True)]

print(Speed)


for speed in SelectedType['Speed']:
    print("Speed: ", speed)

Poke['Type1'].count() - Poke['Type2'].count() #  Считаем покемонов только с основным типом

###### Покемоны умеют становиться старше и мощнее. Делаем выборку в один датасет ####
Gen1 = Poke.loc[Poke['Generation'] == 1]
Gen2 = Poke.loc[Poke['Generation'] == 2]
Gen3 = Poke.loc[Poke['Generation'] == 3]
Gen4 = Poke.loc[Poke['Generation'] == 4]
Gen5 = Poke.loc[Poke['Generation'] == 5]
Gen6 = Poke.loc[Poke['Generation'] == 6]


# Вывод 3 топ самых быстрых

Top3Max = frame.loc[: , ['Name', 'Speed']]

print("TOP 3 the Fastest")
print(Top3Max.nlargest(3, 'Speed'))

# TOP 10 HP

Top10Max = frame.loc[: , ['Name', 'HP']]

print("\n TOP 10 of Healthiest")
print(Top10Max.nlargest(10, 'HP'))