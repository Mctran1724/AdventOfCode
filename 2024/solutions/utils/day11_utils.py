import math
from typing import List
from tqdm import tqdm
import multiprocessing
import itertools
import numpy as np

def even_digits(x: int) -> bool:
    # Returns true if the number has an even number of digits
    if x < 0:
        x *= -1
    return math.floor(math.log10(x)) % 2 != 0

def split_number(x: int) -> List[int]:
    # Splits the number into two equal parts in constant time
    negative_factor = 1
    if x < 0:
        x *= -1
        negative_factor = -1
    num_digits = math.floor(math.log10(x)) + 1
    if num_digits % 2 == 1:
        raise ValueError("Number must have an even number of digits")
    
    power_of_10 = 10 ** (num_digits // 2)

    return [x // power_of_10 * negative_factor, x % power_of_10]

def rules(x: int) -> List[int]:
    if x == 0:
        return [1]
    elif even_digits(x):
        return split_number(x)
    else:
        return [x*2024]

def part2(data: List[int], n_blinks = 75) -> int:
    
    def blink_multiprocessing(lst: List[int]) -> List[int]:
        with multiprocessing.Pool() as pool:
            results = pool.map(rules, lst)
        return list(itertools.chain.from_iterable(results)) 
       
    for _ in tqdm(range(n_blinks)):
        data = blink_multiprocessing(data)
        
    return len(data)


##############################

#Vectorized code functions

def even_digits_np(x: np.ndarray) -> np.ndarray:
    """Vectorized version of even_digits."""
    return (np.floor(np.log10(np.abs(x))) + 1).astype(int) % 2 == 0

def split_number_np(x: np.ndarray) -> np.ndarray:    
    """Vectorized version of split_number."""
    negative_factor = np.where(x < 0, -1, 1)
    num_digits = np.floor(np.log10(np.abs(x))) + 1
    power_of_10 = 10 ** (num_digits // 2)
    return (x // power_of_10 * negative_factor, x % power_of_10)    