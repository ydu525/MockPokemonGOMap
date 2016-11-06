import requests
import time
from multiprocessing import Pool


QUERY_SERVER_URL = "URL"

def create_thousand_request(index):
    start = time.time()

    for i in range(1000):
        response = requests.get(QUERY_SERVER_URL + "?east=-73.979579269886&south=40.74876479398508&north=40.75126408902728&west=-73.98232048749922")

    end = time.time()

    print end - start


if __name__ == '__main__':
    p = Pool(20)
    print(p.map(create_thousand_request, range(20)))
