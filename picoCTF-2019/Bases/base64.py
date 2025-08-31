#!/usr/bin/env python3
"""
Base64 Utility Tool
-------------------
This script can:
1. Check if a string is valid Base64
2. Decode Base64 into plain text
3. Encode plain text into Base64

Author: Sumit Das (2025)
"""

import base64
import re


def is_base64(s: str) -> bool:
    """
    Check if a string looks like valid Base64.
    - Only allowed chars: A-Z, a-z, 0-9, +, /, -, _, =
    - Length should be multiple of 4 (after padding).
    - Must decode without error.
    """
    # ✅ Allowed Base64 characters (standard + URL-safe)
    base64_pattern = re.compile(r'^[A-Za-z0-9+/=_-]+$')

    # Step 1: check character set
    if not base64_pattern.match(s):
        return False

    # Step 2: fix missing padding if needed
    padded = s + "=" * ((4 - len(s) % 4) % 4)

    # Step 3: try decoding
    try:
        base64.b64decode(padded, validate=True)
        return True
    except Exception:
        return False


def decode_base64(s: str) -> str:
    """Decode Base64 into a UTF-8 string."""
    padded = s + "=" * ((4 - len(s) % 4) % 4)  # fix padding
    decoded_bytes = base64.b64decode(padded)
    return decoded_bytes.decode("utf-8", errors="ignore")


def encode_base64(s: str) -> str:
    """Encode a UTF-8 string into Base64."""
    encoded_bytes = base64.b64encode(s.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


# ----------------------------
# 🔹 Example Usage
# ----------------------------
if __name__ == "__main__":
    sample = "bDNhcm5fdGgzX3IwcDM1"

    print(f"Checking string: {sample}")
    if is_base64(sample):
        print("✅ This is valid Base64!")
        print("Decoded value:", decode_base64(sample))
    else:
        print("❌ Not valid Base64!")

    # Encode a string
    text = "l3arn_th3_r0p35"
    encoded = encode_base64(text)
    print("\nEncoding demo:")
    print(f"Plain text : {text}")
    print(f"Base64     : {encoded}")
