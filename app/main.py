# app/main.py
from fastapi import FastAPI
from .routers import pages # Import your page router
# Import other routers as you create them
# from .routers import recommendations

app = FastAPI(title="Music Recommendation API")

# Include routers
app.include_router(pages.router, tags=["Pages"])
# app.include_router(recommendations.router, prefix="/api", tags=["Recommendations"])

# You can add startup events if needed, e.g., to ensure DB connection
@app.on_event("startup")
async def startup_event():
    print("Application startup...")
    # You could potentially run create_tables here, but it's better practice
    # to manage schema separately (e.g., with create_tables.py or Alembic)
    pass

# A simple health check endpoint (optional but good)
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}