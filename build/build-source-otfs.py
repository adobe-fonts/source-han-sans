import os
import sys
from afdko.makeotf import main as makeotf

# Run this script to build the ExtraLight and Heavy source OTFs used to
# create the variable fonts.

weights = ["ExtraLight", "Heavy"]
script_tags = ["JP", "KR", "CN", "TW", "HK"]
script_ids = ["1", "3", "25", "2", "2"]
locales = ["J", "K", "SC", "TC", "HC"]


def build_subset_otfs():
    for weight in weights:
        for i, tag in enumerate(script_tags):
            scriptID = script_ids[i]
            args = [
                "-nshw",
                "-f",
                os.path.abspath(f"../Masters/{weight}/VF/cidfont.VF.{tag}.unhinted"),
                "-omitMacNames",
                "-ff",
                os.path.abspath(f"../Masters/{weight}/VF/features.VF.{tag}"),
                "-fi",
                os.path.abspath(f"../Masters/{weight}/cidfontinfo.{tag}"),
                "-mf",
                os.path.abspath("../FontMenuNameDB.VF.SUBSET"),
                "-r",
                "-nS",
                "-cs",
                scriptID,
                "-ch",
                os.path.abspath(f"../UniSourceHanSans{tag}-UTF32-H"),
                "-ci",
                os.path.abspath(f"../SourceHanSans_{tag}_sequences.txt"),
            ]
            makeotf(args)


def build_otfs():
    for weight in weights:
        for i, tag in enumerate(script_tags):
            scriptID = script_ids[i]
            loc = locales[i]
            args = [
                "-nshw",
                "-f",
                os.path.abspath(
                    f"../Masters/{weight}/OTC/VF/cidfont.VF.{loc}.unhinted"
                ),
                "-omitMacNames",
                "-ff",
                os.path.abspath(f"../Masters/{weight}/OTC/VF/features.VF.{loc}"),
                "-fi",
                os.path.abspath(f"../Masters/{weight}/OTC/cidfontinfo.OTC.{loc}"),
                "-mf",
                os.path.abspath("../FontMenuNameDB.VF"),
                "-r",
                "-nS",
                "-cs",
                scriptID,
                "-ch",
                os.path.abspath(f"../UniSourceHanSans{tag}-UTF32-H"),
                "-ci",
                os.path.abspath(f"../SourceHanSans_{tag}_sequences.txt"),
            ]
            makeotf(args)


def build_half_width_otfs():
    for weight in ["Regular", "Bold"]:
        for i, tag in enumerate(script_tags):
            scriptID = script_ids[i]
            loc = locales[i]
            args = [
                "-nshw",
                "-f",
                os.path.abspath(
                    f"../Masters/{weight}/OTC/VF/cidfont.VF.HW.{loc}.unhinted"
                ),
                "-omitMacNames",
                "-ff",
                os.path.abspath(f"../Masters/{weight}/OTC/VF/features.VF.HW.{loc}"),
                "-fi",
                os.path.abspath(f"../Masters/{weight}/OTC/cidfontinfo.OTC.{loc}"),
                "-mf",
                os.path.abspath("../FontMenuNameDB.VF.HW"),
                "-r",
                "-nS",
                "-cs",
                scriptID,
                "-ch",
                os.path.abspath(f"../UniSourceHanSansHW{tag}-UTF32-H"),
                "-ci",
                os.path.abspath(f"../SourceHanSans_{tag}_sequences.txt"),
            ]
            makeotf(args)


def main():
    build_subset_otfs()
    build_otfs()
    build_half_width_otfs()


if __name__ == "__main__":
    sys.exit(main())
