#Angel Ivan Celaya Garcia
#Jose Fidencio Vanegas Viera
#Julio Cesar Bonilla Hernandez
import subprocess

c = "Get-Process"
Power_line = "powershell -Executionpolicy ByPass -Command "+ c
Tarea = subprocess.check_output(Power_line)
print(Tarea.decode())
