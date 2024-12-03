import os
import importlib
from src.config.database.db import db
base_directory = os.path.dirname(__file__)

for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            module_path = os.path.relpath(os.path.join(root, file), base_directory)
            module_name = module_path.replace(os.sep, ".")[:-3]
            importlib.import_module(f"src.domain.{module_name}")
__all__ = ["db"]
