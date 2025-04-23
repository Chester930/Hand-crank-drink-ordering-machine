# Execution Prompt: Generate Conventional Commit Message Suggestion (Following Spec)

# Goal: Analyze staged changes and suggest commit messages strictly following Conventional Commits v1.0.0 (as detailed below), with description in Traditional Chinese.
# 目標：分析暫存區變更，嚴格遵循下方詳述的 Conventional Commits v1.0.0 規範（描述使用繁體中文），建議提交訊息。

**Context Assumption:** The user has staged changes using `git add`.

**Conventional Commits v1.0.0 Core Rules (MUST follow):**
*   **Format:** `<type>[optional scope]: <description (Traditional Chinese)>`\n\n`[optional body]`\n\n`[optional footer(s)]`
*   **Type:** MUST be one of: `feat` (new feature), `fix` (bug fix), `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`.
*   **Scope:** OPTIONAL noun in parentheses describing codebase section (e.g., `(api)`, `(ui)`).
*   **Description:** REQUIRED short summary in **Traditional Chinese (繁體中文)**.
*   **Breaking Change:** Indicate with `!` before colon (e.g., `feat(api)!:`) OR a footer `BREAKING CHANGE: <description>`. MUST be uppercase `BREAKING CHANGE`.
*   **Body:** OPTIONAL, starts after one blank line, explains 'why'.
*   **Footer:** OPTIONAL, starts after one blank line, follows `token: value` or `token#value` format (e.g., `Refs: #123`, `Reviewed-by: name`). `BREAKING CHANGE:` is a valid token.

**Instructions:**

1.  `@git /diff --staged --name-status` Get staged files and status.
    # 獲取暫存區文件列表及狀態
2.  `@git /diff --staged` Get staged diff content.
    # 獲取暫存區變更詳情
3.  `@workspace /ask --temperature=0.5` **Analyze staged changes based on the Core Rules above.**
    # 根據上述核心規則分析變更
    *   Infer primary `<type>` (from allowed list).
        # 推斷類型 (從允許列表中)
    *   Infer optional `<scope>`.
        # 推斷範圍
    *   Generate concise `<description>` **in Traditional Chinese**.
        # 生成繁體中文描述
    *   Detect potential BREAKING CHANGES and format accordingly (`!` or footer).
        # 檢測 Breaking Change 並按規範處理
4.  `@workspace /ask` **Generate 1-3 commit message suggestions** strictly adhering to the Core Rules.
    # 生成 1-3 條嚴格符合核心規則的建議
    *   Example Suggestion 1: `feat(使用者): 新增帳號刪除功能`
    *   Example Suggestion 2: `fix(api)!: 修復分頁查詢返回錯誤總數的問題\n\nBREAKING CHANGE: 分頁 API 的 `totalPages` 欄位已移除，請改用 `hasNextPage`。`
    *   Example Suggestion 3: `docs(README): 更新安裝說明`
5.  `@workspace /input --prompt="Select suggestion or provide your own commit message:" --choices=@suggestions` Allow user selection or input. Store as `{commitMessage}`.
    # 讓使用者選擇或輸入最終訊息
6.  `@terminal /exec` Run commit command: `git commit -m "{commitMessage}"` (Ensure proper quoting for special characters).
    # 執行 git commit
7.  `@workspace /showMessage` Display commit result.
    # 顯示提交結果