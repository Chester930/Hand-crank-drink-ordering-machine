# Execution Prompt: Initialize Node.js + TypeScript Project

# Goal: Set up a basic Node.js project with TypeScript, ESLint, Prettier.
# 目標：建立基礎 Node.js + TypeScript 專案 (含 Linter/Formatter)。

**Instructions:**

1.  `@terminal /exec` Run: `npm init -y`
    # 初始化 package.json
2.  `@terminal /exec` Run: `npm install typescript @types/node ts-node nodemon --save-dev`
    # 安裝 TypeScript 開發依賴
3.  `@terminal /exec` Run: `npm install eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin prettier eslint-config-prettier eslint-plugin-prettier --save-dev`
    # 安裝 ESLint & Prettier 開發依賴
4.  `@workspace /newFile --path="tsconfig.json"` Create `tsconfig.json`.
    # 建立 TypeScript 配置文件
5.  `@workspace /applyEdit --path="tsconfig.json"` Write basic TypeScript configuration:
    # 寫入基礎 TS 配置
    ```json
    {
      "compilerOptions": {
        "target": "ES2016",
        "module": "CommonJS",
        "outDir": "./dist",
        "rootDir": "./src",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true,
        "resolveJsonModule": true
      },
      "include": ["src/**/*"],
      "exclude": ["node_modules", "**/*.spec.ts", "**/*.test.ts"]
    }
    ```
6.  `@workspace /newFile --path=".eslintrc.js"` Create `.eslintrc.js`.
    # 建立 ESLint 配置文件
7.  `@workspace /applyEdit --path=".eslintrc.js"` Write basic ESLint configuration:
    # 寫入基礎 ESLint 配置
    ```javascript
    module.exports = {
      parser: '@typescript-eslint/parser',
      extends: [
        'plugin:@typescript-eslint/recommended',
        'plugin:prettier/recommended',
      ],
      parserOptions: {
        ecmaVersion: 2020,
        sourceType: 'module',
      },
      rules: {},
    };
    ```
8.  `@workspace /newFile --path=".prettierrc"` Create `.prettierrc`.
    # 建立 Prettier 配置文件
9.  `@workspace /applyEdit --path=".prettierrc"` Write basic Prettier configuration:
    # 寫入基礎 Prettier 配置
    ```json
    {
      "semi": true,
      "singleQuote": true,
      "trailingComma": "es5",
      "printWidth": 80
    }
    ```
10. `@workspace /newFile --path=".gitignore"` Create `.gitignore`.
    # 建立 .gitignore 文件
11. `@workspace /applyEdit --path=".gitignore"` Add common Node.js ignores:
    # 添加 Node.js 忽略項
    ```gitignore
    node_modules/
    dist/
    .env
    *.log
    npm-debug.log*
    yarn-debug.log*
    yarn-error.log*
    ```
12. `@workspace /createDirectory --path="src"` Create `src` directory.
    # 建立 src 源碼目錄
13. `@workspace /newFile --path="src/index.ts"` Create entry file `src/index.ts`.
    # 建立入口文件
14. `@workspace /applyEdit --path="src/index.ts"` Add simple console log:
    # 添加示例代碼
    ```typescript
    console.log('Hello, TypeScript Node.js project!');
    ```
15. `@workspace /updateFile --path="package.json"` Add scripts to `package.json`:
    # 添加 npm 腳本 (start, dev, build, lint, format)
    *   Find the `"scripts"` section.
    *   Add/update the following scripts:
        ```json
        "start": "node dist/index.js",
        "dev": "nodemon src/index.ts",
        "build": "tsc",
        "lint": "eslint . --ext .ts",
        "lint:fix": "eslint . --ext .ts --fix",
        "format": "prettier --write \"src/**/*.ts\""
        ```
16. `@workspace /showMessage` Display: "Node.js + TypeScript project initialized. Run 'npm install' then 'npm run dev'."
    # 顯示完成訊息