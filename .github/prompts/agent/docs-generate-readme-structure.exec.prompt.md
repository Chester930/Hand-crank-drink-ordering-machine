# Execution Prompt: Generate README.md Structure

# Goal: Create a well-structured README.md file with standard sections for a typical software project.
# 目標：創建一個結構良好、包含典型軟體專案標準章節的 README.md 文件。

**Instructions:**

1.  `@workspace /ask` Check if a `README.md` file already exists in the workspace root.
    # 檢查 README.md 是否已存在
2.  **If `README.md` already exists:**
    # 如果 README.md 已存在：
    *   `@workspace /input --prompt="README.md already exists. Overwrite? (yes/no)" --choices=["yes", "no"]` Store choice as `{overwrite}`.
        # 詢問使用者是否覆蓋
    *   If `{overwrite}` is "no", `@workspace /showMessage --type=info` Display "Operation cancelled." and stop.
        # 如果選擇 'no'，取消操作並停止
3.  # (Proceed if file doesn't exist or user chose 'yes' to overwrite)
    # （如果文件不存在或使用者選擇 'yes' 覆蓋，則繼續）
4.  `@workspace /ask` Try to infer the project name from the current directory name or `package.json` (if exists). Store as `{projectName}` (use "My Project" as default).
    # 嘗試從目錄或 package.json 推斷專案名稱（預設為 "My Project"）
5.  `@workspace /newFile --path="README.md" --overwrite` Create or overwrite `README.md`.
    # 創建或覆蓋 README.md
6.  `@workspace /applyEdit --path="README.md"` Write the standard README structure:
    # 寫入標準的 README 結構
    ```markdown
    # {projectName}

    [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Example Badge -->

    [Brief project description - What does this project do? Who is it for?]

    ## ✨ Features

    *   [Feature 1]
    *   [Feature 2]
    *   [Feature 3]

    ## 🚀 Getting Started

    ### Prerequisites

    *   [Prerequisite 1, e.g., Node.js >= 18.x]
    *   [Prerequisite 2, e.g., npm or yarn]
    *   ...

    ### Installation

    1.  Clone the repo
        ```bash
        git clone https://github.com/your_username/{projectName}.git
        ```
    2.  Install NPM packages
        ```bash
        cd {projectName}
        npm install
        ```
        _Or using yarn:_
        ```bash
        yarn install
        ```

    ### Running the Project

    *   **Development Mode:**
        ```bash
        npm run dev
        ```
        _Or using yarn:_
        ```bash
        yarn dev
        ```
    *   **Production Build:**
        ```bash
        npm run build
        ```
    *   **Running Production Build:**
        ```bash
        npm start
        ```

    ## 🛠️ Built With

    *   [Technology 1, e.g., Node.js]
    *   [Technology 2, e.g., TypeScript]
    *   [Technology 3, e.g., React]
    *   ...

    ## 🤝 Contributing

    Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

    Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us. (You might need to create this file).

    ## 📜 License

    Distributed under the MIT License. See `LICENSE` for more information. (You might need to create this file).

    ## 🙏 Acknowledgements

    *   [Acknowledgement 1, e.g., Hat tip to anyone whose code was used]
    *   [Acknowledgement 2]
    *   ...

    ## 📞 Contact

    Your Name - [@your_twitter](https://twitter.com/your_twitter) - your.email@example.com

    Project Link: [https://github.com/your_username/{projectName}](https://github.com/your_username/{projectName})

    ```
7.  `@workspace /openFile --path="README.md"` Open the newly created/updated `README.md`.
    # 打開 README.md 文件
8.  `@workspace /showMessage` Display message: "README.md structure generated. Please fill in the specific details for your project."
    # 顯示完成訊息，提示使用者填寫細節