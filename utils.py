import requests
import geopandas as gpd
import pandas as pd
import json


def API_to_df(dataset_id,format="json"):
    response_API = requests.get(f"https://data.economie.gouv.fr/api/v2/catalog/datasets/{dataset_id}/exports/{format}")
    data = response_API.json()
    if format == "geojson":
        with open(f"data/{dataset_id}.{format}","w") as outfile:
            json.dump(data, outfile)
        gdf = gpd.read_file(f"data/{dataset_id}.{format}")
        return gdf
    else:
        with open(f"data/{dataset_id}.json","w") as outfile:
            json.dump(data, outfile)
        df = pd.read_json(f"data/{dataset_id}.json")
        return df



if __name__ == "__main__":
    print(API_to_df("coordonnees-des-structures-dgfip","geojson").head())




