"""
Google Immersive Product API: Batch Multi-Query Example
See more at: https://apify.com/johnvc/google-immersive-product-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-immersive-product-api/input-schema?fpr=9n7kx3

This script shows the batch capability of the Google Immersive Product API on
Apify: pass a list of product searches with the `queries` input and the Actor
pulls rich product pages for each in a single run, tagging every product with
the `query` it came from. That makes it easy to compare product categories side
by side. Inputs are kept small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from collections import defaultdict
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# This run uses the `queries` list to search several product categories at
# once. Each product row carries the `query` it came from. maxResultsPerQuery
# is kept small (3) to keep this first run inexpensive: you are billed per
# product page returned. Raise it or add queries once you know your budget.
run_input = {
    "queries": ["running shoes", "wireless earbuds"],
    "gl": "us",              # two-letter country code for pricing/localization
    "hl": "en",              # two-letter language code
    "maxResultsPerQuery": 3, # small on purpose to keep it cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-immersive-product-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} product(s) across {len(run_input['queries'])} queries.\n")

# Group the products by their source query so the batch structure is visible.
by_query = defaultdict(list)
for item in items:
    by_query[item.get("query", "")].append(item)

# Print a short report per query.
for query in run_input["queries"]:
    products = by_query.get(query, [])
    print(f"=== {query}: {len(products)} product(s) ===")
    for item in products:
        title = item.get("title", "")
        brand = item.get("brand", "")
        price = item.get("price_range", "")
        rating = item.get("rating")
        reviews = item.get("reviews")
        print(f"  {item.get('position')}. {title} ({brand})")
        print(f"     {price}, rated {rating} from {reviews} reviews")
    print()
