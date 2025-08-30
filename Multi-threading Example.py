# Parallel processing with threading for web requests
import threading
import requests
import time
from queue import Queue

class ThreadedWebChecker:
    def __init__(self, urls, max_threads=5):
        self.urls = urls
        self.max_threads = max_threads
        self.queue = Queue()
        self.results = []
    
    def check_url(self, url):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=5)
            elapsed = time.time() - start_time
            return {
                'url': url,
                'status': response.status_code,
                'response_time': round(elapsed, 2),
                'success': response.status_code == 200
            }
        except Exception as e:
            return {
                'url': url,
                'status': 'Error',
                'response_time': 0,
                'success': False,
                'error': str(e)
            }
    
    def worker(self):
        while not self.queue.empty():
            url = self.queue.get()
            result = self.check_url(url)
            self.results.append(result)
            self.queue.task_done()
    
    def run_checks(self):
        # Fill the queue
        for url in self.urls:
            self.queue.put(url)
        
        # Create and start threads
        threads = []
        for _ in range(min(self.max_threads, len(self.urls))):
            thread = threading.Thread(target=self.worker)
            thread.start()
            threads.append(thread)
        
        # Wait for all threads to complete
        self.queue.join()
        
        return self.results

# Usage
urls_to_check = [
    'https://google.com',
    'https://github.com',
    'https://stackoverflow.com',
    'https://python.org',
    'https://nonexistentwebsite12345.com'
]

checker = ThreadedWebChecker(urls_to_check)
results = checker.run_checks()

for result in results:
    status = "✓" if result['success'] else "✗"
    print(f"{status} {result['url']} - {result['status']} ({result['response_time']}s)")
