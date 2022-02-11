# Bruto 2

A Telnet penetration tool
(read notes below)

## Description

This tool allows to discover, given a list of IP addresses, the ones that are
vulnerable at the telnet port, if there are any.
The sript supports both local and public IP addresses.


## Getting Started

### Dependencies

* Needed Python 3.x
* All imported libraries are default python libraries
* The script is cross-platform compatible

### Installing

How to install the program
 ```
 $ git clone https://github.com/aledipa/bruto2.git
 $ cd bruto2/
 ```

### Executing program
 
Step-by-step usage guide
```
# First thing first, you'll need to get the IPs
$ zmap -p 23 -o list.txt

# Then you can run the script
$ python3 Bruto2.py [ips list name/path] [threads number] [output file name]
# Example:
$ python3 Bruto2.py list.txt 15 bruted_addresses.txt

# NOTE: using a larger thread number will allow you to a faster 
# execution but it will also be more resource intensive too
```

## Help

Commands to run to get the syntax infos
```
$ python3 Bruto2.py [-h] [--help]
> Usage: python3 Bruto2.py <list> <threads> <output file>
```
For other issues try to update your python version
```
# Check your python version (should be at least 3.0)
$ python -v
# Force execute the script using python 3 over python 2.x
$ python3 Bruto2.py
```

## Authors

Main developer: [@AleDipa](https://github.com/aledipa)

Helped with logic and structure: [@Git-Malik](https://github.com/git-malik)

## Version History

* 0.1
    * Initial Release
    * See [commit change](https://github.com/aledipa/bruto2/commits/main) or See [release history](https://github.com/aledipa/bruto2/releases)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Notes
This project is developed based on a very old script called "bruto.py" that worked
as single-threaded, python 2 script. This old script could not work anymore and even so (the rare times it did)
it wasn't reliable or efficient at all. So, i decided to make my own based on that, with a lightly extended wordlist, using multi-thread, python 3.x, more reliability and a pretty raw system to recognize the type of system you've bruted and filter the "false positives".
