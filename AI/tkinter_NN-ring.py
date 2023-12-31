import tkinter as tk
from tkinter import messagebox
import pickle
import getpass

# ログイン名の取得
user = getpass.getuser()


import numpy as np
with open(f"/Users/{user}/Desktop/rotaryNN.pickle", mode="rb") as f1:
        model1 = pickle.load(f1)
    
with open(f"/Users/{user}/Desktop/rotaryScaler.pickle", mode="rb") as f2:
    model2 = pickle.load(f2)
# /Users/yamamurokazuyuki/Desktop/rotaryScaler.pickle
# /Users/yamamurokazuyuki/Desktop/rotaryNN.pickle
def on_register():
    # 各エントリーフィールドから値を取得
    kaitennsuu = entry_kaitennsuu.get()
    sozaigaikei = entry_sozaigaikei.get()
    sozainaikei = entry_sozainaikei.get()
    motosozai = entry_motosozai.get()
    kakougosozai = entry_kakougosozai.get()
    kirikomi = entry_kirikomi.get()
    
    
    # 全てのフィールドが入力されているか確認
    if not (kaitennsuu and sozaigaikei and sozainaikei and motosozai and kakougosozai and kirikomi):
        messagebox.showwarning("警告", "すべてのフィールドを入力してください。")
        return
    def is_num(t: str) -> bool:
        try:
            float(t)
            return True
        except ValueError:
            return False
    
    if  not is_num (kaitennsuu) :
        messagebox.showwarning("警告", "回転数を数字で入力してください。")
        return
    if not is_num (sozaigaikei) :
        messagebox.showwarning("警告", "素材の外径を数字で入力してください。")
        return
    if not is_num (sozainaikei) :
        messagebox.showwarning("警告", "素材の内径を数字で入力してください。")
        return
    if not is_num (motosozai) :
        messagebox.showwarning("警告", "元の素材の厚みを数字で入力してください。")
        return
    if not is_num (kakougosozai) :
        messagebox.showwarning("警告", "加工後の素材の厚みを数字で入力してください。")
        return
    if not is_num (kirikomi) :
        messagebox.showwarning("警告", "切込量を数字で入力してください。")
        return
    
    kaitennsuu = float(kaitennsuu)
    sozaigaikei = float(sozaigaikei)
    sozainaikei = float(sozainaikei)
    motosozai  = float(motosozai )
    kakougosozai = float(kakougosozai)
    kirikomi = float(kirikomi)
    
    if  kaitennsuu > 130 :
        messagebox.showwarning("警告", "テーブル回転数は130以下にしてください")
        return
    if  kaitennsuu < 50 :
        messagebox.showwarning("警告", "テーブル回転数は50以上にしてください")
        return
    
    
    
    # 回転数
    kaitennsuu
    # 素材の大きさ
    sozaigaikei
    sozaigaikei += 20
    createXgaikei = np.array([[kaitennsuu, sozaigaikei]])
    #素材の反復径
    sozainaikei -= 50
    createXnaikei = np.array([[kaitennsuu, sozainaikei]])
    
    
    
    # 元
    motosozai
    # 狙い
    kakougosozai
    # 切込
    kirikomi
    # 加工量
    kakouryou = motosozai - kakougosozai
    kakouryou = round(kakouryou, 3)
    # 切込回数
    kirikomikaisuu = kakouryou / kirikomi

    kirikomikaisuu = round(kirikomikaisuu, 0)
    if kirikomikaisuu % 2 == 0:
         None
    else:
         kirikomikaisuu += 1
    kirikomikaisuu
    
    createXgaikeis = model2.transform(createXgaikei)
    createXnaikeis = model2.transform(createXnaikei)
    
    y_predcreateXgaikeis = model1.predict(createXgaikeis)
    y_predcreateXgaikeis = y_predcreateXgaikeis.tolist()
    CXgaikeis = y_predcreateXgaikeis[0]
    CXgaikeis = round(CXgaikeis, 0)
    y_predcreateXnaikeis = model1.predict(createXnaikeis)
    y_predcreateXnaikeis = y_predcreateXnaikeis.tolist()
    CXnaikeis = y_predcreateXnaikeis[0]
    CXnaikeis = round(CXnaikeis, 0)
    C = CXgaikeis - CXnaikeis
    
    
    
    print(f'テーブル変速{kaitennsuu}回転ワークの外径{sozaigaikei - 20}mmワークの内径{sozainaikei + 50}の時の砥石横軸移動時間は{C}秒です')
    print(f'加工にかかってしまう時間は{round((kirikomikaisuu * C) / 60, 1)}分')
    
    onetoisi = f"{C}秒"
    alltoisi = f"加工時間は{round((kirikomikaisuu * C) / 60, 1)}分"
    
    
    
    # 登録成功のメッセージボックスを表示
    messagebox.showinfo("情報", "情報が登録されました。")
    
    # テキストエリアに入力情報を表示
    info = f"""
加工量:{kakouryou}mm
必要砥石移動回数: {kirikomikaisuu}回
砥石横断時間（１回分):{onetoisi}
<<<{alltoisi}>>>
 """

    

    text_area.insert(tk.END, info)

app = tk.Tk()
app.title("PRG8DXNCリング加工時間推定")
tk.Entry(validate='all')
# 各ラベルとエントリーフィールドを作成し、gridで配置
label_kaitennsuu = tk.Label(app, text="テーブル回転数(50~130回の間)", anchor=tk.CENTER)
label_kaitennsuu.grid(row=0, column=0)

entry_kaitennsuu = tk.Entry(app)
entry_kaitennsuu.grid(row=0, column=1)

label_sozaigaikei = tk.Label(app, text="素材の外径(50~550mmの間)", anchor=tk.CENTER)
label_sozaigaikei.grid(row=1, column=0)

entry_sozaigaikei = tk.Entry(app)
entry_sozaigaikei.grid(row=1, column=1)

label_sozainaikei = tk.Label(app, text="素材の内径(50~550mmの間)", anchor=tk.CENTER)
label_sozainaikei.grid(row=2, column=0)

entry_sozainaikei = tk.Entry(app)
entry_sozainaikei.grid(row=2, column=1)

label_motosozai = tk.Label(app, text="現在の素材の厚み(mm)", anchor=tk.CENTER)
label_motosozai.grid(row=3, column=0)

entry_motosozai = tk.Entry(app)
entry_motosozai.grid(row=3, column=1)

label_kakougosozai = tk.Label(app, text="加工後の素材の厚み(mm)", anchor=tk.CENTER)
label_kakougosozai.grid(row=4, column=0)

entry_kakougosozai = tk.Entry(app)
entry_kakougosozai.grid(row=4, column=1)

label_kirikomi = tk.Label(app, text="切込量(mm) ※10μmなら0.01mm", anchor=tk.CENTER)
label_kirikomi.grid(row=5, column=0)

entry_kirikomi = tk.Entry(app)
entry_kirikomi.grid(row=5, column=1)


# 登録ボタンを作成し、クリックイベントをバインド
button_register = tk.Button(app, text="AI推定", command=on_register)
button_register.grid(row=7, column=0, columnspan=2)

# テキストエリアを作成
text_area = tk.Text(app, height=30, width=40)
text_area.grid(row=8, column=0, columnspan=2)

app.mainloop()