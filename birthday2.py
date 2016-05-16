import datetime,math #datetime,calendar,mathモジュール
def Birthday(year,month,day): #Birthday関数
    """本日を日数として含めない"""
    birth_day=datetime.date(year,month,day) #誕生日の情報を取得
    how_date=(datetime.date.today()-birth_day).days
    print("今日で"+str(how_date)+"日") #生きてきた日数を表示
    print()
    if 0 not in [how_date%x for x in range(2,int(math.sqrt(how_date))+1)]: #素数チェック
        print(str(how_date)+"は素数である")
    else:
        print(str(how_date)+"は素数ではない")
Birthday(1995,3,25)