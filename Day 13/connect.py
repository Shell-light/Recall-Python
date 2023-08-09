import requests
import pprint
import pandas as pd
api_key = "90782ca4cecca6f56d764343b58b5cd8"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MDc4MmNhNGNlY2NhNmY1NmQ3NjQzNDNiNThiNWNkOCIsInN1YiI6IjY0ZDBiZmE2ZDlmNGE2MDNiYWZiNGIxZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.i-KyjvzxVYGuQoHtjqCFoZKGf6LbFQ2ntUPx18FWfPk"
# HTTP  requests
"""
GET -> grap data
POST -> add/update data

PATCH
PUT
DELETE

"""

# what's our endpoint (or a url)?

# what is  the HTTP method that we need?

"""
Endpoint    
/movie/{movie_id}
curl --request GET \
https://api.themoviedb.org/3/movie/11?api_key=89ff7788bbc33b9bb8cf83d5ef5aa8fd
"""
movie_id = 11
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&page=1"
# print(endpoint)
# r = requests.get(endpoint) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)


# using v4
movie_id = 11
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers = {
    'Authorization' : f"Bearer {api_key_v4}",
    "accept": 'application/json'
}
# r = requests.get(endpoint, headers=headers) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)

movie_id = 11
api_version = 3 # both version same
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))
output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)


df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)