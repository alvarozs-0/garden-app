# garden_advice.py
"""Garden Advice Program"""

# Dictionary containing advice based on season and plant type
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


def get_season_advice(season):
    """
    Provides gardening advice based on the season.
    Args:
        season (str): The season entered by the user.
    """
    if season in advice["season"]:
        print("Advice for", season, "is:")
        print(advice["season"][season])

        print("Recommended plants for", season, "are:")
        for plant in advice["plant_type"]:
            print("-", plant)
    else:
        print("Invalid season.")


def get_plant_type_advice(plant_type):
    """
    Provides gardening advice based on the plant type.
    Args:
        plant_type (str): The plant type entered by the user.
    """
    if plant_type in advice["plant_type"]:
        print(advice["plant_type"][plant_type])
    else:
        print("Invalid plant type.")


def main():
    """
    Main function to run the Garden Advice Program.
    """
    # Get user input for season and provide advice
    season = input("Enter the season: ").lower()
    get_season_advice(season)

    print()

    # Get user input for plant type and provide advice
    plant_type = input("Enter the plant type: ").lower()
    get_plant_type_advice(plant_type)


# Entry point of the program
if __name__ == "__main__":
    main()
