import csv
import math


def get_data(file):
	with open(file) as data_file:
		reader = csv.DictReader(data_file)
		objects = [row for row in reader]

	print("Done!")
	print("Found " + str(len(objects)) + " objects.")

	return objects


def create_json():
	"""
	Takes an area key and returns the sum of the number of males, females (and the total),
	:param
	:return: MaleColour, FemaleColour, TotalColour
	"""

	colours_dict = {}
	objects = get_data('data.csv')

	# Get list of GeoCodes
	geo_code_list = []
	for obj in objects:
		geo_code_list.append(obj["GEOGRAPHY_CODE"])
	geo_code_list = list(set(geo_code_list))

	# Get total number of males and females
	total_male_list = []
	total_female_list = []
	total_list = []

	print("Finding max male/female values...")
	for obj in objects:
		if "All" in obj["AGE_NAME"] and obj["GENDER_NAME"] == "Male":
			total_male_list.append(int(obj["OBS_VALUE"]))
		elif "All" in obj["AGE_NAME"] and obj["GENDER_NAME"] == "Female":
			total_female_list.append(int(obj["OBS_VALUE"]))
		elif "All" in obj["AGE_NAME"] and obj["GENDER_NAME"] == "Total":
			total_list.append(int(obj["OBS_VALUE"]))

	male_max = max(total_male_list)
	female_max = max(total_female_list)
	total_max = max(total_list)

	print("Finding colour values...")
	# Find male/female colour values
	for geo_code in geo_code_list:
		male_value_list = []
		female_value_list = []

		for obj in objects:
			if obj["GEOGRAPHY_CODE"] == geo_code and "All" in obj["AGE_NAME"] and obj["GENDER_NAME"] == "Male":
				male_value_list.append(int(obj["OBS_VALUE"]))
			elif obj["GEOGRAPHY_CODE"] == geo_code and "All" in obj["AGE_NAME"] and obj ["GENDER_NAME"] == "Female":
				female_value_list.append(int(obj["OBS_VALUE"]))

		male_value = sum(male_value_list)
		female_value = sum(female_value_list)
		total_value = male_value + female_value

		male_colour = math.floor(255 * male_value / male_max)
		female_colour = math.floor(255 * female_value / female_max)
		total_colour = math.floor(255 * total_value / total_max)

		colours_dict[geo_code] = {
			"male_colour": male_colour,
			"female_colour": female_colour,
			"total_colour": total_colour,
		}

	print("Done!")


if __name__ == "__main__":
	create_json()
