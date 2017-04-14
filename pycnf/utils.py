import os
import json
import yaml
import ini
import toml
import tempfile

def load_config(filename, file_type="json", extra_dict={}, other_config="", **kwargs):
    filename = os.path.expanduser(filename)
    config_dict = {}
    if file_type == "json":
        fn = file(filename)
        str_list = fn.readlines()
        json_str = "".join(str_list)
        config_dict = json.loads(json_str)
    if file_type == "ini":
        config_dict = dict(ini.load(open(filename, "r")))
    if file_type == "yaml":
        fn = open(filename)
        config_dict = yaml.load(fn)
    if file_type == "toml":
        config_dict = toml.load(open(filename))
    return(config_dict)
