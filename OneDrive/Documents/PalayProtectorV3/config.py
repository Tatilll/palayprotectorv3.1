from supabase import create_client, Client

SUPABASE_URL = "https://sgacixkbbbgyblfiudum.supabase.co"
SUPABASE_KEY = "ILAGAY_DITO_ANG_ANON_PUBLIC_KEY_MO"

# ✅ Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Test connection
print("🔍 Checking Supabase connection...")
try:
    users = supabase.table("users").select("*").limit(1).execute()
    print("✅ Connection successful!")
    print(f"🌐 Project URL: {SUPABASE_URL}")
    print(f"🔑 Key starts with: {SUPABASE_KEY[:15]}...")
    print(f"📊 Users table found, {len(users.data)} record(s).")
except Exception as e:
    print("❌ Connection failed:", e)
