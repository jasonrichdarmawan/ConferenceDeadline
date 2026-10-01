"""PEP 562
"""

import importlib
from typing import TYPE_CHECKING

# type checking imports for IDEs and static analysis tools
if TYPE_CHECKING:
    from .utils import (
        PROJECT_ROOT as PROJECT_ROOT,
    )
    from .log import (
        get_logger as get_logger,
    )

# Map the public attributes to their underlying module paths
_LAZY_IMPORTS = {
    "PROJECT_ROOT": ".utils",
    "get_logger": ".log",
}

def __getattr__(name: str):
    # Check if the requested attribute is in lazy map
    if name in _LAZY_IMPORTS:
        module_path = _LAZY_IMPORTS[name]

        # Dynamically import the submodule relatively
        module = importlib.import_module(module_path, __name__)

        # Extract the specific attribute
        value = getattr(module, name)

        # Cache it in globals() so __getattr__ isn't called again for this name
        globals()[name] = value

        return value
    
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

# Define __dir__ so IDE autocompletion still works
def __dir__():
    return sorted(list(_LAZY_IMPORTS.keys()))