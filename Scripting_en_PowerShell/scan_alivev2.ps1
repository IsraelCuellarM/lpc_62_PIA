#Israel Cuéllar Méndez - 2077688
#Escaneo de equipos activos en la subred
#
# Determinando gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Determinando tu gateway"
Write-Host "Tu gateway: $subred"
#
# Determinando rango de subred
#
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring(0,$subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host "Determinando tu rango de subred ..."
echo $rango
#
## Determinando si $rango termian en "."
## En ocasiones el rango de subred no termina en punto, necesimos forzarlo.
#
$punto = $rango.EndsWith('.')
if ($punto -like "False")
{
    $rango = $rango + '.' #agregamos el punto en caso de que no estuviera.
}
#
## Creamos un array con 254 numeros {1 a 254} y se almacena
## en una variable que se llamara $rango_ip
#
$rango_ip = @(1..254)
#
## Generamos bucle foreach para validar hosts activos en nuestra subred
#
Write-Output ""
Write-Host "-- Subred actual: "
Write-Host "Escanenando " -NoNewline; Write-Host $rango -NoNewline; Write-Host "0/24" -ForegroundColor Red
foreach ($r in $rango_ip)
{
    $actual = $rango + $r
    $responde = Test-Connection $actual -Quiet -Count 1
    if ($responde -eq "True")
    {
        Write-Output ""
        Write-Host "Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
        
    }
}
