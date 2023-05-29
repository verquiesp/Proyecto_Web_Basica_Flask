class Config:
    pass

class DevelopmentConfig(Config): # Reinicios automáticos del servidor para poder trabajar en entorno de pruebas
    DEBUG=True
    MYSQL_HOST="db4free.net"
    MYSQL_USER="verquiesp"
    MYSQL_PASSWORD="verquiesp"
    MYSQL_DB="soccespotter"

config={
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}