import os
from distutils.core import setup


def requirements():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
        requires = []
        for require in f.readlines():
            if require.strip().startswith("-i"):
                continue
            requires.append(require.strip().split(";")[0])
    return requires


setup(
    name="DataCenter",
    version="0.0.1",
    description="My data center",
    author="Haha.Li",
    author_email="copylife@gmail.com",
    url="https://www.haha.com/data/center",
    packages=["data_center"],
    install_requires=requirements(),
)
