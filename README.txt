Volopay: API Development and Data Transformation

1. The API is written in Python using the Django framework and SQLite as database.

Steps:
1. First install the conda environment using the following command `conda env create -f env.yml`

2. The SQLite database was created from the Django migrations. The Django Models can be found in `api/models.py`

3. The SQLite database was created from the csv files using the `import_csv_into_db.py` file.

4. The APIs can be found in `api/views.py`

5. To run the API use the command `python3 manage.py runserver`