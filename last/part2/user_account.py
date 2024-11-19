from nicegui import ui

class UserAccount():
    def __init__(self):
        self.accounts = []  # 存儲帳號資料
        self.grid = None    # AgGrid 表格
        self.account_input = None
        self.password_input = None
        self.email_input = None
        self.phone_input = None

    def display(self):
        with ui.card():
            with ui.column().classes('w-80 h-80 '):
                self.account_input = ui.input(label='帳號:', placeholder='請輸入您的帳號').classes('w-full')
                self.password_input = ui.input(label='密碼:', placeholder='請輸入您的密碼', password=True).classes('w-full')
                self.email_input = ui.input(label='電子郵件:', placeholder='請輸入您的電子郵件').classes('w-full')
                self.phone_input = ui.input(label='電話號碼:', placeholder='請輸入您的電話號碼').classes('w-full')

            with ui.row():
                ui.button('新增', on_click=self.add_account)  # 綁定新增功能
                ui.button('刪除', on_click=self.delete_account)  # 綁定刪除功能

            options = {
                'defaultColDef': {'flex': 1},  # 自適應列寬
                'columnDefs': [
                    {'headerName': '選擇', 'field': 'selected', 'checkboxSelection': True},  # 增加選擇框
                    {'headerName': '帳號', 'field': 'name', 'editable': True},  # 可編輯的帳號欄
                    {'headerName': '密碼', 'field': 'password', 'editable': True},  # 可編輯的密碼欄
                    {'headerName': '電子郵件', 'field': 'email', 'editable': True},  # 可編輯的電子郵件欄
                    {'headerName': '電話號碼', 'field': 'phone', 'editable': True},  # 可編輯的電話號碼欄
                ],
                'rowData': self.accounts,  # 初始資料為空
                'rowSelection': 'multiple',  # 支援多選
            }
            self.grid = ui.aggrid(options=options).classes('max-h-40')

    def refresh(self):
        """更新 AgGrid 表格的顯示資料。"""
        self.grid.options['rowData'] = self.accounts  # 設定新的資料
        self.grid.update()  # 更新顯示

    async def delete_account(self):
        selected_rows = await self.grid.get_selected_rows()  # 獲取選中的行
        if selected_rows:
            selected_accounts = {row['name'] for row in selected_rows}  # 提取選中的帳號
            self.accounts = [row for row in self.accounts if row['name'] not in selected_accounts]  # 過濾掉選中的帳號
            self.refresh()  # 刷新顯示

    def add_account(self):
        account = self.account_input.value
        password = self.password_input.value
        email = self.email_input.value
        phone = self.phone_input.value
        if account and password:
            new_entry = {'name': account, 'password': password, 'email': email, 'phone': phone}  # 確保新增的資料格式正確
            self.accounts.append(new_entry)  # 新增到列表
            self.refresh()  # 更新表格
            self.account_input.value = ''  # 清空輸入框
            self.password_input.value = ''  # 清空輸入框
            self.email_input.value = ''  # 清空輸入框
            self.phone_input.value = '' # 清空輸入框

