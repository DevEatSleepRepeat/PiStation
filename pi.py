from numba import njit
from tqdm import tqdm
from decimal import Decimal, getcontext
import time

# === Settings ===
digits = 50  # Desired number of digits
iterations = 100_000_000  # More = more accurate
chunk_size = 1_000_000  # Controls progress bar granularity

# Setup high-precision decimal context
getcontext().prec = digits + 5  # A little buffer for rounding

# === Numba-accelerated chunk calculation ===
@njit
def calculate_pi_chunk(start, end):
    total = 0.0
    for i in range(start, end):
        total += (-1) ** i / (2 * i + 1)
    return total

def calculate_pi_with_progress(total_iterations, chunk_size):
    total_sum = 0.0
    chunks = total_iterations // chunk_size

    for chunk in tqdm(range(chunks), desc="Calculating π"):
        start = chunk * chunk_size
        end = start + chunk_size
        total_sum += calculate_pi_chunk(start, end)

    # Handle leftover iterations
    leftover = total_iterations % chunk_size
    if leftover > 0:
        total_sum += calculate_pi_chunk(total_iterations - leftover, total_iterations)

    return 4 * total_sum

# === Run the calculation ===
start_time = time.time()
raw_pi = calculate_pi_with_progress(iterations, chunk_size)
elapsed = time.time() - start_time

# Convert to Decimal and trim to desired digits
pi_decimal = Decimal(raw_pi)
pi_str = str(+pi_decimal)[:digits + 2]  # +2 to include "3."

# Save to file
filename = f"Pi{digits}.txt"
with open(filename, "w") as f:
    f.write(pi_str)

# Output
print(f"\nApproximated π to {digits} digits: {pi_str}")
print(f"Saved to: {filename}")
print(f"Time taken: {elapsed:.2f} seconds")