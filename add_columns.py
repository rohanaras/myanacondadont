import pandas as pd

#read file
def add_sources(csvfile, output_file):
    df = pd.read_csv(csvfile)

    #counts number of rows
    rows = len(df.index)

    #create DataFrame with source
    source = []
    for x in range(rows):
        source.append('rutgers')
    df['source'] = pd.Series(source, index=df.index)

    #write to file
    df.to_csv(output_file)

if __name__ == "__main__":
    add_sources('C:\Users\Emily Zhai\Desktop\\foods.csv', 'C:\Users\Emily Zhai\Desktop\\source_added.csv')