# დაწერე ფუნქცია რომელიც არგუმენტად მიიღებს ვებგვერდის მისამართს და გააგზავნის GET request_ს ყოველ 10 წამში და დაბეჭდოს ვებგვერდის სახელი და პასუხად მიღებული სტატუსის კოდი. გამოიყენე time მოდულის sleep ფუნქცია.
#
# Threading_ის გამოყენებით ერთდროულად გაუშვი ზემოხსენებული ფუნქცია სამი განსხვავებული ვებგვერდის შესამოწმებლად.

import threading  # მოდული threading-ის იმპორტირება
import requests  # მოდული requests-ის იმპორტირება
import time  # მოდული time-ის იმპორტირება

def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"ვებგვერდი: {url}, სტატუსის კოდი: {response.status_code}")
    except Exception as e:
        print(f"შეცდომა: {e}")

def monitor_websites(urls):
    while True:
        for url in urls:
            threading.Thread(target=fetch_url, args=(url,)).start()
        time.sleep(10)

urls = ["https://av.com", "https://ipn.ge", "https://google.com"]
monitor_websites(urls) # ვებსაიტების მონიტორინი
