# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SECRET_KEY = env.str("SECRET_KEY")
BCRYPT_LOG_ROUNDS = env.int("BCRYPT_LOG_ROUNDS", default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = "webpack/manifest.json"
MONGO_URI = env.str("MONGO_URI")
TWTR_CONSUMER_KEY = env.str("TWTR_CONSUMER_KEY")
TWTR_CONSUMER_SECRET = env.str("TWTR_CONSUMER_SECRET")
TWTR_TOKEN_KEY = env.str("TWTR_TOKEN_KEY")
TWTR_TOKEN_SECRET = env.str("TWTR_TOKEN_SECRET")
MONGODB_DB = env.str("MONGODB_DB")
MONGODB_HOST = env.str("MONGODB_HOST")
MONGODB_PORT = int(env.str("MONGODB_PORT"))
