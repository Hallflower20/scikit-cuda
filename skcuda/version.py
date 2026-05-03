from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("scikit-cuda")
except PackageNotFoundError:
    __version__ = "0+unknown"
