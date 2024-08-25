import glob
import json
from util.log import new_log
from other import path_to_data

print = new_log # NOQA
registry = {}

registries = [
    "character",
    "attack",
    "enemy"
]

tall_characters = [
    "fwb:fredbear",
    "fwb:spring_bonnie",
    "fwb:nightmare_fredbear",
    "fwb:nightmare"
]

characters_with_flipped_texture = [
    "fwb:medic",
    "fwb:paper_pals",
    "fwb:plushtrap",
    "fwb:scout",
    "fwb:spy"
]


def load_registries(full_reload: bool = True, location: str = "", dump: bool = False):
    global registry
    if full_reload:
        registry = {}
        for _ in registries:
            registry[_] = {}
    for reg in registries:
        reg_files = glob.glob(pathname=(location + "data/*/" + reg + "/**/*.json"), recursive=True)
        # print(reg_files)
        reg_dict = registry[reg]
        for f in reg_files:
            name = path_to_data(f, reg)
            with open(f) as file:
                file_contents = json.load(file)
            try:
                reg_dict[name] = file_contents
                print("Loaded " + reg + " \"" + name + "\"")
            except:
                print(("Failed to load " + reg + " \"" + name + "\""), "error")
        registry[reg] = reg_dict
    if dump:
        with open("dumps/registry.json", "w") as f:
            f.write(json.dumps(registry, indent=2))
