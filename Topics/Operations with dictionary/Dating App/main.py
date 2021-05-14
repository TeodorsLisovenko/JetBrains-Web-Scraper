def select_dates(potential_dates):
    selection = {person["name"] for person in potential_dates if
                 person["age"] > 30 and "art" in person["hobbies"] and "Berlin" in person["city"]}

    return ", ".join(selection)
