from connection import connection

def add_products(connection, product_detail):
    cursor = connection.cursor()
    query = """
            insert into products (product_name, unit_id, product_price)
            values (%s, %s, %s)
            """
    unitResponse = display_units(connection)
    for ele in unitResponse:
        if product_detail["unit"] == ele["unit_name"]:
            product_detail["unit"] = ele["unit_id"]
            print(product_detail["unit"])
    print(product_detail)
    cursor.execute(query, (product_detail["product_name"], product_detail["unit"], product_detail["price"]))
    connection.commit()

def display_products(connection):
    cursor = connection.cursor()
    response = []
    query = """
            select p.product_id, p.product_name, u.unit_name, p.product_price
            from products p inner join units u 
            on p.unit_id = u.unit_id
            """
    cursor.execute(query)
    for ele in cursor:
        response += [
            {
                "product_id" : ele[0],
                "product_name" : ele[1],
                "unit_name" : ele[2],
                "product_price" : ele[3]
            } 
        ]
    return response

def display_units(connection):
    cursor = connection.cursor()
    response = []
    query = """
            select * 
            from units
            """
    cursor.execute(query)
    for ele in cursor:
        response += [
            {
                "unit_id" : ele[0],
                "unit_name" : ele[1]
            }
        ]
    # print(response)
    return response

def delete_product(connection, data):
    cursor = connection.cursor()
    query = """
            delete from products
            where product_id = %s
            """
    cursor.execute(query, [data["product_id"]])
    connection.commit()

if __name__ == "__main__":
    connect = connection()
    add_products(connect, {"product_name" : "Vim", "unit" : "piece", "price" : "25"})