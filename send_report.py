import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

# Função para gerar o relatório (exemplo simples)
def generate_report():
    # Gerando um relatório de exemplo (um arquivo CSV)
    report_content = "Nome,Email,Total de Vendas\nJohn Doe,johndoe@email.com,1000\nJane Doe,janedoe@email.com,1500\n"
    report_file = "relatorio.csv"
    
    with open(report_file, "w") as file:
        file.write(report_content)
    
    print(f"Relatório '{report_file}' gerado com sucesso.")
    return report_file

# Função para enviar o relatório por e-mail
def send_report_email(to_email, report_file):
    from_email = "seuemail@gmail.com"
    from_password = "suasenha"
    subject = "Relatório Diário"

    # Configurar o e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Corpo do e-mail
    body = "Por favor, veja o relatório diário em anexo."
    msg.attach(MIMEText(body, 'plain'))

    # Anexar o arquivo
    attachment = open(report_file, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + os.path.basename(report_file))
    msg.attach(part)

    # Configurar o servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)

    # Enviar o e-mail
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

    print(f"Relatório enviado para {to_email}.")

# Função para gerar e enviar o relatório
def generate_and_send_report():
    report_file = generate_report()
    recipients = ["destinatario1@email.com", "destinatario2@email.com"]  # Adicione os destinatários
    for recipient in recipients:
        send_report_email(recipient, report_file)

# Agendar o envio do relatório diariamente às 9:00
schedule.every().day.at("09:00").do(generate_and_send_report)

print("Sistema de automação de relatórios iniciado. Enviando relatórios diariamente às 9:00.")

# Loop para verificar o agendamento
while True:
    schedule.run_pending()
    time.sleep(60)  # Checa a cada minuto se há tarefas pendentes
