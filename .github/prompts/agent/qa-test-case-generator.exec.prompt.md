# Execution Prompt: Generate Basic Test Case Outline

# Goal: Automatically generate a basic set of test case outlines (Markdown format) based on provided requirements, user story, API spec, or function signature.
# 目標：根據提供的需求、用戶故事、API規格或函數簽名，自動生成一組基礎的測試案例大綱（Markdown格式）。

**Context Assumption:** The user will provide the relevant input context (e.g., using `@workspace /include file.md` or pasting text) describing the functionality to be tested.

**Instructions:**

1.  `@workspace /ask` **Analyze the provided context.** Identify:
    # 分析提供的上下文
    *   The core functionality or feature being described.
        # 識別核心功能
    *   Key inputs and their expected data types or constraints (if mentioned).
        # 識別關鍵輸入及其類型/約束
    *   Expected successful outcomes (happy path).
        # 識別預期的成功結果
    *   Potential error conditions or invalid input scenarios (if mentioned or inferable).
        # 識別潛在的錯誤條件/無效輸入
    *   Any mention of boundary conditions or edge cases.
        # 識別邊界條件/邊緣情況
2.  `@workspace /input` Ask for a filename for the test cases (suggest based on context, default: `TEST_CASES_OUTLINE.md`). Store as `{testCaseFilename}`.
    # 詢問測試案例檔名
3.  `@workspace /input` Ask for the save directory (suggest `tests/` or `docs/tests/`). Store as `{savePath}`.
    # 詢問儲存目錄
4.  `@workspace /createDirectory` Ensure `{savePath}` exists.
    # 確保儲存目錄存在
5.  `@workspace /newFile` Create file at `{savePath}{testCaseFilename}`.
    # 建立測試案例文件
6.  `@workspace /applyEdit` **Generate test case outlines** in Markdown format. Structure logically (Positive, Negative, Boundary). Use the template below for each case, filling details based on step 1 analysis.
    # 生成測試案例大綱 (Markdown格式，包含正面、負面、邊界)
    ```markdown
    # Test Case Outline: [Feature/Function Name from Context]

    *Generated based on: [Source of Context]*
    *Status: Draft - Requires review and detailed steps*

    ## Positive Scenarios (Happy Path)

    *   **Test Case ID:** [Feature]-TC-001
        *   **Description:** Verify successful [action] with typical valid inputs.
        *   **Preconditions:** [Infer or state TBD]
        *   **Inputs:** [List inferred valid inputs or state TBD]
        *   **Expected Result:** [Describe inferred successful outcome]
        *   **Priority:** High

    *   *...(Generate more positive cases if applicable based on context)*

    ## Negative Scenarios (Error Handling)

    *   **Test Case ID:** [Feature]-TC-101
        *   **Description:** Verify behavior with invalid input type for [specific input, if identified].
        *   **Preconditions:** ...
        *   **Inputs:** [Example invalid input or state TBD]
        *   **Expected Result:** [e.g., Specific error message, graceful failure]
        *   **Priority:** High

    *   **Test Case ID:** [Feature]-TC-102
        *   **Description:** Verify behavior with missing required input [specific input, if identified].
        *   ... (Inputs, Expected Result)
        *   **Priority:** High

    *   *...(Generate more negative cases based on context/common patterns)*

    ## Boundary Value / Edge Cases

    *   **Test Case ID:** [Feature]-TC-201
        *   **Description:** Verify behavior with [specific boundary/edge case, e.g., min/max value, empty input, zero].
        *   **Preconditions:** ...
        *   **Inputs:** [Example boundary/edge case input or state TBD]
        *   **Expected Result:** [Expected outcome for this edge case]
        *   **Priority:** Medium

    *   *...(Generate more boundary/edge cases if identifiable)*

    ---

    *Note: These are initial outlines. Detailed steps and specific data values need to be added.*
    ```
7.  `@workspace /openFile` Open the newly created file `{savePath}{testCaseFilename}`.
    # 打開新創建的文件
8.  `@workspace /showMessage` Display message: "Basic test case outlines generated in `{savePath}{testCaseFilename}`. Please review and add details."
    # 顯示完成訊息