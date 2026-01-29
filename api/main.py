from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from api.routers import analytics, decisions

app = FastAPI(title="Enterprise Data-to-Decision Platform")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(analytics.router)
app.include_router(decisions.router)

@app.get("/health")
def health():
    return {"status": "ok"}
