# reminder
オンライン授業などで曜日感覚が失われ、知り合いなどが講義や提出物を忘れるなどということを頻繁に耳にした。
そこで対策として忘れていないかというリマインドをしてくれるものがあれば便利なのではないかと考えた。


# 使い方
サインアップのときにメールアドレスを入力してもらい、そこあてにリマインドのような形にしたい
使い方としては時間割を設定し、授業のリマインドに関しては当日は前日、課題などについては授業日から一定の間隔で残りn日という風にリマインドを出すようにしたい。


#メモ

$ python manage.py cron
により手動であらかじめ設定しておいた先にラインの通知
