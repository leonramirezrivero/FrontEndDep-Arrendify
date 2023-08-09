function sumar()
{
var total = 0;
var total2 = 0;
var total3 = 0;
var valor1 = document.getElementById("val1").value;
if (valor1<10000)
{
    total = 2800;
    var reg = /\d{1,3}(?=(\d{3})+$)/g;



    var Display = document.getElementById("Display");
    var Display2 = document.getElementById("Display2");
    var Display3 = document.getElementById("Display3");
    Display.innerHTML =  (total + '').replace(reg,'$&,');
    Display2.innerHTML = (3500 + '').replace(reg,'$&,');
    Display3.innerHTML = (7000 + '').replace(reg,'$&,');
    if (!valor1)
    {
        console.log('esta vacio')
        Display.innerHTML = 0;
        Display2.innerHTML = 0;
        Display3.innerHTML = 0;

    } 
}
else
{
  
    total = (valor1 * 0.28);
    total2 = (valor1 * 0.35);
    total3 = (valor1 * 0.70);
    var dec = total.toFixed()
    var dec2 = total2.toFixed()
    var dec3 = total3.toFixed()
    var reg = /\d{1,3}(?=(\d{3})+$)/g;

    var Display = document.getElementById("Display");
    var Display2 = document.getElementById("Display2");
    var Display3 = document.getElementById("Display3");
    Display.innerHTML =  (dec + '').replace(reg,'$&,');
    Display2.innerHTML = (dec2 + '').replace(reg,'$&,');
    Display3.innerHTML = (dec3 + '').replace(reg,'$&,');
    
    
}
}

                                     
