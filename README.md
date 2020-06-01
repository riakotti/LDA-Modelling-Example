# LDA-Modelling-Example

I played with organizing a collection of recipes into different topics (text clustering). 

* Method: Latent Dirichlet Allocation - LDA (topic modeling algorithm)

* Output: LDA produced a list of topics (cluster of words) where each word in the cluster having a probability of occurrence for the given topic

A different approach would be to group recipes into different clusters based on some suitable similarity measure.  

* Method: KMeans clustering using TF-IDF (term frequency-inverse document frequency) weights

* Output: every recipe showing up in one of the clusters. 

## Scripts
* extract_recipes.py - randomly extract 100 recipes using [spoonacular API](https://spoonacular.com/food-api) (save recipes in a json file)
* text_utils.py - Preprocessing functions for text data
* LDA_text_model.py (class) - LDA preprocesses and algorithm
* load_recipes.py - apply LDA and Kmeans in those recipes
