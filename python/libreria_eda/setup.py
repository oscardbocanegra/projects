from setuptools import setup, find_packages

setup(
    name="libreria_eda",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
    ],
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Una biblioteca para Análisis Exploratorio de Datos (EDA) que proporciona análisis completo en una sola llamada",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/libreria_eda",
    keywords="eda, data analysis, pandas, exploratory data analysis",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.6",
) 