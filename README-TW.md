[English](https://github.com/adobe-fonts/source-han-sans/) [简体中文](README-CN.md) [繁體中文](README-TW.md) [日本語](README-JP.md) [한국어](README-KR.md)

# 思源黑體

「思源黑體」是一套 OpenType/CFF 泛中日韓字型。這個開放原始碼專案不僅提供了可用的 OpenType 字型，還提供了利用 AFDKO *makeotf* 與 *otf2otc* 工具建置這些 OpenType 字型時的所有原始碼檔案。

## 下載字型（OTF、OTC、Super OTC 與 Subset OTF）

本專案提供了為多種部署方式而設定的獨立字型資源以及 ZIP 檔案供下載：

* [最新發佈](https://github.com/adobe-fonts/source-han-sans/tree/release)

參考[《官方字型 readme 檔案》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf)的 Configurations（設定）部分，可以幫助您決定下載哪一套字型。推薦不熟悉 GitHub 的人士，請參照以英文、日文、韓文、簡體中文、繁體中文提供的[《思源字型官方下載指南》](https://github.com/adobe-fonts/source-han-serif/raw/release/download-guide-source-han.pdf)。

您也可以一個單一 ZIP 檔案形式下載整個 [releases](../../releases)，內含所有設定。[最新發佈](../../releases/latest)的 ZIP 檔案大約有 2GB 大小。

## 自原始碼檔案建置字型

### 要求

要自原始碼檔案建置二進位字型檔案，需要安裝[「OpenType 用 Adobe 字型開發套件」](https://github.com/adobe-type-tools/afdko/)（AFDKO）。AFDKO 工具目前已被廣泛用於字型開發，也是大多數字型編輯應用程式的一部分。

### 建置所有字型

這個存放庫裡存放了建置 OpenType/CFF 與 OpenType/CFF 集合字型的所有必要檔案。[COMMANDS.txt](COMMANDS.txt) 檔案提供了用於建置 OTF 與 OTC 檔案的命令列。

## 如何參與

有任何修改建議，請至issue頁面點選[New issue](https://github.com/adobe-fonts/source-han-sans/issues)以資參考。

## 詳細資訊

更多關於「思源黑體」的設計與背景資訊，請參照[《設計指南》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansDesignGuide.pdf)與[《官方字型 readme 檔案》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf)。
