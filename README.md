# RAG-Application
 
This is a minimal implementation of the RAG model for question answering.

## Requirements
- python 3.11 or later

#### install python using Miniconda





## Installation 

### Install the required packages
```bash
$ pip install -r requirements.txt
```
### Setup the environment variables
```bash
$ cp .env.example .env
```


set your enviroment variables in the `.env` file. Like `OPEN_API_KEY` value .



## Run the  FastAPI server

```bash
$ python -m uvicorn main:app --reload
```


