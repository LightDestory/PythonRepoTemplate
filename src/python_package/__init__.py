from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("package_name")
except PackageNotFoundError:  # pragma: no cover - running from a source checkout
    __version__ = "0.0.1"

__all__ = ["__version__"]
