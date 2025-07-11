import pandas as pd
from pathlib import Path

def load_data(country="benin"):
    """Load cleaned CSV from local data/ dir"""
    data_path = Path(__file__).parent.parent / "data" / "clean" / f"{country}_clean.csv"
    return pd.read_csv(data_path)

def filter_regions(df, metric="GHI", top_n=5):
    """Return top regions by selected metric"""
    return df.groupby("region")[metric].mean().nlargest(top_n).reset_index()
