import os

class Settings:
    PROJECT_NAME: str = "Sistema de Indicadores INE Monagas"
    API_V1_STR: str = "/api/v1"
    
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "ine_admin")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "ine_password_2026")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "ine_indicadores_monagas")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "ine-monagas-secret-key-super-secure-2026-auth")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 # 24 horas
    
    @property
    def BACKEND_CORS_ORIGINS(self) -> list:
        origins = [
            "http://localhost",
            "http://localhost:3000",
            "http://localhost:5173",
            "http://localhost:8080",
            "http://127.0.0.1:5173",
        ]
        custom = os.getenv("CORS_ORIGINS")
        if custom:
            origins.extend([o.strip() for o in custom.split(",") if o.strip()])
        frontend_url = os.getenv("FRONTEND_URL")
        if frontend_url and frontend_url not in origins:
            origins.append(frontend_url)
        return origins
    
    @property
    def DATABASE_URL(self) -> str:
        env_url = os.getenv("DATABASE_URL")
        if env_url:
            # Render / Heroku compatibility: postgres:// -> postgresql+psycopg2://
            if env_url.startswith("postgres://"):
                env_url = env_url.replace("postgres://", "postgresql+psycopg2://", 1)
            elif env_url.startswith("postgresql://") and not env_url.startswith("postgresql+psycopg2://"):
                env_url = env_url.replace("postgresql://", "postgresql+psycopg2://", 1)
            return env_url
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

settings = Settings()

