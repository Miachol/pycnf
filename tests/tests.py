import unittest
import os
import tempfile
from pycnf.configtype import *
import pycnf.read as read
from pycnf.pycnf import *
import pycnf.write as write

class ConfigtypeTest(unittest.TestCase):
    def setUp(self):
        print('init by setUp...')
    def tearDown(self):
        print 'end by tearDown...'

    def test_pycnf(self):
        temp_dir = tempfile.mktemp()
        os.mkdir(temp_dir)
        json_config = ConfigFile("tests/config.json")
        self.assertEqual(json_config.file_type, "json")
        self.assertEqual(type(json_config.read()), str)
        self.assertEqual(json_config.read(), "tests/config.json")
        self.assertEqual(json_config.sections(), ["default", "comments"])
        self.assertEqual(json_config.options("default"), ["debug"])
        self.assertEqual(json_config.eval("default", "debug"), "{{debug}} {{debug2}}")
        temp_file = "%s/test.json" % (temp_dir)
        self.assertEqual(json_config.write(temp_file, "json"), True)
        ini_config = ConfigFile("tests/config.ini")
        self.assertEqual(ini_config.file_type, "ini")
        self.assertEqual(type(ini_config.read()), str)
        self.assertEqual(ini_config.read(), "tests/config.ini")
        self.assertEqual(ini_config.sections(), ["default", "comments"])
        self.assertEqual(ini_config.options("default"), ["debug"])
        self.assertEqual(ini_config.eval("default", "debug"), "{{debug}} {{debug2}}")
        temp_file = "%s/test.ini" % (temp_dir)
        self.assertEqual(ini_config.write(temp_file, "ini"), True)
        yaml_config = ConfigFile("tests/config.yaml")
        self.assertEqual(yaml_config.file_type, "yaml")
        self.assertEqual(type(yaml_config.read()), str)
        self.assertEqual(yaml_config.read(), "tests/config.yaml")
        self.assertEqual(yaml_config.sections(), ["default", "comments"])
        self.assertEqual(yaml_config.options("default"), ["debug"])
        self.assertEqual(yaml_config.eval("default", "debug"), "{{debug}} {{debug2}}")
        temp_file = "%s/test.yaml" % (temp_dir)
        self.assertEqual(yaml_config.write(temp_file, "yaml"), True)
        toml_config = ConfigFile("tests/config.toml")
        self.assertEqual(toml_config.file_type, "toml")
        self.assertEqual(type(toml_config.read()), str)
        self.assertEqual(toml_config.read(), "tests/config.toml")
        self.assertEqual(toml_config.sections(), ["default", "comments", "title"])
        self.assertEqual(toml_config.options("default"), ["debug"])
        self.assertEqual(toml_config.eval("default", "debug"), "{{debug}} {{debug2}}")
        temp_file = "%s/test.toml" % (temp_dir)
        self.assertEqual(toml_config.write(temp_file, "toml"), True)
    def test_read(self):
        self.assertEqual(type(read.load("tests/config.json", "json")), dict)
        self.assertEqual(type(read.load("tests/config.yaml", "yaml")), dict)
        self.assertEqual(type(read.load("tests/config.ini", "ini")), dict)
        self.assertEqual(type(read.load("tests/config.toml", "toml")), dict)
        self.assertEqual(type(read.eval("tests/config.toml", "default")), dict)
    def test_write(self):
        example_dict = {"a":"d"}
        temp_dir = tempfile.mktemp()
        os.mkdir(temp_dir)
        temp_file = "%s/write.test.json" % (temp_dir)
        self.assertEqual(write.dump(example_dict, temp_file), True)
        self.assertEqual(get_config_type(temp_file), "json")
    def test_convert(self):
        temp_dir = tempfile.mktemp()
        os.mkdir(temp_dir)
        temp_file = "%s/write.test.json" % (temp_dir)
        self.assertEqual(write.convert("tests/config.toml", temp_file, "json"), True)
        

    def test_is_family(self):
        self.assertEqual(is_json_file("tests/config.json"), True)
        self.assertEqual(is_yaml_file("tests/config.yaml"), True)
        self.assertEqual(is_ini_file("tests/config.ini"), True)
        self.assertEqual(is_toml_file("tests/config.toml"), True)
        self.assertEqual(get_config_type("tests/config.toml"), "toml")
        self.assertEqual(get_config_type("tests/config.ini"), "ini")
        self.assertEqual(get_config_type("tests/config.json"), "json")
        self.assertEqual(get_config_type("tests/config.yaml"), "yaml")

if __name__ == '__main__':
    unittest.main()
