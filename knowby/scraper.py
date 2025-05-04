import requests
import pandas as pd
import json
from keys import X_API_KEY, X_MEMBER_ID, X_ORGANISATION_ID

# --- PUBLISHED ---
url_published = "https://knowby-pro-backend-prod-qt5p6426oq-ts.a.run.app/api/knowby/published/f3a08168-af81-4719-9c23-daccaa827dbb?skip=0&take=24&sort=last_updated_at_utc&ascending=false&query="

headers_published = {
    "X-Api-Key": X_API_KEY,
    "X-Member-Id": X_MEMBER_ID,
    "X-Organisation-Id": X_ORGANISATION_ID,
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://knowby.pro",
    "Referer": "https://knowby.pro/",
    "Accept": "*/*",
    "Content-Type": "application/json",
}

response_published = requests.post(url_published, headers=headers_published)

data_published = response_published.json()
collection_published = data_published.get("collection", [])
df_published = pd.DataFrame(collection_published)
df_published_clean = df_published[["id", "title", "created_by_member_name", "visibility", "estimated_time_in_seconds", "last_updated_at_utc"]]
print(df_published_clean.head())

df_published.to_csv("published.csv", index=False)





# --- COMPLETIONS ---
headers_completions = {
    "X-Api-Key": X_API_KEY,
    "X-Member-Id": X_MEMBER_ID,
    "X-Organisation-Id": X_ORGANISATION_ID,
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://knowby.pro",
    "Referer": "https://knowby.pro/",
    "Accept": "*/*",
    "Content-Type": "application/json",
}

import requests
import pandas as pd

# Dictionaries to store data
df_views_dict = {}
df_completions_dict = {}
ratings_dict = {}

# Base URLs
base_view_url = "https://knowby-pro-backend-prod-qt5p6426oq-ts.a.run.app/api/knowbyview/latest/"
base_completion_url = "https://knowby-pro-backend-prod-qt5p6426oq-ts.a.run.app/api/knowbycompletion/latest/"
base_rating_url = "https://knowby-pro-backend-prod-qt5p6426oq-ts.a.run.app/api/knowbyrating/ratingcounts/"

params = "?skip=0&take=25"

for _, row in df_published_clean.iterrows():
    instruction_id = row['id']
    title = row['title']
    safe_title = ''.join(e for e in title if e.isalnum() or e == '_').replace(' ', '_')

    print(f"\n🔹 Processing: {title}")

    # --- Views ---
    url_views = f"{base_view_url}{instruction_id}{params}"
    res_views = requests.get(url_views, headers=headers_completions)
    if res_views.status_code == 200:
        df_views = pd.DataFrame(res_views.json().get("collection", []))
        df_views_dict[safe_title] = df_views
        print(f"📊 Views for {title}:")
        print(df_views.head())
    else:
        print(f"⚠️ Failed to fetch views for {title}")

    # --- Completions ---
    url_completions = f"{base_completion_url}{instruction_id}{params}"
    res_completions = requests.get(url_completions, headers=headers_completions)
    if res_completions.status_code == 200:
        df_completions = pd.DataFrame(res_completions.json().get("collection", []))
        df_completions_dict[safe_title] = df_completions
        print(f"📈 Completions for {title}:")
        print(df_completions.head())
    else:
        print(f"⚠️ Failed to fetch completions for {title}")

    # --- Ratings ---
    url_rating = f"{base_rating_url}{instruction_id}"
    res_ratings = requests.get(url_rating, headers=headers_completions)
    if res_ratings.status_code == 200:
        ratings_data = res_ratings.json()
        ratings_dict[safe_title] = ratings_data
        print(f"⭐ Ratings for {title}:")
        print(ratings_data)
    else:
        print(f"⚠️ Failed to fetch ratings for {title}")












"""# --- COMPLETIONS ---
url_completions = "https://knowby-pro-backend-prod-qt5p6426oq-ts.a.run.app/api/knowbycompletion/latest/{{ published_ids }}?skip=0&take=25"

headers_completions = {
    "X-Api-Key": X_API_KEY,
    "X-Member-Id": X_MEMBER_ID,
    "X-Organisation-Id": X_ORGANISATION_ID,
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://knowby.pro",
    "Referer": "https://knowby.pro/",
    "Accept": "*/*",
    "Content-Type": "application/json",
}

response_completions = requests.get(url_completions, headers=headers_completions)
print("Completions status:", response_completions.status_code)

data_completions = response_completions.json()
collection_completions = data_completions.get("collection", [])
df_completions = pd.DataFrame(collection_completions)
print(df_completions.head())

df_completions.to_csv("completions.csv", index=False)"""
