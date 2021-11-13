# Julio Cesar Bonilla Hernandez, Angel Ivan Celaya Garcia & Jose Fidencio Vanegas Viera
Function mostrarmenu{
    Clear-Host
    Write-Host "Menu de opciones"
    Write-Host "1. Ver estatus de un perfil en el Firewall"
    Write-Host "2. Cambiar el estatus de los perfiles"
    Write-Host "3. Ver el perfil de nuestra red"
    Write-Host "4. Cambiar nuestra red a otro tipo de perfil"
    Write-Host "5. Ver las reglas de bloqueo"
    Write-Host "6. Agregar regla de bloqueo de entrada para un puerto"
    Write-Host "7. Eliminar regla de bloqueo"
    Write-Host "8. Salir"
}
 
mostrarmenu
 
while(($inp = Read-Host -Prompt "Ingresa un numero") -ne "8"){
 
switch($inp){
        1 {
            Clear-Host
            Write-Host "1. Ver estatus de un perfil en el Firewall `n";
            Write-Host "Escriba en perfil: Public ó Private para ver el estatus `n"
            Ver-StatusPerfil
            pause;
            break
        }
        2 {
            Clear-Host
            Write-Host "2. Cambiar el estatus de los perfiles `n";
            Write-Host "Escriba en perfil: Public ó Private para cambiar el estatus `n"
            Cambiar-StatusPerfil
            pause; 
            break
        }
        3 {
            Clear-Host
            Write-Host "3. Ver el perfil de nuestra red `n";
            Ver-PerfilRedActual
            pause;
            break
            }
        4 {
            Clear-Host
            Write-Host "4. Cambiar nuestra red a otro tipo de perfil `n";
            Cambiar-PerfilRedActual
            pause;
            break
        }
        5 {
            Clear-Host
            Write-Host "5. Ver las reglas de bloqueo `n";
            Ver-ReglasBloqueo
            pause; 
            break
        }
        6 {
            Clear-Host
            Write-Host "6. Agregar regla de bloqueo de entrada para un puerto `n";
            Agregar-ReglasBloqueo
            pause;
            break
            }
        7 {
            Clear-Host
            Write-Host "7. Eliminar regla de bloqueo `n";
            Eliminar-ReglasBloqueo
            pause;
            break
            }
        8 {"Salir"; break}
        default {Write-Host "Opcion invalida, ingrese un digito que venga en el menu `n";pause}
        
    }
 mostrarmenu
}

