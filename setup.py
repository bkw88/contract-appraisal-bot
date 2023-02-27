from setuptools import setup

install_requires = [
    "aiohttp>=3.8.4",
    "discord.py==1.3.3",
    "EsiPy==1.2.2",
    "dynaconf==2.2.3",
    "redis==4.5.1",
    "requests==2.24.0",
    "dhooks==1.1.3",
    "black==23.1.0",
    "loguru==0.6.0",
    "asgiref==3.2.10",
    "dataclasses-json==0.5.5",
]

setup(
    name="contract-appraisal-bot",
    version="0.0.1",
    packages=[""],
    url="",
    license="",
    author="Ben Cole",
    author_email="",
    description="",
    install_requires=install_requires,
)
