# garden_advice.py
"""Garden Advice Program"""

advice = {
    "season": {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Time to plant new seeds and prepare the soil.",
        "autumn": "Harvest your crops and prepare for the colder months."
    },
    "plant_type": {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests.",
        "herb": "Prune regularly to promote growth.",
        "tree": "Ensure proper watering and check for diseases."
    }
}


season = input("Enter the season: ").lower()


if season in advice["season"]:
    print("Advice for", season, "is:")
    print(advice["season"][season])

    print("Recommended plants for", season, "are:")
    for plant in advice["plant_type"]:
        print("-", plant)
else:
    print("Invalid season.")


print()

plant_type = input("Enter the plant type: ").lower()


if plant_type in advice["plant_type"]:
    print(advice["plant_type"][plant_type])
else:
    print("Invalid plant type.")


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
