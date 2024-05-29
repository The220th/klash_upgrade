# -*- coding: utf-8 -*-

import time
import random
import numpy as np
from colorama import Fore, Back, Style, init
from tqdm import tqdm


def generate_message():
    controller_id = f"{random.randint(1000, 9999):04X}"
    producer_id = random.randint(0, 255)
    address = f"{random.randint(0, 0xFFFF):04X}"
    status = random.randint(-5, 9)

    messages = [
        (f"\nController {controller_id} is not functional, producer {producer_id} out of range 65535", Fore.RED + Back.BLACK),
        ("\nTimeout waiting for FW", Fore.YELLOW + Back.BLUE),
        (f"\nNVM write to address {address} failed with status={status}", Fore.BLUE + Back.YELLOW)
    ]

    weights = [0.5, 0.2, 0.3]

    message, color = random.choices(messages, weights=weights, k=1)[0]
    return message, color


def flashing_process():
    # num_messages=20
    # for _ in range(num_messages):
    for _ in tqdm(range(random.randint(500, 5000))):
        if random.randint(1, 100) <= 3:
            wait_time = np.random.normal(loc=2.5, scale=1.0)  # Среднее 2.5 сек, стандартное отклонение 1 сек
            wait_time = max(0.1, min(7, wait_time))  # Ограничиваем интервал от 0.1 до 5 секунд
            time.sleep(wait_time)

            message, color = generate_message()
            print(color + message)

        time.sleep(random.randint(10, 500)/1000)
