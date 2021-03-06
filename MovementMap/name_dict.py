import json


def get_name_dict():

    # create an empty dictionary
    name_dict = dict()

    # load original json file as a dictionary
    with open('result.json') as f:
        txt = f.read()
    text = json.loads(txt)
    wards = text["features"]
    # loop through all the wards to add entries into name_dict map
    for entry in wards:
        name = entry["properties"]["wd16nm"]
        if "total_value" in entry["properties"].keys():
            name_dict[name] = {}
            name_dict[name]["Name"] = name
            name_dict[name]["Male"] = entry["properties"]["male_value"]
            name_dict[name]["Female"] = entry["properties"]["female_value"]
            name_dict[name]["Total"] = entry["properties"]["total_value"]

    return name_dict


if __name__ == "__main__":
    result = get_name_dict()
    print(result)


