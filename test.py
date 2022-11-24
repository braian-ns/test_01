import requests


def greet(person):
    tests = "fefef"
    greeting = f"hello {person}"
    return greeting


api_key = "f59f1b96f2cfbcb2d9c8409ee4cb6453"
token = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNTlmMWI5NmYyY2ZiY2IyZDljODQwOWVlNGNiNjQ1MyIsInN1YiI6IjYxOWJhYzcyNTJkYzdmMDAyYWJmNzdmZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oK2YS1VzYWSCvHtpX1uBA0kmR7AH8QYRM05E5mZwjZE"
headers = {
    "Authorization": token,
    "Content-Type": "application/json;charset=utf-8",
}
url = f"https://api.themoviedb.org/3/movie/478434?api_key=<<api_key>>&language=en-US"
tmdb_search_2 = requests.request("GET", url, headers=headers)

g = greet("BRAIAN")

print(tmdb_search_2.json())
print(g)
