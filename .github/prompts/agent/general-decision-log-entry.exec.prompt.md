# Execution Prompt: Add Entry to Decision Log

# Goal: Capture and record a significant project decision in a structured format within a central decision log file (`DECISION_LOG.md`).
# 目標：在中央決策日誌文件（`DECISION_LOG.md`）中，以結構化格式捕獲並記錄一個重要的專案決策。

**Instructions:**

1.  `@workspace /input --prompt="Decision Title (Brief summary):"` Store as `{decisionTitle}`.
    # 提示使用者輸入決策標題
2.  `@workspace /input --prompt="Context/Problem (What led to this decision?):" --multiline` Store as `{decisionContext}`.
    # 提示使用者輸入決策背景或問題
3.  `@workspace /input --prompt="Options Considered (Briefly list alternatives):" --multiline` Store as `{optionsConsidered}`.
    # 提示使用者輸入考慮過的選項
4.  `@workspace /input --prompt="Decision & Rationale (What was decided and why?):" --multiline` Store as `{decisionRationale}`.
    # 提示使用者輸入最終決定及其理由
5.  `@workspace /input --prompt="Involved Perspectives (e.g., PM, PjM, Tech Lead - Optional):"` Store as `{involvedPerspectives}`.
    # 提示使用者輸入涉及的視角（可選）
6.  `@workspace /ask` Get the current date (e.g., YYYY-MM-DD). Store as `{currentDate}`.
    # 獲取當前日期
7.  `@workspace /readFile --ignoreIfNotExists --path="DECISION_LOG.md"` Read current content of `DECISION_LOG.md`. Store as `{existingLogContent}`.
    # 讀取現有的 DECISION_LOG.md 內容（如果存在）
8.  `@workspace /ask` Construct the new log entry in Markdown format:
    # 構建新的日誌條目 (Markdown 格式)
    ```markdown

    ---

    ## Decision: {decisionTitle}

    *   **Date:** {currentDate}
    *   **Status:** Decided
    *   **Context/Problem:**
        ```
        {decisionContext}
        ```
    *   **Options Considered:**
        ```
        {optionsConsidered}
        ```
    *   **Decision & Rationale:**
        ```
        {decisionRationale}
        ```
    *   **Involved Perspectives:** {involvedPerspectives}

    ```
    Store this new entry as `{newLogEntry}`.
9.  `@workspace /ask` Combine existing content and the new entry (append new entry, perhaps add a newline before the '---'). Store as `{updatedLogContent}`.
    # 將新條目附加到現有內容後
10. `@workspace /writeFile --path="DECISION_LOG.md"` Write `{updatedLogContent}` back to `DECISION_LOG.md`.
    # 將更新後的內容寫回 DECISION_LOG.md
11. `@workspace /showMessage` Display message: "Decision '{decisionTitle}' recorded in DECISION_LOG.md."
    # 顯示完成訊息
12. `@workspace /openFile --path="DECISION_LOG.md"` Open the decision log file.
    # 打開決策日誌文件