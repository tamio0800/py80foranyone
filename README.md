# py80foranyone

> 獻給 Alita 的現代化 Python 極簡手冊  
> 希望你能早點下班，回家和家人一起吃頓熱熱的晚餐。

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://tamio0800.github.io/py80foranyone/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 關於本書

這是一本專為**沒有工程師背景**的人設計的 Python 學習手冊。在這個 AI 已經無所不在的年代，你需要的不是「學好所有 Python 語法」，而是「知道怎麼問 AI、怎麼表達需求」。

這本小書嚴格遵循 **80/20 法則**：
- ✅ 只教你「非學不可」的 Python 開發核心知識
- ✅ 其餘的部分交給 AI 解決

看完這本書後，你將學會怎麼用 **AI + Python** 來自動化日常工作。

## 🌐 線上閱讀

**👉 [立即閱讀](https://tamio0800.github.io/py80foranyone/)**

## ✨ 專案特色

- 🎯 **80/20 法則**：只學最核心的 20% 知識，解決 80% 的問題
- 🤖 **AI 協作導向**：教你如何與 ChatGPT 協作，而不是死背語法
- 📚 **實戰案例**：包含完整的自動化實戰案例
- 🚀 **零基礎友善**：專為沒有程式背景的人設計
- 💡 **實用導向**：聚焦於解決真實世界的問題

## 📚 內容大綱

1. **在正式開始之前** - 環境設置與工具準備
2. **Python 中最重要的四個型別** - 數字、字串、列表、字典
3. **如何使用 Python 套件** - import 與 pandas 基礎
4. **什麼是變數** - 給資料取名字
5. **自動化兩大法寶** - if 與 for
6. **如何用 AI 成為半個工程師** - AI 協作技巧與 prompt 設計
7. **自動化實戰** - 複雜欄位比對案例

## 🚀 快速開始

### 本地運行

1. **克隆專案**
   ```bash
   git clone https://github.com/tamio0800/py80foranyone.git
   cd py80foranyone
   ```

2. **設置虛擬環境**
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```

3. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

4. **啟動本地伺服器**
   ```bash
   mkdocs serve
   ```

5. **訪問網站**
   打開瀏覽器訪問 `http://127.0.0.1:8000/`

## 🛠️ 技術棧

- **MkDocs** - 靜態網站生成器
- **Material for MkDocs** - 現代化文檔主題
- **Python 3.13+** - 開發環境
- **GitHub Pages** - 自動部署

## 📁 專案結構

```
py80foranyone/
├── docs/                    # 文檔源文件
│   ├── index.md            # 首頁
│   ├── 02_setup.md         # 環境設置
│   ├── 03_datatypes.md     # 資料型別
│   ├── 04_import_packages.md # 套件使用
│   ├── 05_variables.md     # 變數
│   ├── 06_if_and_for.md    # 控制流程
│   ├── 07_how_to_work_with_ai.md # AI 協作
│   ├── 08_case_study_complex_mapping.md # 實戰案例
│   ├── data/               # 範例資料
│   └── images/            # 圖片資源
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 部署腳本
├── mkdocs.yml              # MkDocs 配置
├── requirements.txt        # Python 依賴
└── README.md              # 本文件
```

## 🤝 貢獻

歡迎提出問題、建議或貢獻內容！

- 🐛 **回報問題**：[Issues](https://github.com/tamio0800/py80foranyone/issues)
- 💬 **討論交流**：[Discussions](https://github.com/tamio0800/py80foranyone/discussions)
- 📝 **內容建議**：歡迎在對應章節下方留言

## 📄 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 文件

## 👤 關於作者

**[Tamio Tsiu](https://www.linkedin.com/in/tamiotsiu/)**  
Sporty Group // Opennet 全球資料科學團隊負責人

- 十年以上資料科學與 AI 實戰經驗
- 橫跨金融、製造、科技、博弈產業

## 💝 致謝

這本書的起點，是給我的太太 Alita，一位 AML 分析師。  
我只希望她能少加一點班，在正常的時間一起吃晚餐。

這本書不只為她而寫，  
它也獻給每一位沒有工程師背景，卻想用科技讓生活和工作更輕鬆的你。

---

⭐ 如果這個專案對你有幫助，歡迎給個 Star！
