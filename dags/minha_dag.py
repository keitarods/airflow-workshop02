from airflow import DAG
from datetime import  datetime, timedelta
from airflow.operators.bash import BashOperator

#Configuração dos argumentos padrão que serão aplicados a todas as tarefas das DAG.
default_args = {
    "owner":"keitaro", #Define o proprietário da DAG, útil para fins de rastramento e permissão;
    "start_date":"2023-11-02", #Data de inicio da execução da DAG. As execuções serão agendados a partir dessa data;
    "retries": 1, #Número de tentativas de reexecução de uma tarefa em caso de falha;
    "retry_delay": timedelta(minutes=1) #Intervalo de tempo entre as tentativas de reexecução;
}

#Definição da DAG, seu ID, descrição, intervalo de agendamento, argumentos padrão e politica de recuperação;
with DAG(
    dag_id="newdag", #Identificador único para DAG
    description="My first DAG", #Descrição textual da DAG.
    schedule_interval="0 0 * * *", #Intervalo de agendamento (Aqui, diariamente à meia-noite)
    default_args=default_args, #Aplicação dos argumentos padrão declarados acima.
    catchup=False #Determina se o AIRFLOW realiza ou não a execução de datas passadas que foram perdidas (catchup)  

) as dag:
    #definição de uma tarefa usando BashOperator
    task1 = BashOperator(
        task_id="task1", #Identificador único da tarefa dentro da DAGç
        bash_command='echo "Hello World"', #Comando que a tarefa vai executar.
    )

    #Neste ponto, você pode definir mais tarefas e suas dependências.
    #Por exemplo: task2 = BashOperator(...) seguido de task1 >>> task2 para definir a ordem de execução.

#A DAG é automaticamente atribuida a variavel 'dag' devido ao uso do 'with DAG(...) as dag'