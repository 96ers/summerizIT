import uvicorn

from src.configs import config

if __name__ == "__main__":
    # print(config.server)
    # print(config.mysql)
    # print(config.mysql.get_uri())
    uvicorn.run(
        app="src.server:server",
        reload=config.server.RELOAD,
        port=config.server.PORT,
        host="0.0.0.0"
    )
