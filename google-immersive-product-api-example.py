"""
Google Immersive Product API: A Quick Start Example
See more at: https://apify.com/johnvc/google-immersive-product-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-immersive-product-api/input-schema?fpr=9n7kx3

This script shows how to call the Google Immersive Product API on Apify from
Python and read its structured JSON output. It returns Google's rich product
detail pages for a product search. Inputs are kept small so your first call
stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one query, 3 products) to keep this first run
# inexpensive: you are billed per product page returned.
run_input = {
    "query": "running shoes",
    "gl": "us",
    "maxResultsPerQuery": 3,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-immersive-product-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} product(s).\n")

# Show each product with its key fields.
for item in items:
    title = item.get("title", "")
    brand = item.get("brand", "")
    price = item.get("price_range", "")
    rating = item.get("rating")
    reviews = item.get("reviews")
    print(f"{item.get('position')}. {title} ({brand})")
    print(f"   {price}, rated {rating} from {reviews} reviews\n")
