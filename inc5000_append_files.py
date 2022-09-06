import pandas as pd
file_path = 'C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\inc5000_appended_extract.csv'
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


def append_data(data_files):
    combined_files = pd.concat(map(pd.read_csv,data_files),ignore_index=True)
    combined_files.to_csv(file_path,index=False)
    return


# append_data(data_files)
