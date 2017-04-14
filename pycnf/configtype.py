from utils import *
def is_json_file(filename, show_warnings = False):
    """Check configuration file type is JSON
    Return a boolean indicating wheather the file is JSON format or not
    """
    try:
        config_dict = load_config(filename, file_type = "json")
        is_json = True
    except:
        is_json = False
    return(is_json)
        
def is_yaml_file(filename, show_warnings = False):
    """Check configuration file type is yaml
    Return a boolean indicating wheather the file is yaml format or not
    """
    if is_json_file(filename):
        return(False)
    try:
        config_dict = load_config(filename, file_type = "yaml")
        if(type(config_dict) == str):
            is_yaml = False
        else:
            is_yaml = True
    except:
        is_yaml = False
    return(is_yaml)
    
def is_ini_file(filename, show_warnings = False):
    """Check configuration file type is INI
    Return a boolean indicating wheather the file is INI format or not
    """
    try:
        config_dict = load_config(filename, file_type = "ini")
        if config_dict == {}:
            is_ini = False
        else:
            is_ini = True
    except:
        is_ini = False
    return(is_ini)

def is_toml_file(filename, show_warnings = False):
    """Check configuration file type is TOML
    Return a boolean indicating wheather the file is TOML format or not
    """
    if is_yaml_file(filename):
        return(False)
    try:
        config_dict = load_config(filename, file_type = "toml")
        is_toml = True
    except:
        is_toml = False
    return(is_toml)

def get_config_type(filename):
    """Get configuration file type:[JSON, YAML, INI, TOML]
    Return the configuration filetype: json, yaml, ini, toml or False 
    """
    if is_json_file(filename):
        return("json")
    elif is_ini_file(filename):
        return("ini")
    elif is_yaml_file(filename):
        return("yaml")
    elif is_toml_file(filename):
        return("toml")
    else:
        return(False)
