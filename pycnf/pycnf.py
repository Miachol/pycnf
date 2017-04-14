from utils import *
import configtype
import read
import write
class ConfigFile(object):
    """Configuration file class
    This class can be used to parse and write JSON/YAML/INI/TOML format configuration file 

    Attributes:
        filename: A string indicating the file path of configuration file
    """
    def __init__(self, filename):
        """Inits ConfigFile with filename."""
        filename = os.path.expanduser(filename)
        self.filename = filename
        self.file_type = configtype.get_config_type(filename)

    def sections(self):
        return(self.content.keys())

    def options(self, section):
        section_content = self.content[section]
        return(section_content.keys())

    def eval(self, section, option):
        if option == "":
            return(self.content[section])
        else:
            return(self.content[section][option])

    def read(self, extra_dict = {}, other_config = "", **kwargs):
        if self.filename == False:
            return(False)
        if self.file_type not in ["json", "yaml", "ini", "toml"]:
            return(False)
        self.content = read.load(filename = self.filename, extra_dict = extra_dict, 
                other_config = other_config, **kwargs)
        return(self.filename)

    def write(self, out_file = "", write_type = "json", **kwargs):
        if out_file == "":
            out_file = self.filename
        status = write.dump(config_dict = self.content, out_file = out_file, 
                 write_type = write_type, **kwargs)
        return(status)


