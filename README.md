# Introduction to Data Science - Exercise Submissions

Repository for the exercises of the Introduction to Data Science course at the University of Helsinki.

## Virtual Environment

To create a virtual environment, run the following command:

```bash
python3 -m venv venv
```

To activate the virtual environment, run the following command:

```bash
source venv/bin/activate
```

Install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

To launch the Jupyter Notebook, run the following command:

```bash
jupyter notebook
```

To deactivate the virtual environment, run the following command:

```bash
deactivate
```

## Data

Create always a new folder for the data files (use directory name `data`). This way it won't get committed to the repository.

## SQLite Stuff

Pull a lightweight SQLite image from Docker Hub:

```bash
docker pull nouchka/sqlite3
```

Run the container with dump (.sqlite file) mounted to the container:

```bash
docker run -it --rm \
  -v $(pwd)/data:/db \
  nouchka/sqlite3 /db/dump.sqlite
```

Adjust the paths to mount the correct folder on your host machine and the name of the dump file. The example command should be executed under a given week folder, e.g. `week1`. The sqlite file should be placed under the `data` folder and named `dump.sqlite`.
