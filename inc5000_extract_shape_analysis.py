import pandas as pd
import collections

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


extract_columns = ['inc5000companyId', 'rank', 'company',  # incID, rank, companyName
                   'industry', 'founded',  # industry, yrFounded
                   'raw_revenue', 'growth', 'workers', 'previous_workers',  # revenue, growth, workerCount
                   'state_s', 'city', 'zipcode',  # geographic information
                   'ifc_business_model', 'website',  # businessModel, website link
                   'yrs_on_list', 'name', 'ceo_gender', 'Year'  # additional information
                   ]

column_titles = collections.defaultdict(list)
summary_stats = collections.defaultdict(list)
df_shape = collections.defaultdict(list)
files_to_check = []


def file_details(data):

    for i in data:
        df = pd.read_csv(i)
        columns_count = "Col Count: " + str(len(df.columns))
        row_count = "Row Count: " + str(len(df.index))
        summary_stats[i].append(columns_count)
        summary_stats[i].append(row_count)
        column_titles[i].append(df.columns)
        df_shape[i].append(df.shape)

        for k in df.columns:
            if k not in extract_columns:
                key = str(i)+'//'+str(k)
                files_to_check.append(key)
            else:
                continue


file_details(data_files)

# print(column_titles)
# print(summary_stats)
# print(df_shape)
# print(files_to_check)


