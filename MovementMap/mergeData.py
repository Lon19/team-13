import json

from read_csv import create_json


def merge(d):
    # input a dictionary of id mapping to number of people, update the original geo json file

    # load original json file as a fictionary
    with open('../wards.json') as f:
        txt = f.read()
        text = json.loads(txt)
        wards = text["features"]
        for entry in wards:
            geo_code = entry["properties"]["wd16cd"]

            # add colour data into the original dictionary
            if geo_code in d.keys():
                entry["properties"]["male_colour"] = d[geo_code]["male_colour"]
                entry["properties"]["female_colour"] = d[geo_code]["female_colour"]
                entry["properties"]["total_colour"] = d[geo_code]["total_colour"]
                entry["properties"]["male_value"] = d[geo_code]["male_value"]
                entry["properties"]["female_value"] = d[geo_code]["female_value"]
                entry["properties"]["total_value"] = d[geo_code]["total_value"]

    # convert the dictionary into a json file
    with open('result.json', 'w') as fp:
        json.dump(text, fp)

if __name__ == "__main__":
    d = create_json()
    merge(d)
