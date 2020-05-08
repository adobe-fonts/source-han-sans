[English](https://github.com/adobe-fonts/source-han-sans/) [简体中文](README-CN.md) [繁體中文](README-TW.md) [日本語](README-JP.md) [한국어](README-KR.md)

# 思源黑体

思源黑体是一套 OpenType/CFF 泛中日韩字体。这个开源项目不仅提供了可用的 OpenType 字体，还提供了利用 AFDKO *makeotf* 和 *otf2otc* 工具创建这些 OpenType 字体时的所有源文件。

## 下载字体（OTF、OTC、Super OTC 和 Subset OTF）

本项目提供了为多种部署方式而设定的独立字体资源以及 ZIP 文件供下载：

* [最新发布](https://github.com/adobe-fonts/source-han-sans/tree/release)

参考[《官方字体 readme 文件》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf)的 Configurations（设置）部分，可以帮助您决定下载哪一套字体。推荐不熟悉 GitHub 的人士参照以英文、日文、韩文、简体中文、繁体中文提供的[《思源字体官方下载指南》](https://github.com/adobe-fonts/source-han-serif/raw/release/download-guide-source-han.pdf)。

您也可以一个单一 ZIP 文件形式下载整个 [releases](../../releases)，内含所有设置。[最新发布](../../releases/latest)的 ZIP 文件大约有 2GB 大小。

## 从源文件创建字体

### 要求

要从源文件创建二进制字体文件，需要安装[「OpenType 用 Adobe 字体开发包」](https://github.com/adobe-type-tools/afdko/)（AFDKO）。AFDKO 工具目前已被广泛用于字体开发，也是大多数字体编辑应用程序的一部分。

### 创建所有字体

这个库里存放了创建 OpenType/CFF 和 OpenType/CFF 集合字体的所有必须文件。[COMMANDS.txt](COMMANDS.txt) 文件提供了用于创建 OTF 和 OTC 文件的命令行。

## 如何参与

有任何修改建议，请至issue页面点选[New issue](https://github.com/adobe-fonts/source-han-sans/issues)以资参考。

## 更多信息

更多关于「思源黑体」的设计和背景信息，请参照[《设计指南》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansDesignGuide.pdf)和[《官方字体 readme 文件》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf)。
