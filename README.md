pycnf Python package
==============


The Python package '[pycnf](https://github.com/Miachol/pycnf)' implements the
json, configparser, yaml and toml parser for python setting and writing of configuration file.

# Introduction 

The configuration file are necessary for many projects that will help us to manage and set project environment variables easily.

Configuration files, from INI/XML/JSON/YAML to TOML, readability and maneuverability have been improved too much in the past few years, and there are serveral parsers be created in Python and other programming language. That have made us becomes more efficient, but, we need to remember the different functions for different format configuration file that sometimes we only just want to read it and regardless of that format. So, using single function to read or/and write most of configuration file are good way to reduce memory burden.


[pycnf](https://github.com/Miachol/pycnf) have done some work to relax us on configuration files that can be used to parse and generate JSON/INI/YAML/TOML format configuration file.


## Configuration file format

### JSON
``` json
{   "default":{
        "debug":"{{debug}} {{debug2}}"
    },
    "comments":{
        "version":"0.2.0",
        "test_parse":"{{key:test_parse}} {{key:test_parse2}}",
        "test_parse2":"@>@ str_replace('{{key:test_parse}}', '2', '00')@<@ {{key:test_parse2}} {{debug2}}",
        "test_parse3":"{{key:test_parse}}",
        "test_parse4":"@>@ str_replace('{{key:test_parse2}}', '2', '00')@<@ @>@ str_replace('{{key:test_parse}}', '2', '00')@<@ {{key:test_parse2}} {{debug2}}"
    }
}
```
More infomation and example of JSON can be founded in [json.org](http://www.json.org/), [JSON Example](http://www.json.org/example.html) and [JSON-wikipedia](https://en.wikipedia.org/wiki/JSON). `{{key:key:value}}/{{key}}` can be parsed by parse.extra using `extra.list` and `other.config` parameters. `@>@ str_replace("123", "2", "1")@<@` can be parsed by `parse.extra` setting parameter `rcmd.parse` to `TRUE`. Example of that can be founded in this document tail.

### INI
``` ini
[default]
debug = {{debug}} {{debug2}}

[comments]
version = 0.2.0
test_parse = {{key:test_parse}} {{key:test_parse2}}
test_parse2 = @>@ str_replace('{{key:test_parse}}', '2', '00')@<@ {{key:test_parse2}} {{debug2}}
test_parse3 = {{key:test_parse}}
test_parse4 = @>@ str_replace('{{key:test_parse2}}', '2', '00')@<@ @>@ str_replace('{{key:test_parse}}', '2', '00')@<@ {{key:test_parse2}} {{debug2}}
```
More infomation and example of INI can be founded in [INI-wikipedia](https://en.wikipedia.org/wiki/INI_file).

### YAML
``` yaml
default:
  debug: '{{debug}} {{debug2}}'
comments:
  version: 0.2.0
  test_parse: '{{key:test_parse}} {{key:test_parse2}}'
  test_parse2: '@>@ str_replace(''{{key:test_parse}}'', ''2'', ''00'')@<@ {{key:test_parse2}}
    {{debug2}}'
  test_parse3: '{{key:test_parse}}'
  test_parse4: '@>@ str_replace(''{{key:test_parse2}}'', ''2'', ''00'')@<@ @>@ str_replace(''{{key:test_parse}}'',
    ''2'', ''00'')@<@ {{key:test_parse2}} {{debug2}}'
```
More infomation and example of YAML can be founded in [yaml.org](http://www.yaml.org/) and [YAML-wikipedia](https://en.wikipedia.org/wiki/YAML).

### TOML
``` toml
title = "TOML Example"

[default]
debug = true

[comments]
version = "0.1.0"
```
More infomation and example of TOML can be founded in and [toml-lang/toml](https://github.com/toml-lang/toml) and [TOML-wikipedia](https://en.wikipedia.org/wiki/TOML).

# Installation

## pip
``` shell
#You can install this package directly from PYPI by running:
pip install pycnf
```
