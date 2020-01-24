import requests

url = 'https://yandex.ru/maps/-/CGWdv8id'

response = requests.get(url)
text = response.text
print(text)


# 

# import json
# import sys
# 
# from openpyxl import Workbook, load_workbook
# from openpyxl.styles import PatternFill
# from PySide2 import QtCore, QtGui
# from PySide2.QtWidgets import (
#     QApplication, QComboBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QVBoxLayout, QWidget)
# 
# 
# class MyWidget(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setWeight(75)
#         font.setItalic(False)
#         font.setBold(False)
# 
#         # with open("accounts.json", "r") as read_file:
#         #     self.accounts = json.load(read_file)
# 
#         self.layoutAddAccout = QHBoxLayout()
#         self.labelAdding = QLabel("Добавление")
#         self.labelAdding.setFont(font)
#         self.edidAccountLine = QLineEdit()
#         self.edidAccountLine.setFixedSize(296, 25)
#         self.edidAccountLine.setPlaceholderText("Новый аккаунт")
#         self.edidAccountLine.setFont(font)
#         self.edidAccountLine.setContentsMargins(10, 0, 0, 0)
#         self.editAccountAddBtn = QPushButton("+")
#         self.editAccountAddBtn.setFixedSize(25, 25)
#         self.editAccountAddBtn.setFont(font)
#         self.editAccountAddBtn.setContentsMargins(20, 0, 0, 0)
#         self.layoutAddAccout.addWidget(self.labelAdding)
#         self.layoutAddAccout.addWidget(self.edidAccountLine)
#         self.layoutAddAccout.addWidget(self.editAccountAddBtn)
#         self.layoutAddAccout.addStretch()
# 
#         self.layoutDelAccout = QHBoxLayout()
#         self.labelDeliting = QLabel("Удаление")
#         self.labelDeliting.setFont(font)
#         self.comboAccountDel = QComboBox()
#         # self.comboAccountDel.addItems(self.accounts)
#         self.comboAccountDel.addItems(["11", "22"])
#         self.comboAccountDel.setFont(font)
#         self.comboAccountDel.setContentsMargins(10, 10, 10, 10)
#         self.editAccountDelBtn = QPushButton("-")
#         self.editAccountDelBtn.setFixedSize(25, 25)
#         self.editAccountDelBtn.setFont(font)
#         self.layoutDelAccout.addWidget(self.labelDeliting)
#         self.layoutDelAccout.addWidget(self.comboAccountDel)
#         self.layoutDelAccout.addWidget(self.editAccountDelBtn)
#         self.layoutDelAccout.addStretch()
# 
#         self.layoutTableCompetition = QHBoxLayout()
#         self.table = QTableWidget()
#         self.rows = 3
#         self.column = 3
#         self.table.setRowCount(self.rows)
#         self.table.setColumnCount(self.column)
#         self.layoutTableCompetition.addWidget(self.table)
#         self.layoutTableCompetition.addStretch()
# 
#         self.action = ["Подписаться на", "Лайкнуть", "Прокомментровать"]
#         self.table.setHorizontalHeaderLabels(["Действие", "Аккаунт", "Пост"])
# 
#         for i in range(self.rows):
#             self.comboAction = QComboBox()
#             self.comboAction.addItems(self.action)
#             self.comboAccount = QComboBox()
#             self.comboAccount.addItems(["11", "22"])
#             self.table.setCellWidget(i, 0, self.comboAction)
#             self.table.setCellWidget(i, 1, self.comboAccount)
# 
#         self.table.setColumnWidth(0, 180)
#         self.table.setColumnWidth(1, 120)
#         self.table.setColumnWidth(2, 200)
#         self.table.setFixedWidth(700)
# 
#         self.button = QPushButton("Начать")
#         self.button.setFixedSize(100, 50)
#         self.button.setFont(font)
# 
#         self.buttonAddRow = QPushButton("+")
#         self.buttonAddRow.setFixedSize(100, 50)
#         self.buttonAddRow.setFont(font)
# 
#         self.buttonRemoveRow = QPushButton("-")
#         self.buttonRemoveRow.setFixedSize(100, 50)
#         self.buttonRemoveRow.setFont(font)
# 
#         self.layoutMain = QVBoxLayout()
#         self.layoutMain.addLayout(self.layoutAddAccout)
#         self.layoutMain.addLayout(self.layoutDelAccout)
#         self.layoutMain.addLayout(self.layoutTableCompetition)
#         self.layoutMain.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
#         self.layoutMain.addWidget(self.buttonAddRow, alignment=QtCore.Qt.AlignCenter)
#         self.layoutMain.addWidget(self.buttonRemoveRow, alignment=QtCore.Qt.AlignCenter)
# 
#         self.setLayout(self.layoutMain)
# 
#         self.editAccountAddBtn.clicked.connect(self.addAccount)
#         self.editAccountDelBtn.clicked.connect(self.delAccount)
#         self.button.clicked.connect(self.calc)
#         self.buttonAddRow.clicked.connect(self.add_row)
#         self.buttonRemoveRow.clicked.connect(self.remove_row)
# 
#     def updateAccount(self, accounts):
#         with open("accounts.json", "w") as write_file:
#             json.dump(accounts, write_file)
#         for i in range(self.rows):
#             self.comboAccount = QComboBox()
#             self.comboAccount.addItems(accounts)
#             self.table.setCellWidget(i, 1, self.comboAccount)
#         self.accounts = accounts
# 
#     def addAccount(self):
#         accounts = [self.comboAccountDel.itemText(i) for i in range(self.comboAccountDel.count())]
#         if self.edidAccountLine.text():
#             new_account = self.edidAccountLine.text()
#             if new_account not in accounts:
#                 accounts.append(new_account)
#         self.comboAccountDel.addItem(new_account)
#         self.updateAccount(accounts)
# 
#     def delAccount(self):
#         self.comboAccountDel.removeItem(self.comboAccountDel.currentIndex())
#         accounts = [self.comboAccountDel.itemText(i) for i in range(self.comboAccountDel.count())]
#         self.updateAccount(accounts)
# 
#     def add_row(self):
#         currentRowCount = self.table.rowCount()
#         self.table.insertRow(currentRowCount)
#         self.comboAction = QComboBox()
#         self.comboAction.addItems(self.action)
#         self.comboAccount = QComboBox()
#         self.comboAccount.addItems(self.accounts)
#         self.table.setCellWidget(currentRowCount, 0, self.comboAction)
#         self.table.setCellWidget(currentRowCount, 1, self.comboAccount)
# 
#     def remove_row(self):
#         currentRowCount = self.table.rowCount()
#         self.table.removeRow(currentRowCount - 1)
# 
#     def get_info_from_table(self):
#         account = {
#             "ekokman": {
#                 "account": None,
#                 "followers": None,
#                 "likes": None,  # ['artempacholchyk', 'ledneek', ...]
#                 "comments": None,
#             }
#         }
#         accounts = {}
#         for i in range(self.table.rowCount()):
#             l = []
#             for j in range(self.table.columnCount()):
#                 combo = self.table.cellWidget(i, j)
#                 if combo:
#                     value = combo.currentText()
#                 elif self.table.item(i, j):
#                     value = self.table.item(i, j).text()
#                 else:
#                     value = None
#                 l.append(value)
#             if not l[1] in accounts:
#                 accounts[l[1]] = {"followers": None, "likes": None, "comments": None}
#             if l[0] == "Подписаться на":
#                 accounts[l[1]]["followers"] = True
#             else:
#                 key = "likes" if l[0] == "Лайкнуть" else "comments"
#                 if not accounts[l[1]][key]:
#                     accounts[l[1]][key] = [int(l[2])]
#                 else:
#                     accounts[l[1]][key].append(int(l[2]))
# 
#         return accounts
# 
#     # def calc(self):
#     #     accounts = self.get_info_from_table()
#     #     print(accounts)
#     #     # accounts = {'ekokman': {'followers': True, 'likes': [1], 'comments': [1]}, 'ledneek': {'followers': True, 'likes': [2], 'comments': None}}
#     #     # accounts = {'ekokman': {'followers': True, 'likes': [5], 'comments': [5]}}
#     #     # accounts_records = {}
#     #     # agent = None
#     #     # for account in accounts.keys():
#     #     #     _account = account
#     #     #     accounts_records[account] = {}
#     #     #     if accounts[account]['followers']:
#     #     #         followers = get_followers(_account)
#     #     #         accounts_records[account]['followers'] = followers
#     #     #     if accounts[account]['likes'] or accounts[account]['comments']:
#     #     #         media = get_media(_account, agent)
#     #     #     if accounts[account]['likes']:
#     #     #         accounts_records[account]['likes'] = []
#     #     #         for l in accounts[account]['likes']:
#     #     #             post = media[l-1]
#     #     #             likes = get_likes(post, agent)
#     #     #             accounts_records[account]['likes'].append(likes)
#     #     #     if accounts[account]['comments']:
#     #     #         comments = get_comments(post, agent)
#     #     #         accounts_records[account]['comments'] = [comments]
#     #     # print(accounts_records)
#     #
#     #
#     #     # records = {
#     #     #     'accounts':{
#     #     #         'ekokman':{
#     #     #             'account': Account('ekokman'),#instagram.entities.Account
#     #     #             'followers': get_followers(), #['artempacholchyk', 'ledneek', ...]
#     #     #             'likes': get_likes(),         #['artempacholchyk', 'ledneek', ...]
#     #     #             'comments': get_comments()
#     #     #         }
#     #     #     }
#     #     # }
# 
#     def calc(self):
#         accounts = self.get_info_from_table()
#         print(accounts)
#         # accounts = {'ekokman': {'followers': True, 'likes': [1], 'comments': [1]},
#         #             'ledneek': {'followers': True, 'likes': [2], 'comments': [2]}}
#         # accounts = {'ekokman': {'followers': True, 'likes': [1, 2], 'comments': [5]}}
#         # accounts = {
#         #     'ledneek': {'followers': True, 'likes': [1], 'comments': None},
#         #     'ekokman': {'followers': True, 'likes': [2, 1], 'comments': [1]}
#         # }
# 
#         l_and_f = {"likes": [], "comments": [], "follow": []}
#         agent = None
#         for account in accounts.keys():
#             _account = account
#             if accounts[account]["followers"]:
#                 followers = get_followers(_account)
#                 l_and_f["follow"].append({f"{account}": followers})
# 
#             if accounts[account]["likes"] or accounts[account]["comments"]:
#                 media = get_media(_account, agent)
# 
#             if accounts[account]["likes"]:
#                 for l in accounts[account]["likes"]:
#                     post = media[l - 1]
#                     likes = get_likes(post, agent)
#                     l_and_f["likes"].append({f"{account} пост {l}": likes})
# 
#             if accounts[account]["comments"]:
#                 for c in accounts[account]["comments"]:
#                     post = media[c - 1]
#                     comments = get_comments(post, agent)
#                     l_and_f["comments"].append({f"{account} пост {c}": comments})
# 
#         comments = l_and_f["comments"]
#         records = {}
#         for i, comment in enumerate(comments):
#             [(header_c, comment)] = list(comment.items())
#             records[header_c] = []
#             for c in comment:
#                 create_at = "2019-12-17 13:58"  # = datetime.datetime.fromtimestamp(c.created_at)
#                 comment_owner = "1"  # =str(c.owner)
#                 comment_text = "@wqq"  # = str(c.text)
#                 record = {"Когда": create_at, "Кто": comment_owner, "Комментарий": comment_text}
#                 likes = l_and_f["likes"]
#                 if likes:
#                     for i, like in enumerate(likes):
#                         [(header_l, like)] = list(like.items())
#                         record[f"Лайк у {header_l}"] = is_like(comment_owner, like)
#                 follow = l_and_f["follow"]
#                 if follow:
#                     for i, f in enumerate(follow):
#                         [(header_f, f)] = list(f.items())
#                         record[f"Подписка на {header_f}"] = is_follower(comment_owner, f)
# 
#                 records[header_c].append(record)
# 
#         with open("1.json", "w", encoding="cp1251") as f:
#             json.dump(records, f, indent=4, ensure_ascii=False)
#         with open("l_and_f.json", "w", encoding="cp1251") as f:
#             json.dump(l_and_f, f, indent=4, ensure_ascii=False)
#         preparing_records("1.json")
#         write_l_and_f("l_and_f.json")
# 
# 
# def authorise(account, password):
#     pass
# 
# 
# def get_followers(account):
#     followers = [1, 2, 3, 4]
# 
#     return [str(follower) for follower in followers]
# 
# 
# def get_likes(post, agent):
#     likes = [1, 2, 3]
#     return [str(like) for like in likes]
# 
# 
# def get_comments(media, agent):
#     comments = [1, 2, 3]
#     return [str(comment) for comment in comments]
# 
# 
# def get_media(account, agent):
#     media = [1, 2, 3]
#     return [str(m) for m in media]
# 
# 
# def is_like(comment_owner, likes):
#     return "+" if comment_owner in likes else "-"
# 
# 
# def is_follower(comment_owner, followers):
#     return "+" if comment_owner in followers else "-"
# 
# 
# def calc():
#     accounts = {
#         "ekokman": {"followers": True, "likes": [1], "comments": [1]},
#         "ledneek": {"followers": True, "likes": [2], "comments": [2]},
#     }
#     # accounts = {'ekokman': {'followers': True, 'likes': [1, 2], 'comments': [5]}}
#     # accounts = {
#     #     'ledneek': {'followers': True, 'likes': [1], 'comments': None},
#     #     'ekokman': {'followers': True, 'likes': [2, 1], 'comments': [1]}
#     # }
# 
#     l_and_f = {"likes": [], "comments": [], "follow": []}
#     agent = None
#     for account in accounts.keys():
#         _account = account
#         if accounts[account]["followers"]:
#             followers = get_followers(_account)
#             l_and_f["follow"].append({f"{account}": followers})
# 
#         if accounts[account]["likes"] or accounts[account]["comments"]:
#             media = get_media(_account, agent)
# 
#         if accounts[account]["likes"]:
#             for l in accounts[account]["likes"]:
#                 post = media[l - 1]
#                 likes = get_likes(post, agent)
#                 l_and_f["likes"].append({f"{account} пост {l}": likes})
# 
#         if accounts[account]["comments"]:
#             for c in accounts[account]["comments"]:
#                 post = media[c - 1]
#                 comments = get_comments(post, agent)
#                 l_and_f["comments"].append({f"{account} пост {c}": comments})
# 
#     comments = l_and_f["comments"]
#     records = {}
#     for i, comment in enumerate(comments):
#         [(header_c, comment)] = list(comment.items())
#         records[header_c] = []
#         for c in comment:
#             create_at = "2019-12-17 13:58"  # = datetime.datetime.fromtimestamp(c.created_at)
#             comment_owner = "1"  # =str(c.owner)
#             comment_text = "@wqq"  # = str(c.text)
#             record = {"Когда": create_at, "Кто": comment_owner, "Комментарий": comment_text}
#             likes = l_and_f["likes"]
#             if likes:
#                 for i, like in enumerate(likes):
#                     [(header_l, like)] = list(like.items())
#                     record[f"Лайк у {header_l}"] = is_like(comment_owner, like)
#             follow = l_and_f["follow"]
#             if follow:
#                 for i, f in enumerate(follow):
#                     [(header_f, f)] = list(f.items())
#                     record[f"Подписка на {header_f}"] = is_follower(comment_owner, f)
# 
#             records[header_c].append(record)
# 
#     with open("1.json", "w", encoding="cp1251") as f:
#         json.dump(records, f, indent=4, ensure_ascii=False)
#     with open("l_and_f.json", "w", encoding="cp1251") as f:
#         json.dump(l_and_f, f, indent=4, ensure_ascii=False)
# 
# 
# def preparing_records(path_to_json):
#     with open(path_to_json, "r", encoding="cp1251") as f:
#         data = json.load(f)
#     [[headers, *_], *_] = list(data.values())
#     headers = list(headers.keys())
#     records = {}
#     for key, value in data.items():
#         name_tab = key
#         records[name_tab] = [headers]
#         for v in value:
#             record = []
#             for i in v.values():
#                 record.append(i)
#             records[name_tab].append(record)
#     sheet = 0
#     for key, value in records.items():
#         headers = value.pop(0)
#         value = sorted(value, key=lambda v: v[0])
#         headers.insert(0, "Номер")
#         for i, v in enumerate(value):
#             # valid_comment = is_valid_comment(record[1], record[2])
#             # record.append(valid_comment)
#             # record[0] = record[0].strftime('%d.%m.%Y %H:%M')
#             v.insert(0, str(i + 1))
#         value.insert(0, headers)
# 
#         write_records(tab=key, records=value, sheet=sheet)
#         sheet += 1
# 
#     # print(accounts_records)
# 
# 
# def write_records(tab, records, sheet):
#     red = PatternFill(start_color="FE0303", end_color="FE0303", fill_type="solid")
#     green = PatternFill(start_color="01BA00", end_color="01BA00", fill_type="solid")
#     try:
#         wb = load_workbook("comp.xlsx")
#     except FileNotFoundError:
#         wb = Workbook()
#     ws = wb.create_sheet(tab, sheet)
#     for r, row in enumerate(records):
#         for c, col in enumerate(row):
#             cell = ws.cell(r + 1, c + 1)
#             cell.value = col
#             if col == "+":
#                 cell.fill = green
#             elif col == "-":
#                 cell.fill = red
#     wb.save("comp.xlsx")
# 
# 
# def get_worksheet(wb, tab):
#     last_ws = wb.worksheets[-1]
#     last_ws_index = wb.index(last_ws)
#     ws = wb.create_sheet(tab, last_ws_index)
#     return ws
# 
# 
# def write_l_and_f(path_to_json):
#     try:
#         wb = load_workbook("comp.xlsx")
#     except FileNotFoundError:
#         wb = Workbook()
# 
#     wb.save("comp.xlsx")
#     with open(path_to_json, "r", encoding="cp1251") as f:
#         data = json.load(f)
#     for key, value in data.items():
#         if key in ("likes", "follow"):
#             suf = "Лайки" if key == "likes" else "Подписчики"
#             for val in value:
#                 for k, v in val.items():
#                     ws = get_worksheet(wb, tab=suf + " " + k)
#                     for i, c in enumerate(v):
#                         cell = ws.cell(i + 1, column=1)
#                         cell.value = c
# 
#     wb.save("comp.xlsx")
# 
# 
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()
#     sys.exit(app.exec_())
# 
#     # calc()
#     # preparing_records('1.json')
#     # write_l_and_f('l_and_f.json')
