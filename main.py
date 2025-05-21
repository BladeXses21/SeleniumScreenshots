import undetected_chromedriver as uc
import time
import os

import pandas as pd

options = uc.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)

screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

file_path = "screenshot-urls-only.csv"
df = pd.read_csv(file_path, header=None)
urls = df.iloc[1:11, 1].dropna().tolist()


for url in urls:
    try:
        driver.get(url)
        time.sleep(3)

        domain = url.split("//")[-1].split("/")[0]
        screenshot_path = os.path.join(screenshot_dir, f"{domain}.png")

        driver.save_screenshot(screenshot_path)
        print(f"Скриншот збережено: {screenshot_path}")
    except Exception as e:
        print(f"Помилка при обробці {url}: {e}")

driver.quit()
