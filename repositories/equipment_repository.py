from db.run_sql import run_sql

from models.producer import Producer
from models.equipment import Equipment

import repositories.producer_repository as producer_repository

def save(equipment):
    sql = "INSERT INTO equipment (name, producer, stock, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s)"
    values = [equipment.name, equipment.producer.id, equipment.stock, equipment.buy_price, equipment.sell_price]
    results = run_sql(sql, values)
    equipment.id = results[0]['id']
    return equipment

def select_all():
    equipment = []
    sql = "SELECT * FROM equipment"
    results = run_sql(sql)

    for row in results:
        producer = producer_repository.select[row['producer_id']]
        equipment1 = Equipment(row['name'], producer, row['stock'], row['buy_price'], row['sell_price'])
        equipment.append(equipment1)
    return equipment

def select(id):
    equipment = None
    sql = "SELECT * FROM equipment WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        equipment = Equipment(result['name'], result['producer_id'], result[''])