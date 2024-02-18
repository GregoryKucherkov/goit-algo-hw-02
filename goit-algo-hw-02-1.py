from queue import Queue
import uuid
import random  
import time

queue = Queue()

def generate_request(request_type):
    request = f'Request {uuid.uuid4()} - {request_type}'
    queue.put(request)
    print(f'Request {request} has been generated')
    time.sleep(1)


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'The request {request} has been processed')
        time.sleep(1)
    else:
        print(f'The queue is empty')
        

possible_request_type = ['Warnig', 'Info', 'Critical' ]


def main():
    try:
        while True:
            generate_request(random.choice(possible_request_type))
            process_request() 
    except KeyboardInterrupt:
        print('Exiting the program ')

if __name__ == '__main__':
    main()


'''
# Alternative version with user input

def main():
    while True:
        user_input = input("Press Enter to generate and process a request (type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break

        generate_request(random.choice(possible_request_type))
        process_request() 

if __name__ == '__main__':
    main()
'''

