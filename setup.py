from setuptools import setup, find_packages

setup(
    name="imobiliaria-3-irmaos",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "sqlalchemy>=1.4.0",
        "pydantic>=1.8.0",
        "passlib[bcrypt]>=1.7.0"
    ],
)