from bs4 import BeautifulSoup
import requests
import smtplib, ssl

# Get price of the product

product_url = 'https://www.amazon.com/ZeroWater-Pitcher-Quality-BPA-Free-Certified/dp/B0073PZ6O0?ref' \
              '=dlx_deals_gd_dcl_img_3_097a7ae6_dt_sl15_c9&th=1 '
HEADERS = {
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36 '
}

product_data = requests.get(url=product_url, headers=HEADERS).text
soup = BeautifulSoup(product_data, 'html.parser')
product_price = soup.find('span', class_='a-offscreen')
product_price_float = float(product_price.getText().split('$')[1])
print(product_price_float)


# # sending email alert
# sender_email = '***********@gmail.com'
# receiver_email = '**********@gmail.com'
# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls
# password = input("Type your password and press enter: ")
#
#
# message = f"""From: Timmy {sender_email}
# To: To timmy {receiver_email}
# Subject: Product price Dropped on Amazon
#
# if you want to but the product the price of the product has reduced to {product_price} .
# """
#
# if product_price_float <= 40.0:
#     context = ssl.create_default_context()
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.ehlo()  # Can be omitted
#         server.starttls(context=context)
#         server.ehlo()  # Can be omitted
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)



