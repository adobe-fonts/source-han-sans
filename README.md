Source Han Sans
====

Overview
----
Source Han Sans is an OpenType/CFF Pan-CJK font family. This open source project provides all of the source files that were used to build these OpenType fonts by using the AFDKO *makeotf*, *sfntedit*, and *otf2otc* tools.

Getting Involved
----
Send suggestions for changes to the Source Han Sans project maintainer, [Dr. Ken Lunde](mailto:lunde@adobe.com), for consideration.

Building
====

Pre-built font binaries
----
The installable font resources (pre-built font binaries) are not part of the source files. They are available at [Open@Adobe](https://sourceforge.net/projects/source-han-sans.adobe/files/) where technical details about these fonts, along with resources not necessary for building the fonts, are also available.

Important Note: The four OTFs in the "OTC" subdirectory of each weight directory are included as source data for building the corresponding OTC, and are not meant to be used as stand-alone fonts, though they can be installed and used as such.

Requirements
----

For building binary font files from source, installation of the [Adobe Font Development Kit for OpenType](http://www.adobe.com/devnet/opentype/afdko.html) (AFDKO) is necessary. The AFDKO tools are widely used for font development today, and have been integrated into most font editing applications.

Building the fonts
----

The key to building OpenType/CFF fonts is *makeotf*, which is included in AFDKO. Information and usage instructions can be found by executing *makeotf -h*. The AFDKO *sfntedit* tool is used to splice in the stub 'DSIG' table. The AFDKO script, *otf2otc*, is used to assemble multiple OTFs into a single OTC (OpenType Collection).

In this repository, all necessary files are in place for building the OpenType/CFF and OpenType/CFF Collection fonts. The COMMANDS.txt file includes the command lines that are used to build the OTFs and OTCs.

That is all.
