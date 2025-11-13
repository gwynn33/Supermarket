import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from flask import Blueprint,request,render_template,jsonify
from flask_login import login_required,current_user
from sqlalchemy import select
from blueprints.fn.functions import parsed_gmail
from blueprints.database.models import Staff,Product,Order,StockHistory
from blueprints.database import get_session
import traceback

staff_bp = Blueprint("staff_bp",__name__)

def generate_chart_data():
    with get_session() as session:
        products = session.query(Product).all()

        df = pd.DataFrame([{
            'product_id' : p.product_id,
            'product_name' : p.product_name,
            'product_categorie' : p.product_categorie,
            'product_price' : p.product_price,
            'current_stock_quantity': p.current_stock_quantity
        } for p in products])

        products_by_price = df.sort_values('product_price',ascending=False)
        products_by_stock = df.sort_values('current_stock_quantity',ascending=False)

        df['total_value'] = df['product_price'] * df['current_stock_quantity']
        total_stock_value = float(df['total_value'].sum())

        category_stock = df.groupby('product_categorie')['current_stock_quantity'].sum()

        return {
            'products_by_price': products_by_price.to_dict('records'),
            'products_by_stock': products_by_stock.to_dict('records'),
            'total_stock_value': total_stock_value,
            'products_with_value': df.to_dict('records'),
            'category_data': {
                'categories': category_stock.index.tolist(),
                'quantities': category_stock.values.tolist()
            }
        }


@staff_bp.route('/staff_page',methods = ['GET','POST'])
@login_required
def staff():
    if request.method == 'GET':
        user = int(current_user.get_id())
        with get_session() as session:
            query = select(Staff).where(Staff.staff_id == user)
            statement = session.execute(query).scalars().first()
            username =  statement.staff_email
        username = parsed_gmail(username)
        data = generate_chart_data()
        return render_template(
            'staff_bp.html',
            username=username,
            products_by_price=data['products_by_price'],
            products_by_stock=data['products_by_stock'],
            total_stock_value=data['total_stock_value'],
            products_with_value=data['products_with_value']
        )

@staff_bp.route('/api/chart-data', methods=['GET'])
def get_chart_data():
    """API endpoint pour récupérer les données du graphique"""
    data = generate_chart_data()
    return jsonify(data['category_data'])

# OPTIONNEL: Si tu veux vraiment générer des images matplotlib
@staff_bp.route('/api/matplotlib-chart', methods=['GET'])
def generate_matplotlib_chart():
    """Génère un graphique matplotlib et le retourne en base64"""
    data = generate_chart_data()
    category_data = data['category_data']
    
    # Créer le graphique avec matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(category_data['categories'], category_data['quantities'], color='steelblue')
    ax.set_xlabel('Category')
    ax.set_ylabel('Stock Quantity')
    ax.set_title('Stock by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Convertir en base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    plt.close()
    
    return jsonify({
        'image': f'data:image/png;base64,{image_base64}',
        'data': category_data
    })
        