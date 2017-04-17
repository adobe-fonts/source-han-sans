# Downloading Source Han Sans

Source Han Sans is an open source Pan-CJK typeface whose OpenType/CFF fonts are covered under the terms of the [SIL Open Font License, Version 1.1](http://scripts.sil.org/OFL) (also see the [LICENSE](LICENSE.txt) and [FAQ](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL-FAQ_web)). In addition to providing ready-to-install OpenType/CFF font resources in this branch as individual font resources or grouped together in downloadable ZIP files, this open source project provides in its [master branch](https://github.com/adobe-fonts/source-han-sans/) all of the CID-based source files that were used to build these OpenType/CFF fonts by using the [AFDKO](https://www.adobe.com/devnet/opentype/afdko.html) *makeotf* and *otf2otc* tools.

Those who are unfamiliar with GitHub are encouraged to reference the [official Source Han download guide](https://github.com/adobe-fonts/source-han-serif/raw/release/download-guide-source-han.pdf), which is provided in English, Japanese, Korean, Simplified Chinese, and Traditional Chinese.

### Super OTC

Select this deployment format if you want all languages and all weights in a single and easy-to-manage font resource. Changing languages is accomplished by either selecting a font of the appropriate language or by language-tagging the text. A limited number of apps support language tagging and the corresponding OpenType 'locl' (*Localized Forms*) GSUB feature, such as [Adobe InDesign CC](https://www.adobe.com/products/indesign.html) and modern browsers.

[Super OTC](https://github.com/adobe-fonts/source-han-sans/raw/release/SuperOTC/SourceHanSans.ttc.zip)

**Special Note**: This deployment format requires macOS (OS X) Version 10.8 (aka *Mountain Lion*) or later, iOS 7 or later, or Windows 10 Version 1703 (aka *Creators Update*) or later. If you are using Adobe apps, CS6 or later versions must be used.

### OTCs

Select this deployment format if you want all languages and some weights, or if your environment does not support the Super OTC. Changing languages is performed the same way as the Super OTC. If you need specific weights, download individual font resources from the [OTC](OTC) folder, otherwise click one or both of the links below:

[ExtraLight + Light + Normal + Regular](https://github.com/adobe-fonts/source-han-sans/raw/release/OTC/SourceHanSansOTC_EL-R.zip) & [Medium + Bold + Heavy](https://github.com/adobe-fonts/source-han-sans/raw/release/OTC/SourceHanSansOTC_M-H.zip)

**Special Note**: This deployment format requires macOS (OS X) Version 10.8 (aka *Mountain Lion*) or later, iOS 7 or later, or Windows 10 Version 1607 (aka *Anniversary Update*) or later. If you are using Adobe apps, CS6 or later versions must be used.

### Language-specific OTFs

Select this deployment format if you prefer to use only one language, but also want full character coverage or the ability to language-tag text to use glyphs that are appropriate for other languages (like the Super OTC and OTCs, this requires an app that supports language tagging and the OpenType 'locl' GSUB feature). Font resources that include "HW" in their names use half-width glyphs for ASCII by default. If you need only specific weights, download individual font resources from the [OTF](OTF) folder, otherwise click on the appropriate links below:

[Simplified Chinese (简体中文)](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansSC.zip) | [HW Regular + HW Bold](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansHWSC.zip)

[Traditional Chinese (繁體中文)](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansTC.zip) | [HW Regular + HW Bold](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansHWTC.zip)

[Japanese (日本語)](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansJ.zip) | [HW Regular + HW Bold](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansHWJ.zip)

[Korean (한국어)](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansK.zip) | [HW Regular + HW Bold](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansHWK.zip)

### Region-specific Subset OTFs

Select this deployment format if you need only the glyphs for characters for a particular region, **or if you are not sure which deployment format to choose**.

Each ZIP file contains seven font resources, one for each of the seven weights. If you need specific weights, download individual font resources from the [SubsetOTF](SubsetOTF) folder, otherwise click on the appropriate links below:

[China (中国)](https://github.com/adobe-fonts/source-han-sans/raw/release/SubsetOTF/SourceHanSansCN.zip), [Taiwan (臺灣)](https://github.com/adobe-fonts/source-han-sans/raw/release/SubsetOTF/SourceHanSansTW.zip), [Japan (日本)](https://github.com/adobe-fonts/source-han-sans/raw/release/SubsetOTF/SourceHanSansJP.zip), [Korea (한국)](https://github.com/adobe-fonts/source-han-sans/raw/release/SubsetOTF/SourceHanSansKR.zip)

## Font installation instructions

* [macOS](https://support.apple.com/en-us/HT201749)
* [Windows](https://www.microsoft.com/en-us/Typography/TrueTypeInstall.aspx)
* [Linux/Unix-based systems](https://github.com/adobe-fonts/source-code-pro/issues/17#issuecomment-8967116)

## Getting Involved

Send suggestions for changes to the Source Han Sans project maintainer, [Dr. Ken Lunde](mailto:lunde@adobe.com?subject=[GitHub]%20Source%20Han%20Sans), for consideration.

## Further information

For information about the design and background of Source Han Sans, please refer to the [design guide](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansDesignGuide.pdf) and [official font readme file](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf).
