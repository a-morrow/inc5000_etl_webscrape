import pandas as pd
file_path = 'desired_file_path.csv'
data_files = [
    'filepath\\file1.csv',
    'filepath\\file2.csv',
    'filepath\\file3.csv',
    'filepath\\file4.csv',
    'filepath\\file5.csv',
    'filepath\\file6.csv',
    'filepath\\file7.csv',
    'filepath\\file8.csv',
    'filepath\\file9.csv',
    'filepath\\file10.csv',
    'filepath\\file11.csv',
    'filepath\\file12.csv',
    'filepath\\file13.csv']


def append_data(data_files):
    combined_files = pd.concat(map(pd.read_csv,data_files),ignore_index=True)
    combined_files.to_csv(file_path,index=False)
    return


# append_data(data_files)
