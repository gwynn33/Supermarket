from flask import Blueprint
from blueprints.database.create_tables import recreate_tables
import click
import traceback

recreate_bp = Blueprint('recreate_bp',__name__)

@recreate_bp.cli.command("recreate-all")
def recreate_all():
    try:
        recreate_tables()
    except Exception as e:
        click.echo(f"-------Error--------")
        click.echo(str(e))
        click.echo(f"==================Detailed Error================")
        traceback.print_exc()