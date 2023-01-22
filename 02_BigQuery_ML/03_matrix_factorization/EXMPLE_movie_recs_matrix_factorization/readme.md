# 05: Creating a matrix factorization model to make movie recommendations

This project used a matrix factorization model in BigQuery ML to generate movie recommendations for a user using the public movielens dataset. This dataset contains explicit feedback data given a movie ID and User ID. The recommendation is based on rating scale (1-5), genre and other metadata info. The user_id and movie_id ratings dataset has 1,000,209 rows. The movie titles dataset has 3,883 rows. 


## Key Concepts: 
- Matrix Factorization
- ML.RECOMMEND 
- ML.WEIGHTS

## Objective
- Create an explicit recommendations model using the CREATE MODEL statement 
- Use the ML.EVALUATE function to evaluate the ML Models 
- Use the ML.WEIGHTS function to inspect the latent factor weights generated during training 
- Use the ML.RECOMMEND function to produce recommendations for a user. 
 
## Steps
- Create the dataset & load the dataset into BQ
- Use the SELECT statement to examine the data 
- Use the CREATE MODEL statement to create the explicit recommendation model. 
- Use the ML.EVALUATE function to evaluate the model data
- Use the ML.PREDICT function to predict the ratings and make recommendations
- Use the ML.RECOMMEND function to fetch all the ratings for the user-item pairs
- Save the recommendation predictions to a table
- Generate the top 5 recommendations per user. 

--------------------------------------------------------------------------------

_Let's connect and chat! Open to anyone on Earth under the Sun and Moon._

[![](https://github.com/paulycloud/paulycloud/blob/main/assets/twitter.png)](https://twitter.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/linkedin.png)](https://www.linkedin.com/in/paulmkamau/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/insta.png)](https://www.instagram.com/paulykamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/behance.png)](https://www.behance.net/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dribbble.png)](https://dribbble.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/facebook.png)](https://www.facebook.com/paul.m.kamau.3/) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/github.png)](https://github.com/paulycloud) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/medium.png)](https://medium.com/@paulkamau) [![](https://github.com/paulycloud/paulycloud/blob/main/assets/dev.png)](https://dev.to/paulycloud)