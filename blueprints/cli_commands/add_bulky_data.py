from blueprints.database import get_session
from blueprints.database.models import Product,User,StockHistory,Order,User_account,Staff,Admin
from datetime import date 
from flask import Blueprint
import click


add_data_bp = Blueprint("add_data_bp",__name__)

@add_data_bp.cli.command("add_data")
def add_data():
    with get_session() as session:
        try:
            user_accounts = []
            
            # User Account 1
            ua1 = User_account(user_id=1, user_email="mohammed.alami@gmail.com", is_user=True)
            ua1.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua1)
            
            # User Account 2
            ua2 = User_account(user_id=2, user_email="fatima.bennani@gmail.com", is_user=True)
            ua2.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua2)
            
            # User Account 3
            ua3 = User_account(user_id=3, user_email="youssef.amrani@gmail.com", is_user=True)
            ua3.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua3)
            
            # User Account 4
            ua4 = User_account(user_id=4, user_email="khadija.idrissi@gmail.com", is_user=True)
            ua4.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua4)
            
            # User Account 5
            ua5 = User_account(user_id=5, user_email="omar.tazi@gmail.com", is_user=True)
            ua5.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua5)
            
            # User Account 6
            ua6 = User_account(user_id=6, user_email="salma.benjelloun@gmail.com", is_user=True)
            ua6.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua6)
            
            # User Account 7
            ua7 = User_account(user_id=7, user_email="hamza.chakir@gmail.com", is_user=True)
            ua7.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua7)
            
            # User Account 8
            ua8 = User_account(user_id=8, user_email="aicha.squalli@gmail.com", is_user=True)
            ua8.set_password("Gwynnistrash12@@@Ali")
            user_accounts.append(ua8)
            
            session.add_all(user_accounts)
            session.flush()
            
            # ========== ADMIN ACCOUNT ==========
            admin = Admin(admin_id=1, admin_email="admin@store.ma")
            admin.set_password("Gwynnistrash12@@@Ali")
            session.add(admin)
            
            # ========== STAFF ACCOUNTS ==========
            staff1 = Staff(staff_id=1, staff_email="staff1@store.ma", is_staff=True)
            staff1.set_password("Gwynnistrash12@@@Ali")
            
            staff2 = Staff(staff_id=2, staff_email="staff2@store.ma", is_staff=True)
            staff2.set_password("Gwynnistrash12@@@Ali")
            
            session.add_all([staff1, staff2])
            
            # ========== PRODUCTS ==========
            products = [
                # Drinks
                Product(product_id=1, product_name="Coca Cola", product_categorie="drinks", 
                        product_price=8, current_stock_quantity=150, 
                        product_entering_date=date(2024, 11, 1), product_expiration_date=date(2025, 6, 1)),

                Product(product_id=2, product_name="Sidi Ali Water", product_categorie="drinks", 
                        product_price=5, current_stock_quantity=200, 
                        product_entering_date=date(2024, 11, 5), product_expiration_date=date(2026, 11, 5)),

                Product(product_id=3, product_name="Centrale Lait", product_categorie="drinks", 
                        product_price=7, current_stock_quantity=80, 
                        product_entering_date=date(2024, 11, 10), product_expiration_date=date(2024, 11, 25)),

                Product(product_id=4, product_name="Hawai Tropical", product_categorie="drinks", 
                        product_price=6, current_stock_quantity=120, 
                        product_entering_date=date(2024, 11, 8), product_expiration_date=date(2025, 5, 8)),

                # Vegetables
                Product(product_id=5, product_name="Tomatoes", product_categorie="vegetables", 
                        product_price=4, current_stock_quantity=50, 
                        product_entering_date=date(2024, 11, 12), product_expiration_date=date(2024, 11, 19)),

                Product(product_id=6, product_name="Potatoes", product_categorie="vegetables", 
                        product_price=3, current_stock_quantity=100, 
                        product_entering_date=date(2024, 11, 10), product_expiration_date=date(2024, 12, 10)),

                Product(product_id=7, product_name="Onions", product_categorie="vegetables", 
                        product_price=3, current_stock_quantity=75, 
                        product_entering_date=date(2024, 11, 11), product_expiration_date=date(2024, 12, 11)),

                Product(product_id=8, product_name="Carrots", product_categorie="vegetables", 
                        product_price=4, current_stock_quantity=60, 
                        product_entering_date=date(2024, 11, 12), product_expiration_date=date(2024, 11, 26)),

                Product(product_id=9, product_name="Peppers", product_categorie="vegetables", 
                        product_price=5, current_stock_quantity=40, 
                        product_entering_date=date(2024, 11, 12), product_expiration_date=date(2024, 11, 20)),

                # Fruits
                Product(product_id=10, product_name="Oranges", product_categorie="fruits", 
                        product_price=6, current_stock_quantity=90, 
                        product_entering_date=date(2024, 11, 9), product_expiration_date=date(2024, 11, 23)),

                Product(product_id=11, product_name="Apples", product_categorie="fruits", 
                        product_price=7, current_stock_quantity=70, 
                        product_entering_date=date(2024, 11, 8), product_expiration_date=date(2024, 12, 8)),

                Product(product_id=12, product_name="Bananas", product_categorie="fruits", 
                        product_price=8, current_stock_quantity=85, 
                        product_entering_date=date(2024, 11, 11), product_expiration_date=date(2024, 11, 18)),

                Product(product_id=13, product_name="Watermelon", product_categorie="fruits", 
                        product_price=15, current_stock_quantity=30, 
                        product_entering_date=date(2024, 11, 10), product_expiration_date=date(2024, 11, 24)),

                Product(product_id=14, product_name="Dates", product_categorie="fruits", 
                        product_price=25, current_stock_quantity=45, 
                        product_entering_date=date(2024, 11, 1), product_expiration_date=date(2025, 2, 1)),

                # Dairy
                Product(product_id=15, product_name="Jaouda Yogurt", product_categorie="dairy", 
                        product_price=4, current_stock_quantity=100, 
                        product_entering_date=date(2024, 11, 11), product_expiration_date=date(2024, 11, 21)),

                Product(product_id=16, product_name="Cheese Vache qui rit", product_categorie="dairy", 
                        product_price=12, current_stock_quantity=60, 
                        product_entering_date=date(2024, 11, 5), product_expiration_date=date(2025, 1, 5)),

                # Bakery
                Product(product_id=17, product_name="Khobz", product_categorie="bakery", 
                        product_price=1, current_stock_quantity=200, 
                        product_entering_date=date(2024, 11, 12), product_expiration_date=date(2024, 11, 13)),

                Product(product_id=18, product_name="Batbout", product_categorie="bakery", 
                        product_price=2, current_stock_quantity=80, 
                        product_entering_date=date(2024, 11, 12), product_expiration_date=date(2024, 11, 14)),
            ]
            session.add_all(products)
            session.flush()

            # ========== USERS (Profiles) ==========
            users = [
                User(user_id=1, user_fullname="Mohammed Alami", user_region="Casablanca", 
                     user_phone="0612345678", user_sign_up_date=date(2023, 5, 15), 
                     user_sexe="M", user_age=35, user_loyality=True, user_ordering_count=45),

                User(user_id=2, user_fullname="Fatima Zahra Bennani", user_region="Rabat", 
                     user_phone="0623456789", user_sign_up_date=date(2023, 8, 22), 
                     user_sexe="F", user_age=28, user_loyality=True, user_ordering_count=32),

                User(user_id=3, user_fullname="Youssef El Amrani", user_region="Tangier", 
                     user_phone="0634567890", user_sign_up_date=date(2024, 1, 10), 
                     user_sexe="M", user_age=42, user_loyality=False, user_ordering_count=8),

                User(user_id=4, user_fullname="Khadija Idrissi", user_region="Fes", 
                     user_phone="0645678901", user_sign_up_date=date(2023, 3, 5), 
                     user_sexe="F", user_age=31, user_loyality=True, user_ordering_count=58),

                User(user_id=5, user_fullname="Omar Tazi", user_region="Marrakech", 
                     user_phone="0656789012", user_sign_up_date=date(2024, 6, 18), 
                     user_sexe="M", user_age=25, user_loyality=False, user_ordering_count=5),

                User(user_id=6, user_fullname="Salma Benjelloun", user_region="Casablanca", 
                     user_phone="0667890123", user_sign_up_date=date(2023, 11, 30), 
                     user_sexe="F", user_age=38, user_loyality=True, user_ordering_count=41),

                User(user_id=7, user_fullname="Hamza Chakir", user_region="Agadir", 
                     user_phone="0678901234", user_sign_up_date=date(2024, 9, 12), 
                     user_sexe="M", user_age=29, user_loyality=False, user_ordering_count=3),

                User(user_id=8, user_fullname="Aicha Squalli", user_region="Meknes", 
                     user_phone="0689012345", user_sign_up_date=date(2023, 7, 8), 
                     user_sexe="F", user_age=45, user_loyality=True, user_ordering_count=67),
            ]
            session.add_all(users)

            # ========== ORDERS ==========
            orders = [
                Order(order_id=1, user_id=1, product_id=1, order_date=date(2024, 11, 10), 
                      product_quantity=6, order_total_price=48),

                Order(order_id=2, user_id=2, product_id=10, order_date=date(2024, 11, 11), 
                      product_quantity=10, order_total_price=60),

                Order(order_id=3, user_id=4, product_id=5, order_date=date(2024, 11, 11), 
                      product_quantity=15, order_total_price=60),

                Order(order_id=4, user_id=1, product_id=17, order_date=date(2024, 11, 12), 
                      product_quantity=20, order_total_price=20),

                Order(order_id=5, user_id=6, product_id=3, order_date=date(2024, 11, 12), 
                      product_quantity=12, order_total_price=84),

                Order(order_id=6, user_id=3, product_id=11, order_date=date(2024, 11, 12), 
                      product_quantity=8, order_total_price=56),

                Order(order_id=7, user_id=8, product_id=14, order_date=date(2024, 11, 10), 
                      product_quantity=3, order_total_price=75),
            ]
            session.add_all(orders)

            # ========== STOCK HISTORY ==========
            stock_history = [
                StockHistory(stock_history_id=1, product_id=1, quantity_change=150, 
                             quantity_after=150, change_date=date(2024, 11, 1), change_type="initial_stock"),

                StockHistory(stock_history_id=2, product_id=1, quantity_change=-6, 
                             quantity_after=144, change_date=date(2024, 11, 10), change_type="sale"),

                StockHistory(stock_history_id=3, product_id=10, quantity_change=-10, 
                             quantity_after=90, change_date=date(2024, 11, 11), change_type="sale"),

                StockHistory(stock_history_id=4, product_id=5, quantity_change=-15, 
                             quantity_after=50, change_date=date(2024, 11, 11), change_type="sale"),

                StockHistory(stock_history_id=5, product_id=17, quantity_change=200, 
                             quantity_after=200, change_date=date(2024, 11, 12), change_type="restock"),

                StockHistory(stock_history_id=6, product_id=17, quantity_change=-20, 
                             quantity_after=180, change_date=date(2024, 11, 12), change_type="sale"),

                StockHistory(stock_history_id=7, product_id=3, quantity_change=-12, 
                             quantity_after=80, change_date=date(2024, 11, 12), change_type="sale"),
            ]
            session.add_all(stock_history)

            # Commit everything
            session.commit()
            click.echo("✅ All Data Added Successfully!")

        except Exception as e:
            session.rollback()
            click.echo(f"Something Wrong ! {e}")

