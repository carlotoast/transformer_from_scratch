from datasets import load_dataset

print("Attempting to connect to the Hugging Face Hub...")
try:
    # Attempt to download a very small part of the dataset
    ds = load_dataset('opus_books', 'en-fr', split='train[:1%]', trust_remote_code=True)
    print("✅ Success! Connection is working.")
except Exception as e:
    print(f"❌ Failed to connect. Error: {e}")