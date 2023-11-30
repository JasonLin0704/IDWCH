# IDWCH
I don't want to correct homework. 

<br/>

### 以下是中文說明：

目前的廢廢功能：
1. 把學生資料夾中的檔案 (包括 header file) 做分類，分到三個資料夾：c、cpp、pdf

    <操作方法>
    - 把所有作業載下來應該會有一大包，解壓縮後備用
    - 更改 homework_corrector.py 中的變數
      - hw_num 表示第幾次作業
      - hw_path 表示當前一大包作業的絕對路徑
        - e.g. *'/home/demo/Downloads/HW4'*
      - target_path 表示要新增三個資料夾在哪個絕對路徑上
        - e.g. *'/home/demo/Downloads'*
    - 執行 homework_corrector.py
   
   <注意事項>
   - 執行完最好再檢查一下是否所有檔案都搬過去了，因為有些同學沒依規定取名，檔案就會被留在原處，.h檔常常會亂取名
   - 目前是用 shutil.move() 直接搬動檔案，如此可以比較容易檢查哪些同學的資料夾還有東西沒搬到，若要用複製的方式全改成 shutil.copy() 即可

<br/>
<br/>

新增小功能:
1. 一次測試多人、多筆測資的script : check.sh

    <操作方法>
    - 把 input1.txt ~ input10.txt、answer1.txt~answer10.txt 放在測試目錄下
    - 如果要改變測資數量，在check.sh裡面 for i in seq(1 1 num)改變num
    - 把要測試的.c/.cpp檔也放進測試目錄下
    - ./check.sh
	  
    <待改進>
    - 有時候一個人的程式卡住，就會卡死後面所有人

    <執行範例>

    ![image](https://github.com/JasonLin0704/IDWCH/assets/71300686/1277338d-200d-46df-9626-d4edcd9d9ea4)

   
