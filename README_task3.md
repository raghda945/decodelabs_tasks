# Movie Recommendation System

## Project Overview
This project implements a simple recommendation system that suggests movies based on user preferences. The system analyzes movie information from a dataset and provides recommendations according to the selected genre.

## Objectives
- Collect user preferences
- Match user interests with movie attributes
- Generate recommendations

## Features
- Reads movie dataset
- Accepts user input
- Filters movies by genre
- Displays recommended movies

## Technologies Used
- Python
- Pandas
- OpenPyXL

## Dataset
Movie dataset containing information such as:
- Movie Title
- Genre
- Rating
- Release Year

## Project Structure

project_3/
│
├── recommendation.py
├── README.md
├── requirements.txt
└── movies_dataset.csv.xlsx

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the project

```bash
python recommendation.py
```

## Example

Input:

```
Action
```

Output:

```
Recommended Movies:
Movie 1
Movie 2
Movie 3
```

## Learning Outcomes
- Recommendation Systems
- Pattern Matching
- User Preference Analysis
- Data Filtering