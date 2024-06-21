import os
from supabase import create_client, Client
from dotenv import load_dotenv


load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def sign_up(email: str, password: str):
    return supabase.auth.sign_up({"email": email, "password": password})
def sign_in(email: str, password: str):
    return supabase.auth.sign_in_with_password({"email": email, "password": password})


if __name__ == "__main__":
    # new_user = sign_up("wiliam.able.kane@gmail.com", "12H1NPw4N3wnDU7!")
    # print("đăng ký thành công")
    user = sign_in("wiliam.able.kane@gmail.com", "v-Z^5?5!CHK$/fd")
    print(user)
    print("đăng nhập thành công")
    print("---")
    # supabase.auth.sign_out()
    # print("đăng xuất thành công")
    