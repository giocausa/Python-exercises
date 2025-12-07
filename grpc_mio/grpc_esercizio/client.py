import grpc
import order_management_pb2
import order_management_pb2_grpc

import multiprocess as mp 
import logging,time,sys

def generate_orders_for_processing():
    print('generate order...')

    ord1 = order_management_pb2.Order(
        id='104', price=2332,
        items=['Item - A', 'Item - B'],  
        description='Updated desc', 
        destination='San Jose, CA')
    
    ord2 = order_management_pb2.Order(
        id='105', price=3000, 
        description='Updated desc', 
        destination='San Francisco, CA')
    
    ord3 = order_management_pb2.Order(
        id='106', price=2560, 
        description='Updated desc', 
        destination='San Francisco, CA')
    
    ord4 = order_management_pb2.Order(
        id='107', price=2560, 
        description='Updated desc', 
        destination='Mountain View, CA')    

    list = []
    list.append(ord1)
    list.append(ord2)
    list.append(ord3)
    list.append(ord4)
    for processing_orders in list:
        yield processing_orders

def run(port):
    channel = grpc.insecure_channel('localhost'+str(port))

    stub = order_management_pb2_grpc.OrderManagementStub(channel)

    orders = []

    orders.append(order_management_pb2.Order(
        price=2400.50,
        items=['Item-A','Item-B','Item_C'],
        description='questo è un ordine di merda',
        destination='casa di thatotor,NA'
    ))
    orders.append(order_management_pb2.Order(
        price=1200.50,
        items=['Item-A','Item-B','Item_C','Item-D'],
        description='questo è un ordine semplice',
        destination='Civitavecchia,RM'
    ))
    orders.append(order_management_pb2.Order(
        price=240.50,
        items=['Item-A'],
        description='questo è un ordine pidocchioso',
        destination='Monte di Procida,NA'
    ))
    orders.append(order_management_pb2.Order(
        price=6000.00,
        items=['Item-A','Item-B','Item_C','Item-D','Item-E'],
        description='questo è un ordine lungo come quello di rocco',
        destination='Tarquinia,VT'
    ))
    orders.append(order_management_pb2.Order(
        price=1400.50,
        items=['Item-A','Item-B','Item_C'],
        description='questo è un ordine ',
        destination='Fregene,RM'
    ))

    print('###########')

    for order in orders:
        response = stub.addOrder(order)
        print('AddOrder invoked: '+response)

        order =stub.getOrder(response)
        print('getOrder invoked, Order: '+order)

    
    print('########')
    order_search_result = stub.searchOrder(order_management_pb2.StringMessage(value='Item-A'))
    print('Search order invoked, result: ')
    for order in order_search_result:
        print(order)

    print('#########')
    proc_order_iterator =generate_orders_for_processing()

    shipments =stub.processOrder(proc_order_iterator)
    print('ProcessOrder invoked. Result: ')
    for shipment in shipments:
        print('shipment: ',shipment)

if __name__ == '__main__':
    try:
        port = sys.argv[1]
    except IndexError:
        print('errore nell inserimento del port')
        sys.exit(-1)
    
    logging.basicConfig()
    run(port)

