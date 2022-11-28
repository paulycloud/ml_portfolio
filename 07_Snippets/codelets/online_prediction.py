petfinder_adoption_prediction = petfinder_adoption_endpoint.predict(
    [
        {
            "Type": "Cat",
            "Age": "3",
            "Breed1": "Tabby",
            "Gender": "Male",
            "Color1": "Black",
            "Color2": "White",
            "MaturitySize": "Small",
            "FurLength": "Short",
            "Vaccinated": "No",
            "Sterilized": "No",
            "Health": "Healthy",
            "Fee": "100",
            "PhotoAmt": "2",
        }
    ]
)
print(petfinder_adoption_prediction)
