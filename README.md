# reminder
オンライン授業などで曜日感覚が失われ、知り合いなどが講義や提出物を忘れるなどということを頻繁に耳にした.
そこで対策として忘れていないかというリマインドをしてくれるものがあれば便利なのではないかと考え、作成を試みた.


# 使い方
サインアップのときにメールアドレスを入力してもらい、そこあてにリマインドのような形にしたい.
あるいはsnsのidなどを入力して人ごとにリマインドを通知する.
使い方としては時間割を設定し、授業のリマインドに関しては当日は前日、課題などについては授業日から一定の間隔で残りn日という風にリマインドを出すようにしたい.



#メモ
$ python manage.py cron
により手動でユーザーごとに設定しておいた先にlinenotifyで通知
今の所linenotifyで進める
