# CanadaComputersAPI
hawkhacks2022 entry

a RESTful API that scrapres data queried from Canada Computers' website

(frontend is kinda dead rn so focus on backend)

# installation / setup

clone repo
make a venv and install requirements:
`python -m venv env`
`./env/Scripts/activate`
`pip install -r requirements.txt`

# running the project
make sure ur in ur venv (you'll see `(env)` on the left of your prompt)
run the api server locally
`python backend/src/app.py`

access it via `localhost:5000` (should be a "page not found")
query Canada Computers with `localhost:5000/search/<SEARCH_STRING>`

price range:
`localhost:5000/search/<SEARCH_STRING>?price_min=<MIN>&price_max=<MAX>`
returns listings that return from the search query that are within the price range given

hawkhacks was fun
