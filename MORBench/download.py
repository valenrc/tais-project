# script para descargar MORBbench y PolyRefuse y guardarlo en el mismo directorio de este script
# hf://datasets/Aaron-Pan/MORBench/morbench.csv

import pandas as pd

if __name__ == "__main__":
    morbench_url = "https://huggingface.co/datasets/Aaron-Pan/MORBench/resolve/main/morbench.csv"
    morbench_df = pd.read_csv(morbench_url)
    morbench_df.to_csv("morbench.csv", index=False)