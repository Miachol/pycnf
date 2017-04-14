from utils import *
from configtype import get_config_type

def load(filename, extra_dict={}, other_config="", **kwargs):
    file_type = get_config_type(filename)
    config_dict = load_config(filename = filename, file_type = file_type, extra_dict = extra_dict, 
            other_config = other_config, **kwargs)
    return(config_dict)

def eval(filename, section = "default", option = "", **kwargs):
    config_dict = load(filename, **kwargs)
    if option == "":
        return(config_dict[section])
    else:
        return(config_dict[section][option])

def merge(filename, sections = [], **kwargs):
    config_dict = load(filename, **kwargs)
    merge_dict = {}
    for section in sections:
        if(type(config_dict[section]) == dict): 
            merge_dict.update(config_dict[section])
        else:
            merge_dict.update({section:config_dict})
    return(merge_dict)

def sections(filename, **kwargs):
    config_dict = load(filename, **kwargs)
    return(config_dict.keys())

def options(filename, section, **kwargs):
    config_dict = load(filename, **kwargs)
    section_content = config_dict[section]
    return(section_content.keys())

