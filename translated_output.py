from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint

# Selenium WebDriver を初期化します (この場合は Chrome を使用)
driver = webdriver.Chrome() # または、Firefox の場合は webdriver.Firefox() に置き換えます

def get_all_forms(url):
"""Web ページの 'url' で見つかったすべてのフォーム タグを返します"""
# URL を開きます
driver.get(url)

# ページが完全に読み込まれるまで待機します (JavaScript を多用するページの場合はオプション)
driver.implicitly_wait(5)

# JavaScript の実行後にページ ソースを取得します
page_source = driver.page_source

# BeautifulSoup で解析します
soup = BeautifulSoup(page_source, "html.parser")
return soup.find_all("form")

def get_form_details(form):
"""アクション、メソッド、フォーム コントロールのリストなど、フォームの HTML 詳細を返します(入力など)"""
details = {}
# フォームアクション (要求された URL) を取得します
action = form.attrs.get("action").lower()
# フォームメソッド (POST、GET、DELETE など) を取得します
method = form.attrs.get("method", "get").lower()
# すべてのフォーム入力を取得します
inputs = []

# 入力タグを処理します
for input_tag in form.find_all("input"):
input_type = input_tag.attrs.get("type", "text")
input_name = input_tag.attrs.get("name")
input_value = input_tag.attrs.get("value", "")
inputs.append({"type": input_type, "name": input_name, "value": input_value})

# 選択タグを処理します
for select in form.find_all("select"):
select_name = select.attrs.get("name")
select_type = "select"
select_options = []
select_default_value = ""
for select_option in select.find_all("option"):
option_value = select_option.attrs.get("value")
if option_value:
select_options.append(option_value)
if select_option.attrs.get("selected"):
select_default_value = option_value
if not select_default_value and select_options:
select_default_value = select_options[0]
inputs.append({"type": select_type, "name": select_name, "values": select_options, "value": select_default_value})

# textarea タグを処理
for textarea in form.find_all("textarea"):
textarea_name = textarea.attrs.get("name")
textarea_type = "textarea"
textarea_value = textarea.text
inputs.append({"type": textarea_type, "name": textarea_name, "value": textarea_value})

details["action"] = action
details["method"] = method
details["inputs"] = inputs

return details

if __name__ == "__main__":
# スクレイピングする URL を定義します
url = "https://www.amazon.com/"
forms = get_all_forms(url)

if not forms:
print("No forms found on the page.")
else:
for i, form in enumerate(forms, start=1):
form_details = get_form_details(form)
print("="*50, f"form #{i}", "="*50)
pprint(form_details)

# ブラウザ ウィンドウを閉じます
driver.quit()