import tqdm
import time
from decimal import Decimal, getcontext

for chunk in tqdm(range(0,10), desc="Working"):
    time.sleep(0.1)