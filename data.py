import glob
import json
import logging
from other import path_to_data

logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=logging.DEBUG)
registry = {}

registries = [
    "character",
    "attack",
    "enemy"
]


def load_registries(full_reload: bool = True, location: str = "", dump: bool = False):
    global registry
    if full_reload:
        registry = {}
        for _ in registries:
            registry[_] = {}
    for reg in registries:
        reg_files = glob.glob(pathname=(location + "data/*/" + reg + "/**/*.json"), recursive=True)
        reg_dict = registry[reg]
        for f in reg_files:
            name = path_to_data(f, reg, location)
            with open(f) as file:
                file_contents = json.load(file)
            try:
                reg_dict[name] = file_contents
                logging.info("Loaded " + reg + " \"" + name + "\"")
            except Exception as e:
                logging.exception(("Failed to load " + reg + " \"" + name + "\": " + str(e)))
        registry[reg] = reg_dict
    if dump:
        with open("dumps/registry.json", "w") as f:
            f.write(json.dumps(registry, indent=2))
