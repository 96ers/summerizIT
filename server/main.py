import uvicorn

from src.configs.server import server_config

if __name__ == "__main__":
    print("Server is running on environment: ", server_config.ENVIRONMENT)
    uvicorn.run(
        app="src.server:server",
        reload=True,
        port=server_config.PORT,
    )
