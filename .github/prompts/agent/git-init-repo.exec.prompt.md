# Execution Prompt: Initialize Git Repository

# Goal: Initialize a new Git repository in the current workspace root directory.
# 目標：在當前工作區根目錄初始化一個新的 Git 倉庫。

**Instructions:**

1.  `@workspace /ask` Check if a `.git` directory already exists in the workspace root.
    # 檢查是否已存在 .git 目錄
2.  **If `.git` does NOT exist:**
    # 如果 .git 目錄不存在：
    *   `@terminal /exec` Run the command:
        # 執行 git init 命令
        ```bash
        git init
        ```
    *   `@workspace /showMessage` Display message: "Git repository initialized successfully."
        # 顯示成功訊息
3.  **If `.git` already exists:**
    # 如果 .git 目錄已存在：
    *   `@workspace /showMessage --type=warning` Display warning message: "A Git repository already exists in this directory. No action taken."
        # 顯示警告訊息，不執行任何操作