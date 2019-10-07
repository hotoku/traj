import numpy as np
import pandas as pd

source_file="~/project/traj/db/df.csv"
df = pd.read_csv(source_file, index_col=0)[["id", "latitude", "longitude"]]
df.columns = ["user_id", "latitude", "longitude"]
df["id"] = np.arange(len(df))


dest_file="~/project/traj/db/table.csv"
df.to_csv(dest_file, columns=["id", "user_id", "latitude", "longitude"],
          index=False, header=False)
