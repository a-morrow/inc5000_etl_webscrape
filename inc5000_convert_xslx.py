import pandas as pd

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


file_path = 'desired_file_path.xlsx'
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
