import pandas as pd


# データベース名からPropertiesを得る
def get_properties(dbname: str) -> dict[str, str]:
    filename = dbname + ".txt"
    prop = pd.read_csv(filename, sep="=", header=None,
                       names=['mailaddr', 'username'])
    prop = {k: v for k, v in zip(prop.mailaddr, prop.username)}
    return prop
