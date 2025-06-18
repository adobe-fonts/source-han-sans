import sys
from afdko.buildcff2vf import main as buildcff2vf

# Before running this script you must first run build-source-otfs.py to make
# the ExtraLight and Heavy source OTFs used to create the variable fonts.
#
# Run this script to build all variable fonts or run the buildcff2vf command
# manually to build the desired designspace files.
# By default the fonts will be written to the designspace folder.
# This can be changed by using the -o option on buildcff2vf to specify an
# output location.

script_tags = ["JP", "KR", "CN", "TW", "HK"]
script_ids = ["1", "3", "25", "2", "2"]
locales = ["J", "K", "SC", "TC", "HC"]


def build_subset_vfs():
    for tag in script_tags:
        args = [
            "--omit-mac-names",
            "-d",
            f"../Masters/designspaces/Subset/SourceHanSans{tag}-VF.designspace",
        ]
        buildcff2vf(args)


def build_half_width_vfs():
    for loc in locales:
        if loc == "J":
            loc = ""
        args = [
            "--omit-mac-names",
            "-d",
            f"../Masters/designspaces/HW/SourceHanSansHW{loc}-VF.designspace",
        ]
        buildcff2vf(args)


def build_vfs():
    for loc in locales:
        if loc == "J":
            loc = ""
        args = [
            "--omit-mac-names",
            "-d",
            f"../Masters/designspaces/SourceHanSans{loc}-VF.designspace",
        ]
        buildcff2vf(args)


def main():
    build_subset_vfs()
    build_vfs()
    build_half_width_vfs()


if __name__ == "__main__":
    sys.exit(main())
