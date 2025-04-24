# Hand-crank-drink-ordering-machine

## 虛擬機建立與啟用

1. **建立虛擬環境**  
   使用以下指令建立虛擬環境：
   ```bash
   python -m venv venv
   ```

2. **啟用虛擬環境**  
   - 在 Windows 上執行：
     ```bash
     .\venv\Scripts\activate
     ```
   - 在 macOS/Linux 上執行：
     ```bash
     source venv/bin/activate
     ```

3. **安裝相依套件**  
   確保虛擬環境啟用後，執行以下指令安裝必要的相依套件：
   ```bash
   pip install -r requirements.txt
   ```

4. **停用虛擬環境**  
   完成後可使用以下指令停用虛擬環境：
   ```bash
   deactivate
   ```

# Github Copilot Prompts 與 Cursor Rules 整合指南

這個專案整合了 Github Copilot Prompts 和 Cursor Rules，提供完整的開發工作流程指導。

## 目錄結構

```
project/
├── .cursor/
│   └── rules/          # Cursor Rules 存放目錄
├── .github/
│   └── copilot-instructions.md  # Copilot 全局指導
├── pjm-define-role.role.prompt.mdc  # 專案管理角色定義
├── pm-define-role.role.prompt.mdc   # 產品管理角色定義
├── RULES_MAPPING.md    # 規則集對照表
└── README.md           # 本文件
```

## Cursor Rules 整合

本專案使用 Cursor Rules 來確保代碼品質和開發標準的一致性。詳細的規則對照表請參考 `RULES_MAPPING.md`。

### 使用方式

1. **安裝必要工具**
   - 安裝 Cursor AI
   - 安裝 vscode-cursor-rules 擴充功能

2. **選擇適當的規則集**
   - 查看 `RULES_MAPPING.md` 了解可用的規則集
   - 根據專案需求選擇合適的規則

3. **整合到工作流程**
   - 在任務規劃時參考規則集
   - 在開發過程中遵循選定的規則
   - 在代碼審查時使用規則作為標準

## 工作流程

1. **專案初始化**
   - 使用 PM Role 確定需求
   - 使用 PJM Role 規劃執行藍圖
   - 選擇適當的 Cursor Rules

2. **開發流程**
   - 遵循選定的規則集進行開發
   - 使用 Cursor AI 協助確保符合規則
   - 定期審查和更新規則使用情況

3. **品質保證**
   - 使用測試相關規則集
   - 執行代碼審查
   - 確保符合專案標準

## 更新和維護

- 定期檢查規則集是否需要更新
- 根據專案需求調整規則使用方式
- 記錄規則使用經驗和最佳實踐

## 相關文件

- [專案管理角色定義](./pjm-define-role.role.prompt.mdc)
- [產品管理角色定義](./pm-define-role.role.prompt.mdc)
- [規則對照表](./RULES_MAPPING.md)

# Cursor AI 專案開發流程指南

## 目錄結構