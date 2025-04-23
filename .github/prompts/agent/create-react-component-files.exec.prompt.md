# Execution Prompt: Create React Component File Set

# Goal: Automatically create a standard set of files for a new React component (TypeScript).
# 目標：為新的 React 組件（使用 TypeScript）自動創建一套標準文件。

**Context Assumption:** Assumes a common React project structure where components reside in `src/components` or similar. Assumes TypeScript (`.tsx`) and CSS Modules (`.module.css`) are used, adjust if needed.

**Instructions:**

1.  `@workspace /input --prompt="Enter the Component Name (PascalCase, e.g., UserProfile):"` Store as `{componentName}`.
    # 提示使用者輸入組件名稱 (PascalCase)
2.  `@workspace /input --prompt="Enter the directory path for components (default: src/components):"` --value="src/components" Store as `{componentsPath}`.
    # 提示使用者輸入組件存放目錄 (預設 src/components)
3.  `@workspace /ask` Construct the component's directory path: `{componentDirPath} = "{componentsPath}/{componentName}"`.
    # 構建組件自身的目錄路徑
4.  `@workspace /createDirectory --path="{componentDirPath}"` Create the component's directory.
    # 創建組件目錄
5.  # Create Component File (.tsx)
    # 創建組件文件 (.tsx)
    `@workspace /newFile --path="{componentDirPath}/{componentName}.tsx"`
    `@workspace /applyEdit --path="{componentDirPath}/{componentName}.tsx"` Write basic component structure:
    # 寫入基礎組件結構
    ```typescript
    import React from 'react';
    import styles from './{componentName}.module.css';

    interface {componentName}Props {
      // TODO: Define component props
    }

    /**
     * TODO: Add component description
     */
    const {componentName}: React.FC<{componentName}Props> = (props) => {
      return (
        <div className={styles.wrapper} data-testid="{componentName}-wrapper">
          {/* TODO: Implement component structure */}
          {componentName} Component Placeholder
        </div>
      );
    };

    export default {componentName};
    ```
6.  # Create CSS Module File (.module.css)
    # 創建 CSS Module 文件 (.module.css)
    `@workspace /newFile --path="{componentDirPath}/{componentName}.module.css"`
    `@workspace /applyEdit --path="{componentDirPath}/{componentName}.module.css"` Write basic CSS rule:
    # 寫入基礎 CSS 規則
    ```css
    /* Styles for {componentName} component */
    .wrapper {
      /* TODO: Add component styles */
      padding: 1rem;
      border: 1px dashed #ccc; /* Placeholder border */
    }
    ```
7.  # Create Index File (index.ts for easier imports)
    # 創建索引文件 (index.ts 以便於導入)
    `@workspace /newFile --path="{componentDirPath}/index.ts"`
    `@workspace /applyEdit --path="{componentDirPath}/index.ts"` Write export statement:
    # 寫入導出語句
    ```typescript
    export { default } from './{componentName}';
    export * from './{componentName}'; // Optional: re-export props type if needed
    ```
8.  # (Optional) Create Storybook File (.stories.tsx) - Uncomment if using Storybook
    # （可選）創建 Storybook 文件 (.stories.tsx) - 如果使用 Storybook，取消註釋
    # `@workspace /newFile --path="{componentDirPath}/{componentName}.stories.tsx"`
    # `@workspace /applyEdit --path="{componentDirPath}/{componentName}.stories.tsx"` Write basic Storybook story:
    # # 寫入基礎 Storybook 故事
    # ```typescript
    # import React from 'react';
    # import { StoryFn, Meta } from '@storybook/react';
    # import {componentName} from './{componentName}'; // Adjust import if using index.ts
    #
    # export default {
    #   title: 'Components/{componentName}', // Adjust Storybook path as needed
    #   component: {componentName},
    #   // argTypes: { /* Define argTypes for props here */ },
    # } as Meta<typeof {componentName}>;
    #
    # const Template: StoryFn<typeof {componentName}> = (args) => <{componentName} {...args} />;
    #
    # export const Default = Template.bind({});
    # Default.args = {
    #   // TODO: Provide default props for the story
    # };
    # ```
9.  # (Optional) Create Test File (.test.tsx) - Uncomment if using Jest/RTL
    # （可選）創建測試文件 (.test.tsx) - 如果使用 Jest/RTL，取消註釋
    # `@workspace /newFile --path="{componentDirPath}/{componentName}.test.tsx"`
    # `@workspace /applyEdit --path="{componentDirPath}/{componentName}.test.tsx"` Write basic test structure:
    # # 寫入基礎測試結構
    # ```typescript
    # import React from 'react';
    # import { render, screen } from '@testing-library/react';
    # import '@testing-library/jest-dom';
    # import {componentName} from './{componentName}'; // Adjust import
    #
    # describe('{componentName} Component', () => {
    #   test('renders correctly with default props', () => {
    #     render(<{componentName} />);
    #     // Example assertion: Check if placeholder text is present
    #     expect(screen.getByText('{componentName} Component Placeholder')).toBeInTheDocument();
    #     // TODO: Add more specific assertions based on component implementation
    #   });
    #
    #   // TODO: Add more test cases for different props and interactions
    # });
    # ```
10. `@workspace /showMessage` Display message: "React component file set for '{componentName}' created in {componentDirPath}."
    # 顯示完成訊息