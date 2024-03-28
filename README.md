# capital-finder

## Example Links

- <https://capital-finder-psi-nine.vercel.app/api/capital-finder?capital=santiago>

- <https://capital-finder-psi-nine.vercel.app/api/capital-finder?country=chile>

- Replace (santiago) with any capital to know the country

- Replace (chile) with any country to know capital

## Overview

This serverless function provides information about countries and their capitals based on user queries. It's built using Python's http.server module and utilizes data from the [Rest Countries API](https://restcountries.com).

## Usage

### Sending GET Requests

To retrieve information about a country or its capital, send a GET request to the serverless function with the following parameters:

- `country`: To get the capital of a specific country.
- `capital`: To get the country associated with a specific capital.

### Example

```,
GET /?country=France
```

This request will return the capital of France.

```,
GET /?capital=Paris
```

This request will return the country accosiciated with the capital Paris.
