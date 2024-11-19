from models.product_model import Product
from init_db import get_async_session_context
from sqlalchemy.future import select
from typing import List

class productControler:

    @staticmethod
    async def add_product(product_number: str, product_name: str, unit_price: str, stock: int, spec: str, detail: str) -> None:
        async with get_async_session_context() as session:        
            product = Product(
                product_number = product_number,
                product_name = product_name,
                unit_price = unit_price,
                stock = stock,
                spec = spec,
                detail = detail
            )
            session.add(product)
            await session.commit()
            return product
        
    @staticmethod
    async def delete_product(id: int = None, product_number: str = None, product_name: str = None) -> None:
        async with get_async_session_context() as session:
            result = await session.execute(
                select(Product).where((Product.id == id) | (Product.product_number == product_number) | (Product.product_name == product_name))
            )
            user_account = result.scalars().first()
            await session.delete(user_account)
            await session.commit()

    @staticmethod
    async def update_product(id: int, account: str = None, email: str = None, password: str = None, address: str = None) -> None:
        async with get_async_session_context() as session:
            user_account = await session.get(Product, id)
            if account is not None:
                user_account.account = account
            if email is not None:
                user_account.email = email
            if password is not None:
                user_account.password = password
            if address is not None:
                user_account.address = address                                          
            await session.commit()                              

    @staticmethod
    async def select_all() -> List[Product]:
        async with get_async_session_context() as session:
            result = await session.execute(select(Product))
            product = result.scalars().all()
            return product

    @staticmethod
    async def select_product(id: int = None, product_number: str = None, product_name: str = None) -> List[Product]:
        async with get_async_session_context() as session:
            result = await session.execute(
                select(Product).where((Product.id == id) | (Product.product_number == product_number) | (Product.product_name == product_name))
            )
            product = result.scalars().first()
            return product                  