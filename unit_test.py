from nicegui import ui, app
from views.user_account_view import UserAccountView
from init_db import engine, create_db_and_tables
from controlers.product_controler import productControler

def init_app():
    async def handle_startup():
        try:
            await create_db_and_tables()
        except:
            pass    

    async def handle_shutdown():
        await engine.dispose()

    app.on_startup(handle_startup)
    app.on_shutdown(handle_shutdown)


@ui.page('/')
async def home_page():
    await productControler.add_product(
        product_number='123',
        product_name='123',
        unit_price=123,
        stock=123,
        spec='123',
        detail='123'
    )

init_app()


ui.run()