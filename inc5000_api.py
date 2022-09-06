# Package Import
import requests
import time
import pandas as pd

# Global Vars
inc5000_url = "https://api.inc.com/rest/i5list/"
payload = ""
headers = {
    "authority": "api.inc.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.inc.com",
    "pragma": "no-cache",
    "referer": "https://www.inc.com/",
    "sec-ch-ua": "^\^Chromium^^;v=^\^104^^, ^\^"
}
extract_columns = ['inc5000companyId', 'rank', 'company',  # incID, rank, companyName
                   'industry', 'founded',  # industry, yrFounded
                   'raw_revenue', 'growth', 'workers', 'previous_workers',  # revenue, growth, workerCount
                   'state_s', 'city', 'zipcode',  # geographic information
                   'ifc_business_model', 'website',  # businessModel, website link
                   'yrs_on_list', 'name', 'ceo_gender'  # additional information
                   ]


def extract(year):
    results = []
    url = inc5000_url + str(year)
    response = requests.request("GET", url, data=payload, headers=headers)
    data = response.json()
    for i in data['companies']:
        results.append(i)

    return results


def transform(results, year):
    transformed_df_columns = []
    normalize_df = pd.json_normalize(results)
    columns = list(normalize_df.columns)
    for i in columns:
        if i in extract_columns:
            transformed_df_columns.append(i)
        else:
            continue

    transformed_df = normalize_df[transformed_df_columns]
    transformed_df.insert(loc=0, column='Year', value=year)

    return transformed_df


def load(df, year):
    df.to_csv(f"C:\\Users\\amorrow\\Documents\\inc5000_Extracts\\{year}_inc5000_extract.csv", index=False)


def main():
    for i in list(range(2010, 2023)):
        print('Program Executing\n')
        print(i, '\nBegin Data Extract:')
        extract_data = extract(i)
        print('End Extract')

        time.sleep(3)

        print('Begin Data Transform:')
        transform_data = transform(extract_data, i)
        print('End Transform')

        time.sleep(3)

        print('Start Data Load to CSV')
        load(transform_data, i)
        print('End Load')

        time.sleep(3)

        print('Finished Executing')

    return


if __name__ == "__main__":
    main()
