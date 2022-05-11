import os
from serpapi import GoogleSearch
from google_scholar_profile_results import profile_results
from urllib.parse import urlsplit, parse_qsl
import pandas as pd
def author_results():
    print("extracting author results..")
    author_results_data = []
    for author_id in profile_results():
        print(f"Parsing {author_id['author_id']} author ID.")
        params = {
            "api_key": os.getenv("API_KEY"),      # SerpApi API key
            "engine": "google_scholar_author",    # author results search engine
            "author_id": author_id["author_id"],  # search query
            "hl": "en"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        thumbnail = results.get("author").get("thumbnail")
        name = results.get("author").get("name")
        affiliations = results.get("author").get("affiliations")
        email = results.get("author").get("email")
        website = results.get("author").get("website")
        interests = results.get("author").get("interests")
        cited_by_table = results.get("cited_by", {}).get("table")
        cited_by_graph = results.get("cited_by", {}).get("graph")
        public_access_link = results.get("public_access", {}).get("link")
        available_public_access = results.get("public_access", {}).get("available")
        not_available_public_access = results.get("public_access", {}).get("not_available")
        co_authors = results.get("co_authors")
        author_results_data.append({
          "thumbnail": thumbnail,
          "name": name,
          "affiliations": affiliations,
          "email": email,
          "website": website,
          "interests": interests,
          "cited_by_table": cited_by_table,
          "cited_by_graph": cited_by_graph,
          "public_access_link": public_access_link,
          "available_public_access": available_public_access,
          "not_available_public_access": not_available_public_access,
          "co_authors": co_authors
        })
    return author_results_data