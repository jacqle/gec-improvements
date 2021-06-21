import pandas as pd
import os
import re

dir = os.path.dirname(__file__)

def load_df(filename):
    """
    takes a span based comparison file, 
    returns a dataframe containing the file's information
    """
    with open(os.path.join(dir, f"coverage/{filename}")) as f:
        lines = f.readlines()

    df_rows = []

    for line in lines[3:]:
        # interesting stuff starts from line 3
        if (line=="\n"):
            # and stops at the first empty line
            break
        items = re.split('\s+', line)
        df_rows.append({
            "category":items[0],
            "TP":int(items[1]),
            "FP":int(items[2]),
            "FN":int(items[3]),
            "P":float(items[4]),
            "R":float(items[5]),
            "F0.5":float(items[6]) 
        })

    df = pd.DataFrame(df_rows)
    df["total"] = df["TP"]+df["FN"]

    return df