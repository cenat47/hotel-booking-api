from email.message import EmailMessage
from app.config import settings
from pydantic import EmailStr

def create_booking_confirmation_template(booking: dict, email_to: EmailStr):
        email = EmailMessage()
        email["Subject"] = "✅ Подтверждение бронирования"
        email["From"] = settings.SMTP_USER
        email["To"] = email_to
        
        # Красивый HTML шаблон
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
                <style>
                body {{
                        font-family: 'Arial', sans-serif;
                        line-height: 1.6;
                        color: #333;
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                }}
                .header {{
                        background-color: #4CAF50;
                        color: white;
                        padding: 20px;
                        text-align: center;
                        border-radius: 5px 5px 0 0;
                }}
                .content {{
                        padding: 20px;
                        border: 1px solid #ddd;
                        border-top: none;
                        border-radius: 0 0 5px 5px;
                }}
                .booking-details {{
                        background: #f9f9f9;
                        padding: 15px;
                        border-radius: 5px;
                        margin: 15px 0;
                }}
                .footer {{
                        margin-top: 20px;
                        font-size: 12px;
                        color: #777;
                        text-align: center;
                }}
                .button {{
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #4CAF50;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                        margin-top: 15px;
                }}
                </style>
        </head>
        <body>
                <div class="header">
                <h1>Ваше бронирование подтверждено!</h1>
                </div>
                <div class="content">
                <p>Спасибо за бронирование в нашем отеле. Вот детали вашей поездки:</p>
                
                <div class="booking-details">
                        <h3>🔎 Детали бронирования</h3>
                        <p><strong>Номер:</strong> {booking['room_id']}</p>
                        <p><strong>Дата заезда:</strong> {booking['date_from']}</p>
                        <p><strong>Дата выезда:</strong> {booking['date_to']}</p>
                        <p><strong>Количество дней:</strong> {booking['total_days']}</p>
                        <p><strong>Общая стоимость:</strong> {booking['total_cost']} руб.</p>
                </div>
                
                <p>Если у вас есть вопросы, не стесняйтесь отвечать на это письмо.</p>
                
                <div class="footer">
                        <p>С уважением,<br>Команда отеля</p>
                </div>
                </div>
        </body>
        </html>
        """
        
        email.set_content(html_content, subtype="html")
        return email