import pandas as pd


def csv_feature(path:str):
    def inner_fn(fn):
        def inner(domain):
            return fn(pd.read_csv(path))
        return inner
    return inner_fn

def tsv_feature(path:str):
    def inner_fn(domain):
        def inner(domain):
            return pd.read_csv(path, sep='\t')
        return inner
    return inner_fn


def parquet_feature(path:str):
    def inner_fn(domain):
        def inner(domain):
            return pd.read_parquet(path)
        return inner
    return inner_fn