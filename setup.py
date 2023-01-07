from setuptools import setup
import versioneer

setup(
    name="fastapi-quick",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Quickstart FastAPI server",
    author="Jae Ryu",
    author_email="thejaeryu@gmail.com",
    url="",
    packages=[],
)
