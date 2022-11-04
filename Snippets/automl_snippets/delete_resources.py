# You must delete any `Model` resources deployed to the `Endpoint` resource 
# before deleting the `Endpoint` resource.

delete_training_job = True
delete_model = True
delete_endpoint = True

# Warning: Setting this to true will delete everything in your bucket
delete_bucket = False

# Delete the training job
petfinder_adoption_job.delete()

# Delete the model
petfinder_adoption_model.delete()

# Delete the endpoint
petfinder_adoption_endpoint.delete()

if delete_bucket and "BUCKET_NAME" in globals():
    ! gsutil -m rm -r $BUCKET_NAME