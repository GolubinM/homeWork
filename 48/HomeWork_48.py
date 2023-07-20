from jinja2 import Template

# task 1
users_l = [
    {'name': 'Иван', 'email': '2020@ya.ru'}, {'name': 'Данила', 'email': '2021@gmail.com'},
    {'name': 'Лука', 'email': '2022@gmail.com'}, {'name': 'Сергей', 'email': '2023@mail.ru'},
    {'name': 'Наталья', 'email': '2024@d-mail.com'}]

html = """
{%- macro list_users(users) -%}
{%- for usr in users -%}
    {%- if usr.email[-9:] == 'gmail.com' %}
        <p>{{caller(usr)}}</p>
    {%- endif -%}
{%- endfor -%}
{%- endmacro -%}
{%- call(user) list_users(users) -%}
name: {{ user.name }} email: {{ user.email }}
{%- endcall -%}
"""

tm = Template(html)
msg = tm.render(users=users_l)
print(msg)

# task 2
products = [
    {'name': 'Огурцы', 'price': 17}, {'name': 'Томаты', 'price': 19},
    {'name': 'Лук зеленый', 'price': 8}, {'name': 'Чеснок', 'price': 20},
    {'name': 'Дуриан', 'price': 2000}]

html = """
{%- macro list_users(products) -%}
{%- for product in products|sort(attribute='price') %}
        <p>
        {%- if product.price < 10 -%}
            {{caller(product)}} доступный  
        {%- elif product.price < 20 -%}
            {{caller(product)}} имеет среднюю цену
        {%- else -%}
            {{caller(product)}} имеет высокую цену
        {%- endif -%}
        </p>
{%- endfor -%}
    
{%- endmacro -%}
{%- call(prod) list_users(products) -%}
Продукт: {{ prod.name }}
{%- endcall -%}
"""

tm = Template(html)
msg = tm.render(products=products)
print(msg)
