[English](https://github.com/adobe-fonts/source-han-sans/) [简体中文](README-CN.md) [繁體中文](README-TW.md) [日本語](README-JP.md) [한국어](README-KR.md)

# 思源黑體

思源黑體是一套 OpenType/CFF 泛中日韓字型。這個開放原始碼專案不僅提供了可用的 OpenType 字型，還提供了利用 AFDKO *makeotf* 和 *otf2otc* 工具創建這些 OpenType 字型時的所有原始碼檔案。

## 下載字型（OTF、OTC、Super OTC 和 Subset OTF）

本項目提供了為多種發佈方式而設定的獨立字型資源以及 ZIP 檔案供下載：

* [最新發佈](https://github.com/adobe-fonts/source-han-sans/tree/release)

參考[《官方字型 readme 檔案》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf)的 Configurations（配置）部分，可以幫助您決定下載哪一套字型。推薦不熟悉 GitHub 的人士，請參照以英文、日文、韓文、簡體中文、繁體中文提供的[《思源字型官方下載指南》](https://github.com/adobe-fonts/source-han-serif/raw/release/download-guide-source-han.pdf)。

您也可以一個單一 ZIP 檔案形式下載整個 [releases](../../releases)，內含所有設置。[最新發佈](../../releases/latest)的 ZIP 檔案大約有 1.6GB 大小。

## 字型安裝步驟

* [macOS](https://support.apple.com/en-us/HT201749)
* [Windows](https://www.microsoft.com/en-us/Typography/TrueTypeInstall.aspx)
* [Linux/以 Unix 為基礎的系統](https://github.com/adobe-fonts/source-code-pro/issues/17#issuecomment-8967116)

## 從原始碼檔案創建字型

### 要求

要從原始碼檔案創建二進制字型檔案，需要安裝[「OpenType 用 Adobe 字型開發包」](http://www.adobe.com/devnet/opentype/afdko.html)（AFDKO）。AFDKO 工具目前已被廣泛用於字型開發，也是大多數字型編輯應用程序的一部分。

### 創建所有字型

這個庫里存放了創建 OpenType/CFF 和 OpenType/CFF 集合字型的所有必須檔案。[COMMANDS.txt](COMMANDS.txt) 檔案提供了用於創建 OTF 和 OTC 檔案的命令列。

## 如何參與

請將修改建議發送給負責思源黑體項目維護的[小林劍博士](mailto:lunde@adobe.com?subject=[GitHub]%20Source%20Han%20Sans)，以茲參考。

## 更多資訊

更多關於「思源黑體」的設計和背景資訊，請參照[《設計指南》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansDesignGuide.pdf)和[《官方字型 readme 檔案》](https://github.com/adobe-fonts/source-han-sans/raw/release/SourceHanSansReadMe.pdf)。
