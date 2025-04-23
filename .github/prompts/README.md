# Github Copilot Prompts for [您的專案名稱]

這個目錄包含了在此專案中與 Github Copilot（`Ask` 和 `Agent` 模式）配合使用的預定義 Prompts。這些 Prompts 旨在輔助開發生命週期的不同階段，遵循一個為單一操作者利用多種 AI 視角而優化的結構化工作流程。

## 命名規範

此目錄下的所有 Prompt 文件（除了位於 `.github/` 下的 `copilot-instructions.md`）**建議**遵循以下命名規範：

`[分類]-[動作]-[描述符].[類型].md`

*   **分類 (Category):** 高層級領域/角色 (例如 `pm`, `pjm`, `tech-lead`, `frontend`, `backend`, `database`, `devops`, `qa`, `general`, `docs`)。用於排序/分組。
*   **動作 (Action):** 核心動詞/意圖 (例如 `define`, `generate`, `init`, `create`, `review`, `explain`, `refactor`, `plan`, `setup`, `commit`)。
*   **描述符 (Specifier):** 可選的細節 (例如 `role`, `initial-idea`, `project-outline`, `node-ts`, `react-component`, `test-case`, `decision-log`)。
*   **類型 (Type):** `role` (用於 Ask 模式的角色扮演/引導) 或 `exec` (用於 Agent 模式的執行步驟)。

*(詳情請參閱完整的 `[連結至您的命名規範文檔]` - **請替換為您的命名規範文檔連結或文件名**)*

## 核心角色 Prompts (`*.role.md`)

這些定義了在專案生命週期中使用的主要 AI 視角。

*   **`pm-define-role.role.md`**:
    *   **角色:** 產品經理 (結構化輔助者，用於報告生成)
    *   **目的:** 結構化地引導需求澄清討論，旨在於 Ask 聊天中生成專案大綱的 Markdown 文本。
*   **`pjm-define-role.role.md`**:
    *   **角色:** 專案經理 (核心角色協調者與藍圖生成器)
    *   **目的:** 引導創建包含順序和核心角色建議的執行藍圖與任務列表（Markdown 文本在 Ask 聊天中生成），協調進度，審核細化計劃，並根據僅限的核心角色建議下一步行動。
*   **`tech-lead-define-role.role.md`**:
    *   **角色:** 技術負責人 (設計、問題解決與工具建議顧問)
    *   **目的:** 提供技術設計指導、API 設計、代碼結構建議、問題解決輔助，並在需要時**建議創建新的專業化 Prompts (role 或 exec)**。
*   **`frontend-design.role.md`**:
    *   **角色:** 前端設計與工程顧問 (含工具建議)
    *   **目的:** 專注於 UI/UX 細節、組件設計、狀態管理、API 集成和前端標準。能在需要時建議新的前端相關 Prompts。
*   **`backend-design.role.md`**:
    *   **角色:** 後端設計與工程顧問 (含工具建議)
    *   **目的:** 專注於伺服器端邏輯、數據庫交互、API 實現、性能、安全。能在需要時建議新的後端相關 Prompts。
*   **`database-design.role.md`**:
    *   **角色:** 資料庫設計與管理顧問 (含工具建議)
    *   **目的:** 專注於 Schema 設計、索引、查詢優化、數據完整性。能在需要時建議新的資料庫相關 Prompts。
*   **`devops-setup.role.md`**:
    *   **角色:** DevOps 與基礎設施顧問 (含工具建議)
    *   **目的:** 專注於基礎設施 (IaC)、CI/CD Pipeline、容器化、監控、部署。能在需要時建議新的 DevOps 相關 Prompts。
*   **`qa-plan.role.md`**:
    *   **角色:** QA 與測試策略師 (含工具建議)
    *   **目的:** 專注於測試策略、計劃、案例設計、自動化策略。能在需要時建議新的 QA 相關 Prompts。

## 初始工具/執行 Prompts (`*.exec.md`)

這些自動化常見的設置和生成任務。

*   **`eng-init-node-ts.exec.md`**: 初始化一個標準的 Node.js + TypeScript 專案（含 Linter/Formatter）。
*   **`git-init-repo.exec.md`**: 初始化 Git 倉庫，會檢查是否已存在。
*   **`git-commit-conventional.exec.md`**: 輔助生成符合 Conventional Commits 規範（內嵌規則，描述使用繁體中文）的提交訊息（基於暫存區變更）。
*   **`qa-test-case-generator.exec.md`**: 根據提供的上下文生成基礎測試案例大綱的 Markdown 文件。
*   **`general-decision-log-entry.exec.md`**: 引導使用者將關鍵決策記錄到 `DECISION_LOG.md`。
*   **`docs-generate-readme-structure.exec.md`**: 創建一個標準的 `README.md` 文件結構。
*   **`create-react-component-files.exec.md`**: 為新的 React 組件創建一套標準文件（.tsx, .module.css, index.ts, 可選的 test/story）。*(請根據您的框架調整)*

## 補充性角色 Prompts (`*.role.md`)

用於特定輔助的可選 Prompts。

*   **`general-explain-code.role.md`**: 解釋選定的代碼片段。
*   **`general-refactor-advisor.role.md`**: 為選定的代碼建議重構技巧。
*   **`tech-lead-architecture-review.role.md`**: 基於原則和質量屬性提供高層級的架構審查。

## 如何使用

1.  **從 PM 開始：** 使用 `pm-define-role.role.md` 澄清需求並生成專案大綱文本。保存為 `PROJECT_OUTLINE.md`。
2.  **與 PjM 規劃：** 載入 `pjm-define-role.role.md` 並提供 `PROJECT_OUTLINE.md`。合作生成執行藍圖與任務列表文本。保存為 `EXECUTION_BLUEPRINT.md`。注意第一個任務和建議的核心角色 Prompt。
3.  **更新全局指示：** 確保 `.github/copilot-instructions.md` 包含專案標準（技術棧、提交格式等）。
4.  **按順序細化任務：**
    *   載入 PjM 為當前任務建議的核心角色 Prompt（例如 `database-design.role.md`）。
    *   提供 `EXECUTION_BLUEPRINT.md` 中的相關上下文。
    *   與 AI 專家討論並細化任務。如果此專家建議創建一個*新的*專業化 Prompt，可以考慮創建。
    *   將詳細設計記錄下來（例如，在 `DatabaseSchema.md` 中）。
5.  **返回 PjM 審核：** 重新載入 `pjm-define-role.role.md`。提供詳細設計供其審核。
6.  **使用 Agent 執行：** 一旦 PjM 確認了詳細計劃，創建必要的 `*.exec.md` Prompt（可能在專家角色 AI 的幫助下）並使用 Agent (`@agent /exec ...`) 運行它。
7.  **重複：** 回到 PjM 確認執行（可選）並獲取藍圖中的下一個任務/角色建議。繼續這個循環（細化 -> 審核 -> 執行 -> 下一步）。
8.  **使用工具/補充 Prompts：** 在整個過程中根據需要使用 `exec` Prompts 進行自動化，或使用補充性角色 Prompts 獲取特定幫助（代碼解釋、重構等）。

*(請記得替換佔位符，例如 `[您的專案名稱]` 和 `[連結至您的命名規範文檔]`)*