import pandas


def sort(file):
    df = pandas.read_csv(file,delimiter=';' ,index_col='Code_commune_INSEE')
    List =[]
    for index , row in df.iterrows():
        if index[:2] not in ['2A' , '2B']:
            List.append(f"{index}  {row['Nom_commune']}")
    # This value of i corresponds to how many values were sorted
    for i in range(len(List)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(List)):
            if int(List[j][:2]) < int(List[lowest_value_index][:2]):
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        List[i], List[lowest_value_index] = List[lowest_value_index], List[i]
        print(List[i]+ "  "+ List[lowest_value_index])
    for index, row in df.iterrows():
        if index[:2] == '2A':
            List.append(f"{index}  {row['Nom_commune']}")
    for index, row in df.iterrows():
        if index[:2] == '2B':
            List.append(f"{index}  {row['Nom_commune']}")
    with open('Sorted_file.txt', 'w') as Dt :
        Dt.write('Code_commune_INSEE  Nom_commune\n')
        for x in range(len(List)):
            #print(List[x] + '\n')
            Dt.write(List[x] + '\n')
    return 'Sorted_file.txt'


def combine(file1, file2):
    df1 = pandas.read_csv(file1, delimiter=';',index_col='Code INSEE Département')
    df2 = pandas.read_csv(file2, delimiter='  ', index_col='Code_commune_INSEE')
    List1=[]
    for x in range (100):
        if x in range(11):
            List1.append(f'0{x}')
        else:
            List1.append(f'{x}')
    List1.append('2A')
    List1.append('2B')
    List2=[]
    for x in range(1000):
        if (x >969):
            List2.append(f'{x}')
        else:
            pass
    Data_file = open(r'DataBase.txt', 'a') #file for the final database to be used
    for index2 , row2 in df2.iterrows():
        if (index2[:2] in List1) and (index2[:2] not in ['97', '98']):
           for index1, row1 in df1.iterrows():
                if (index1[:2] == index2[:2]) :
                    print((f"{index1}  {index2}  {row1['Nom Département']}  {row2['Nom_commune']}\n"))
                    Data_file.write(f"{index1}  {index2}  {row1['Nom Département']}  {row2['Nom_commune']}\n")
                else:
                    pass
        elif (index2[:3] in List2):
            for index1, row1 in df1.iterrows():
                if (index1[:3] == index2[:3]):
                    print((f"{index1}  {index2}  {row1['Nom Département']}  {row2['Nom_commune']}\n"))
                    Data_file.write(f"{index1}  {index2}  {row1['Nom Département']}  {row2['Nom_commune']}\n")
                else:
                    pass
    Data_file.close()
    with open('DataBase.txt') as DataBase:
        DB = DataBase.read()
        print(DB)

if __name__ == '__main__':
    sort('laposte_hexasmal.csv')
    combine('code-officiel-geographique-2019-regions-et-departement.csv','Sorted_file.txt')
