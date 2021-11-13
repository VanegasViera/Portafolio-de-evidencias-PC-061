function Cambiar-StatusPerfil{ 
	param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil) 
	$status = Get-NetFirewallProfile -Name $perfil -ErrorAction "Stop"
	Write-Host "Perfil:" $perfil 
	if($status.enabled){ 
		Write-Host "Status actual: Activado" 
		$opc = Read-Host -Promt "Deseas desactivarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){ 
			Set-NetFirewallProfile -Name $perfil -Enabled False 
		} 
	} else{ 
		Write-Host "Status: Desactivado" 
		$opc = Read-Host -Promt "Deseas activarlo? [Y] Si [N] No" 
		if ($opc -eq "Y"){ 
			Write-Host "Activando perfil" 
			Set-NetFirewallProfile -Name $perfil -Enabled True 
		} 
	} 
	Ver-StatusPerfil -perfil $perfil 
}

function show-Service{
    #[cmdletBinding()] Param([Parameter()][String]$perfil)
    Param([Parameter(Mandatory)][String]$perfil)
    $status = Get-Service -Name $perfil -ErrorAction "Stop"
    
    $status
}

function show-parimpar{
    [cmdletBinding()] Param([Parameter()][Int]$num)
    if($num % 2 -eq 0){
        Write-Host "El numero $num es par"
    }
    else{
        Write-Host "El numero $num es impar"
    }
}

Export-ModuleMember -Function  Cambiar-StatusPerfil show-Service show-parimpar