Sistema de Automação para Envio de Relatórios (Python)
Descrição do Projeto:
Este projeto é um sistema automatizado desenvolvido em Python que gera relatórios diários e os envia por e-mail para uma lista de destinatários. O sistema foi projetado para ser agendado e rodar em intervalos específicos usando a biblioteca schedule. Ele também utiliza o módulo smtplib para o envio de e-mails, anexando os relatórios gerados automaticamente.
Principais Funcionalidades:
•	Geração Automática de Relatórios: O sistema gera relatórios no formato CSV. Esses relatórios podem ser modificados para incluir dados reais extraídos de fontes como APIs ou bancos de dados.
•	Envio de E-mails Automatizado: Utilizando o protocolo SMTP, o sistema envia os relatórios para uma lista de destinatários via e-mail, anexando o arquivo gerado.
•	Agendamento Diário: Com a biblioteca schedule, o envio dos relatórios é agendado para ocorrer todos os dias em um horário específico (por exemplo, às 9h da manhã).
Ferramentas e Tecnologias:
•	Python (smtplib): Usado para configurar e enviar e-mails via protocolo SMTP. No projeto, integrei o servidor SMTP do Gmail para enviar os relatórios.
•	Python (schedule): Biblioteca responsável pelo agendamento das tarefas diárias. O código fica em execução contínua e verifica periodicamente se há uma tarefa agendada a ser executada.
•	Automação com Looping: Um loop infinito é utilizado para garantir que o sistema verifique a cada minuto se há um envio de relatório programado, sem necessidade de intervenção manual.
•	CSV: Os relatórios são gerados no formato CSV, o que facilita a manipulação de dados estruturados. A função generate_report() cria esse arquivo automaticamente com base em informações de exemplo, mas pode ser adaptada para gerar relatórios com dados reais de um banco de dados ou outra fonte.
Como Funciona o Código:
1.	Gerar Relatório: A função generate_report() cria um arquivo CSV simples com dados fictícios de exemplo. Esse arquivo pode ser adaptado para incluir dados reais.
2.	Envio de E-mail: A função send_report_email() utiliza o servidor SMTP do Gmail para enviar o relatório gerado. Ela configura o e-mail com o anexo (relatório) e o envia para os destinatários definidos.
3.	Agendamento: A biblioteca schedule permite que o envio do relatório seja automatizado para ocorrer diariamente às 9h da manhã. Esse agendamento pode ser modificado para qualquer outro horário ou frequência.
4.	Execução Contínua: Um loop infinito (while True) mantém o script rodando e verificando a cada minuto se há alguma tarefa pendente de execução.
Desafios Resolvidos:
•	Automatização Completa: O sistema não requer intervenção manual após configurado, sendo capaz de gerar e enviar relatórios automaticamente em intervalos regulares.
•	Segurança no Envio de E-mails: O envio dos e-mails é configurado para rodar via servidores seguros como o Gmail, mas pode ser facilmente adaptado para outros serviços.
