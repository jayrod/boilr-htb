#!/usr/bin/env python3
import os
from pathlib import Path

PROJECT_DIRECTORY = Path().cwd()


if __name__ == '__main__':

    #Create directories 

    dirs = ['notes','penetration','pillage','privesc','remote-enum', 'root-in-10-steps-or-less']

    [PROJECT_DIRECTORY.joinpath(d).mkdir() for d in dirs]
