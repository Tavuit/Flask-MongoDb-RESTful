# coding: UTF-8
import os
def load_config():
    """Load config."""
    try:
        from .development import DevelopmentConfig
        return DevelopmentConfig
    except ImportError:
        from .default import Config
        return Config
