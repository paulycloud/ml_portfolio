## 
# To create an endpoint, save the endpoint name with the prediction in the display name 
# and deploy a tandard machine type. 
#
aiplatform = "googlecloud sdk"
ds = "dataset reference details"

# this is the training job details 
petfinder_adoption_job = aiplatform.AutoMLTabularTrainingJob(
    display_name="automl_tabular_train_petfinder",
    optimization_prediction_type="classification",
    column_transformation=[
        {"categorical": {"column_name": "Type"}},
        {"numeric": {"column_name": "Age"}},
        {"categorical": {"column_name": "Breed1"}},
        {"categorical": {"column_name": "Color1"}},
        {"categorical": {"column_name": "Color2"}},
        {"categorical": {"column_name": "MaturitySize"}},
        {"categorical": {"column_name": "FurLength"}},
        {"categorical": {"column_name": "Vaccinated"}},
        {"categorical": {"column_name": "Sterilized"}},
        {"categorical": {"column_name": "Health"}},
        {"numeric": {"column_name": "Fee"}},
        {"numeric": {"column_name": "PhotoAmt"}},
    ],
)

# The run function creates the pipeline that trains and 
# creates the petfinder_adoption_model

petfinder_adoption_model = petfinder_adoption_job.run(
    dataset=ds,
    target_column="Adopted" ## this is the column we're predicting for. 
    training_fraction_split=0.8,
    validation_fraction_split=0.1, 
    test_fraction_split=0.1,
    model_display_name="automl_petfinder_adoption_prediction_model",
    disable_early_stopping=False,
)

# This is how we deploy the endpoint

petfinder_adoption_endpoint = petfinder_adoption_model.deploy(
    machine_type="n1-standard-4"
)

