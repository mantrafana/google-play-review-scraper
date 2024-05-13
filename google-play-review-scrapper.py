import os
from google_play_scraper import Sort, reviews, reviews_all
import pandas as pd

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the app package name
app_package = 'id.kubuku.bintangpusnas'

# Initialize result list
result = []

# Scrap reviews
batch_number = 1
continuation_token = None
reviews_batch, continuation_token = reviews(
    app_package,
    lang='id',  #Defaults to 'en'
    country='id',  #Defaults to 'us'
    sort=Sort.MOST_RELEVANT,  #Defaults to Sort.MOST_RELEVANT, change to Sort.NEWEST for recent review
    filter_score_with=None,  #Default None, other value: 1, 2, 3, 4, 5
    count=170,  #Default 100 
    continuation_token=continuation_token
)

result.extend(reviews_batch)
fetched_reviews_count = len(result)
print(f"Fetched {fetched_reviews_count} reviews (Batch {batch_number})")

# Convert the result to a DataFrame
df = pd.DataFrame(result)

# Print the number of reviews scraped
print(f"Scrapped {fetched_reviews_count} reviews in total")

# Save the DataFrame to a CSV file in the same folder as the script
csv_path = os.path.join(script_dir, f'{app_package}_reviews.csv')
df.to_csv(csv_path, index=False)

print(f"All reviews saved to: {csv_path}")