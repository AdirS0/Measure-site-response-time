import time
import requests


def main():
    server_url = input('Enter server URL: ')
    max_response_time = input('Enter maximum acceptable response time: ')
    num_of_checks = 10

    check_server_response_time(server_url, max_response_time, num_of_checks)


def check_server_response_time(url, max_response_time, num_of_checks):
    for i in range(num_of_checks):
        response_time = get_response_time(url)
        ## If there was an error
        if response_time == -1:
            return

        if response_time > max_response_time:
            print(f'Response time of {response_time} seconds exceeds threshold of {max_response_time} seconds')


def get_response_time(url):
    try:
        start = time.time()
        requests.get(url)
        end = time.time()
        return end - start
    except Exception as e:
        print(f'Error occurred: {e}')
        return -1


if __name__ == '__main__':
    main()
