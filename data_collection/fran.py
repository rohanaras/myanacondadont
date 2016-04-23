import urllib
import json
import pandas as pd


def pull_data(start_year, end_year, save_file=None, debug=False):
    # find all trawl catch fact variables
    tcf_vars_url = 'https://www.nwfsc.noaa.gov/data/api/v1/source/trawl.catch_fact/variables'
    tcf_vars_response = urllib.urlopen(tcf_vars_url)
    tcf_vars_json = json.loads(tcf_vars_response.read())['variables']

    # get variables we want to keep
    kept_vars = []
    for var in tcf_vars_json:
        split_var = var.split('$')
        date_vars = ["date_dim", "most_recent_taxonomy_update_date_dim"]
        time_vars = ["sampling_end_time_dim", "sampling_start_time_dim"]
        if split_var[0] in date_vars:
            if split_var[1] == 'yyyymmdd':
                kept_vars.append(var)
        elif split_var[0] in time_vars:
            if split_var[1] == 'hh24miss':
                kept_vars.append(var)
        else:
            kept_vars.append(var)

    # split variable list into chunks of 10 and format into url
    n = 20
    tcf_vars_chunks = ['https://www.nwfsc.noaa.gov/data/api/v1/source/trawl.catch_fact/selection.json?filters=' +
                       'date_dim$year%3E=' + str(start_year) + ',date_dim$year%3C=' + str(end_year) + '&variables=' +
                       str(','.join(kept_vars[i:i+n])) for i in xrange(0, len(kept_vars), n)]

    if debug:
        print(tcf_vars_chunks)

    # read in json and convert to dataframes
    tcf_df_chunks = [pd.DataFrame(json.loads(urllib.urlopen(url).read())) for url in tcf_vars_chunks]

    final = pd.concat(tcf_df_chunks)

    if debug:
        print(final)

    if save_file is not None:
        final.to_csv(save_file, encoding='utf-8')

    return final


def push_data():
    pass


if __name__ == "__main__":
    print(pull_data(2010, 2012, "./2010-2012.csv", debug=True))
