import pandas as pd

data = {
    'description': [
        "Stylish black leather wallet with multiple card slots and a coin pocket.",
        "Wireless Bluetooth headphones with noise-canceling feature.",
        "Durable stainless steel water bottle with a vacuum seal.",
        "Soft and comfortable cotton T-shirt in various colors.",
        "High-performance laptop with a fast processor and large storage capacity.",
        "Classic wooden chess set for strategy enthusiasts.",
        "Elegant silver necklace with a heart-shaped pendant.",
        "Portable and rechargeable electric toothbrush for dental care.",
        "Deluxe leather office chair with ergonomic design.",
        "Compact digital camera with zoom and image stabilization."
    ]
}

df = pd.DataFrame(data)
df.to_csv('product_descriptions.csv', index=False)
