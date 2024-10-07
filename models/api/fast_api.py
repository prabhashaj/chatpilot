import chromadb
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from ..scrape.query import query_db

from ..scrape.selenium_scrapper import selenium_scrape_and_save_to_csv
# Initialize FastAPI app
app = FastAPI()


# Input model for scraping request
class ScrapeRequest(BaseModel):
    url: str


# Input model for query request
class QueryRequest(BaseModel):
    query_text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return RedirectResponse(url="https://example.com/favicon.ico")  # You can use any URL or local file path

@app.post("/scrape/")
def scrape_and_store(scrape_request: ScrapeRequest):
    # """Scrape a URL and store the content."""
    content = selenium_scrape_and_save_to_csv(scrape_request.url)
    if content is None:
        raise HTTPException(status_code=500, detail="Error during scraping")

    return {"message": "Scraping successful, content stored.", "content": content}
    # return "HI"


@app.post("/query/")
def query_content(query_request: QueryRequest):
    # """Query the stored content from ChromaDB."""
    # print(query_request.query_text)
    return query_db( query_request.query_text)
    # return "HI again"


# To run the server
# Use: uvicorn main:app --reload