from utils import *
from configtype import get_config_type
import read

def dump(config_dict, out_file, write_type = "json", **kwargs):
    fn = open(out_file, "w")
    if write_type == "json":
        json.dump(config_dict, fn, sort_keys = False, ensure_ascii = False, **kwargs)
    elif write_type == "yaml":
        yaml.dump(config_dict, fn, **kwargs)
    elif write_type == "ini":
        ini.dump(config_dict, fn, **kwargs)
    elif write_type == "toml":
        toml.dump(config_dict, fn, **kwargs)
    fn.close()
    if get_config_type(out_file) == write_type:
        return(True)
    else:
        return(False)

def convert(filename, out_file, convert_type = "json", **kwargs):
    config_dict = read.load(filename, **kwargs)
    status = dump(config_dict, out_file, convert_type, **kwargs)
    return(status)
