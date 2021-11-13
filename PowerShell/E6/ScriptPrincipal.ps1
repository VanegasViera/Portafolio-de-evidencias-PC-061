# Julio Cesar Bonilla Hernandez, Angel Ivan Celaya Garcia & Jose Fidencio Vanegas Viera
Import-Module ModuloE6
Function mostrarmenu{
    Clear-Host
    Write-Host "Menu de opciones"
    Write-Host "1. Cambiar el estatus de los perfiles"
    Write-Host "2. ver los Status de los servicios"
    Write-Host "3. Escribir un numero y saber si es par o impa"
    Write-Host "4. Salir"
}
 
mostrarmenu
 
while(($inp = Read-Host -Prompt "Ingresa un numero") -ne "4"){
 
switch($inp){
        1 {
            try{
                Clear-Host
                Write-Host "1. Cambiar el estatus de los perfiles `n";
                Write-Host "Escriba en perfil: Public ó Private para ver el estatus `n"
                Cambiar-StatusPerfil
            }
            catch{
                Write-Host "|ERROR|:valor no valido"
            }
            pause;
            break
        }
        2 {
            try{
                Clear-Host
                Write-Host "2. ver los Status de los servicios `n";
                $perfil = Read-Host "Escribe el nombre de un servicio"
                show-qwe($perfil)
            }
            catch{
                Write-Host "|ERROR|-No escribio un servio valido"
            }
            pause;
            break
        }
        3 {
           try{
                Clear-Host
                Write-Host "3. Escribir un numero y saber si es par o impar `n";
                $num = Read-Host "Escribe un numero" 
                show-parimpar($num)
            }
            catch{
            Write-Host "|ERROR|-No selecciono un numero"
            }
            pause;
            break
            }
        
        4 {"Salir"; break}
        default {Write-Host "Opcion invalida, ingrese un digito que venga en el menu `n";pause}
        
    }
 mostrarmenu
}

