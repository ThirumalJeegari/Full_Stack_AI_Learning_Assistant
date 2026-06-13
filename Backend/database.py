SUPABASE_URL="https://dveebeycgvphrzgifkps.supabase.co"
SUPABASE_KEY="sb_publishable_qU-fjsNwWVJGtFt_3TJ7ZA_chZNBI2f"
from supabase import create_client

supa_base = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)