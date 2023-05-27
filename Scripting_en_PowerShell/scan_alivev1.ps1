#Israel Cuéllar Méndez - 2077688
#Escaneo de equipos activos en la subred
#
# Determinando gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host 'Tu gateway es : ' $subred
#
# Determinando rango de subred
#
$rango = $subred.Substring(0,$subred.Indexof('.')+ 1 + $subred.Substring($subred.Indexof('.')+1).Indexof('.')+3)
Write-Host $rango
#
## Determinando si $rango termian en "."
## En ocasiones el rango de subred no termina en punto, necesimos forzarlo.
#
$punto = $rango.EndsWith('.')
if ($punto -like 'False') 
{
    $rango = $rango+'.' #agregamos el punto en caso de que no estuviera. 
}
#
## Creamos un array con 254 numeros {1 a 254} y se almacena
## en una variable que se llamara $rango_ip
#
$rango_ip = @(1..254)
#
## Generamos bucle foreach para validar hosts activos en nuestra subred
#
foreach ($r in $rango_ip)
{
    $actual = $rango + $r # Se genera direccion ip
    $responde = Test-Connection $actual -Quiet -Count 1 # Validamos conexion contra ip en $actual
    if ($responde -eq "True") {
        Write-Output''
        Write-Host 'host responde: ' -NoNewline; Write-Host $actual -ForegroundColor Green
    }


}