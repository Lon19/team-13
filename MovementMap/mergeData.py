import json

from read_csv import create_json


def merge(d):
    # input a dictionary, output a new json file which combines both the necessary data

    # build a dictionary based on the current geography data
    finaldict = dict()

    with open('../wards.json') as f:
        txt = f.read()
        text = json.loads(txt)
        wards = text["features"]
        for entry in wards:
            geo_code = entry["properties"]["wd16cd"]
            finaldict[geo_code] = {"name": entry["properties"]["wd16nm"], "geometry": entry["geometry"]}

    # add the input data into the dictionary
    for key in d.keys():
        if key in finaldict.keys():
            finaldict[key]["male_colour"] = d[key]["male_colour"]
            finaldict[key]["female_colour"] = d[key]["female_colour"]
            finaldict[key]["total_colour"] = d[key]["total_colour"]

    with open('result.json', 'w') as fp:
        json.dump(finaldict, fp)

    return finaldict


if __name__ == "__main__":
    d = create_json()
    finaldic = merge(d)
    print(finaldic)
