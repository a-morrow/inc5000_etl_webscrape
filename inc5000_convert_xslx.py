import pandas as pd

data_files = [
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2010_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2011_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2012_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2013_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2014_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2015_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2016_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2017_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2018_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2019_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2020_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2021_inc5000_extract.csv',
    'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\2022_inc5000_extract.csv']

file_path = 'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\inc5000_extract_all.xlsx'
writer = pd.ExcelWriter(file_path)


def write_to_excel_sheets(data):
    for i in data:
        df = pd.read_csv(i)
        name = file_transform(i)
        df.to_excel(writer,sheet_name=name, index=False)
        print('Excel File Created')
    writer.save()


def file_transform(file):
    file_split = file.split("\\", 5)[-1]
    sheet_name = file_split[0:12]
    return sheet_name


# write_to_excel_sheets(data_files)
