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