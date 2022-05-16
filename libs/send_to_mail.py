import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendMail():
# self, subject, from_addr, to_addr, body_text
    def send_errors(self, mail_sender, pass_sender):
        from_addr = mail_sender
        to_addr = mail_sender
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Error in ACAM'
        msg['From'] = 'SUE-FK@fsfk.local'
        msg['To'] = to_addr
        text = 'text'
        html = """\
        <html>
            <head></head>
            <body>
                <p><br>
                    <h1 align="center">Ошибка в ACAM</h1>
                </p>
            </body>
        </html>
        """

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        server = smtplib.SMTP('10.128.1.251', 25)
        server.ehlo()
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def send_email(self, number, request_type, registration_date, service, component, service_recipient, location, description, mail_sender, pass_sender, mail_group_one, mail_group_two):
        from_addr = mail_sender
        # to_addr = 'ShilkinYuV@fsfk.local, NovikovMiA@fsfk.local'
        to_addr = ''
        if component == 'Материальные ценности' or component == 'Этапы Материальные ценности' or component == 'ЦА Отдел МТО ЦОКР' or component == 'Этапы Предоставление канцелярских товаров':
            to_addr = mail_group_one
        else:
            to_addr = mail_group_two
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'СУЭ ФК Новое обращение'
        msg['From'] = 'SUE-FK@fsfk.local'
        msg['To'] = to_addr

        text = 'text'
        html = """\
        <html>
            <head></head>
            <body>
                <p><br>
                    <h1 align="center">Зарегистрировано новое обращение: <a href="http://sm-sue.fsfk.local/sd/operator/#esearch:full:serviceCall:ACTIVE_OBJECTS_ONLY!%7B%22query%22:%22{}%22%7D">{}</a></h1>
                    <p>Тип запроса: <b>{}</b></p>
                    <p>Дата регистрации: <b>{}</b></p>
                    <p>Услуга: <b>{}</b></p>
                    <p>Компонент: <b>{}</b></p>
                    <p>Получатель услуг: <b>{}</b></p>
                    <p>Расположение получателя услуг: <b>{}<b></p>
                    <p>Описание: {}</p>
                </p>
            </body>
        </html>
        """.format(number, number, request_type, registration_date, service, component, service_recipient, location, description)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        server = smtplib.SMTP('10.128.1.251', 25)
        server.ehlo()
        # server.starttls()
        # server.login(from_addr, '!29Ofebov@')
        server.sendmail(from_addr, to_addr.split(','), msg.as_string())
        server.quit()