import pandas


def sort(file1, file2):
# Sorting laposte_hexasmal.csv
    df1 = pandas.read_csv(file1, delimiter=';', index_col='Code_commune_INSEE')
    List = []
    for index, row in df1.iterrows():
        if index[:2] not in ['2A', '2B']:
            List.append(f"{index}  {row['Nom_commune']}")
    # Sorting using the Sorting by selection method :
    # This value of i corresponds to how many values were sorted
    for i in range(len(List)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(List)):
            if int(List[j][:3]) < int(List[lowest_value_index][:3]):
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        List[i], List[lowest_value_index] = List[lowest_value_index], List[i]
        print(List[i] + "  " + List[lowest_value_index] + '\n')

    # Adding Corsica's communes :
    for index, row in df1.iterrows():
        if (index[:2] == '2A'):
            List.append(f"{index}  {row['Nom_commune']}")
    for index, row in df1.iterrows():
        if index[:2] == '2B':
            List.append(f"{index}  {row['Nom_commune']}")
    # Writing everything to new file
    with open('file1_Sorted.txt', 'w' , encoding='iso-8859-1') as Dt1:
        Dt1.write('Code_commune_INSEE  Nom_commune\n')
        for x in range(len(List)):
            Dt1.write(List[x] + '\n')

# Sorting code-officiel-geographique-2019-regions-et-departement.csv
    df2 = pandas.read_csv(file2, delimiter=';', index_col='Code INSEE Département')
    List1 = []
    for index, row in df2.iterrows():
        if index[:2] not in ['2A', '2B']:
            List1.append(f"{index}  {row['Nom Département']}")
    # Sorting using the Sorting by selection method :
    # This value of i corresponds to how many values were sorted
    for i in range(len(List1)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(List1)):
            if int(List1[j][:2]) < int(List1[lowest_value_index][:2]):
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        List1[i], List1[lowest_value_index] = List1[lowest_value_index], List1[i]
        print(List1[i] + "  " + List1[lowest_value_index] + '\n')
    #finding first index in list with a department code corresponding to a DOM-TOM region
    for i in range(len(List1)):
        if (List1[i][:2] in ['97' , '98']):
            Index_DOM_TOM = i
            break
    #Sorting DOM-TOM region codes
    for i in range(Index_DOM_TOM, len(List1)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(List1)):
            if int(List1[j][:3]) < int(List1[lowest_value_index][:3]):
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        List1[i], List1[lowest_value_index] = List1[lowest_value_index], List1[i]
        print(List1[i] + "  " + List1[lowest_value_index] + '\n')

    for index, row in df2.iterrows():
        if (index[:2] in ['2A' , '2B'] ):
            List1.append(f"{index}  {row['Nom Département']}")

    with open('file2_Sorted.txt', 'w' , encoding='iso-8859-1') as Dt2:
        Dt2.write('Code_Departement  Nom_Departement\n')
        for x in range(len(List1)):
            Dt2.write(List1[x] + '\n')

    return 'file2_Sorted.txt' , 'file1_Sorted.txt'


def combine(file1, file2):
    df1 = pandas.read_csv(file1, delimiter='  ',index_col='Code_Departement', encoding='iso-8859-1')
    df2 = pandas.read_csv(file2, delimiter='  ', index_col='Code_commune_INSEE', encoding='iso-8859-1')

    Data_file = open(r'DataBase.txt', 'a') #file for the final database to be used
    for index1, row1 in df1.iterrows():
        if (index1[:2] not in ['97','98', '2A' , '2B']):
            for index2 , row2 in df2.iterrows():
                if (index1[:2] == index2[:2]):
                    print((f"{index1}  {index2}  {row1['Nom_Departement']}  {row2['Nom_commune']}\n"))
                    Data_file.write(f"{index1}  {index2}  {row1['Nom_Departement']}  {row2['Nom_commune']}\n")
        elif (index1[:2] in ['97','98']):
            for index2, row2 in df2.iterrows():
                if (index1[:3] == index2[:3]):
                    print((f"{index1}  {index2}  {row1['Nom_Departement']}  {row2['Nom_commune']}\n"))
                    Data_file.write(f"{index1}  {index2}  {row1['Nom_Departement']}  {row2['Nom_commune']}\n")
        elif (index1[:2] in ['2A' , '2B'] ) :
            for index2, row2 in df2.iterrows():
                if (index1[:2] == index2[:2]):
                    print((f"{index1}  {index2}  {row1['Nom_Departement']}  {row2['Nom_commune']}\n"))
                    Data_file.write(f"{index1}  {index2}  {row1['Nom_Departement']}  {row2['Nom_commune']}\n")

    Data_file.close()
    with open('DataBase.txt') as DataBase:
        DB = DataBase.read()
        print(DB)

if __name__ == '__main__':
    sort('laposte_hexasmal.csv','code-officiel-geographique-2019-regions-et-departement.csv' )
    combine('file2_Sorted.txt','file1_Sorted.txt')


