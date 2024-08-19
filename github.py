import requests

def get_github_user_info(username):
    print("Gathering Information Please Wait!!")
    
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(response.json().get("message", "Error fetching data"))
        return
    
    user_info = response.json()
    
    name = user_info.get("name")
    user_id = user_info.get("id")
    bio = user_info.get("bio")
    html_url = user_info.get("html_url")
    avatar_url = user_info.get("avatar_url")
    email = user_info.get("email")
    location = user_info.get("location")
    company = user_info.get("company")
    repos = user_info.get("public_repos")
    gists = user_info.get("public_gists")
    followers = user_info.get("followers")
    following = user_info.get("following")

    txt = (
        f"✅ Found From [GitHub](http://www.github.com/)\n\n"
        f"▪️ Name : {name}\n"
        f"▪️ Id : {user_id}\n"
        f"▪️ Bio : {bio}\n"
        f"▪️ Type : {user_info.get('type')}\n"
        f"▪️ Email : {email}\n"
        f"▪️ Location: {location}\n"
        f"▪️ Company : {company}\n"
        f"▪️ Total Repos : {repos}\n"
        f"▪️ Total Gists : {gists}\n"
        f"▪️ Followers : {followers}\n"
        f"▪️ Following : {following}"
    )

    if avatar_url and avatar_url.startswith("https://"):
        send_photo(avatar_url, txt, html_url)
    else:
        send_message(txt, html_url)

def send_photo(photo_url, caption, url):
    print(f"Sending photo: {photo_url}\nCaption: {caption}\nLink: {url}")

def send_message(text, url):
    print(f"Sending message: {text}\nLink: {url}")

# User input for GitHub username
username = input("Enter GitHub username : ")
get_github_user_info(username)