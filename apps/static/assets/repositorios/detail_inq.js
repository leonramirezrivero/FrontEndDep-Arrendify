const server = "https://arrendify-api.onrender.com";
    document.getElementById("cargar_tabla").onload = plantar()
    
    
function plantar()
{   
    
    var datos = JSON.parse( localStorage.getItem('data_inquilino'))
    if(datos.p_fom == "Persona Fisica"){
        console.log("persona f")
        document.getElementById("nav-ac1").style.display = 'none';
        
    }
    
    if(datos.p_fom == "Persona Moral"){
        console.log("persona m")
       document.getElementById("nav-empleo1").style.display = 'none';
       document.getElementById("nav-jefe1").style.display = 'none';
        
    }
    
    if(datos.rentado_antes == "No"){
        console.log("no rente antes")
       document.getElementById("nav-aa").style.display = 'none';
        
    }
    console.log(localStorage)
    console.log("soy datos",datos)
    console.log(datos.id)
    console.log("datos Credito",datos.credito)
    var full = document.getElementById("nombre_full")
    var conyu = document.getElementById("n_conyuge")
    var k1 = Object.getOwnPropertyNames(datos);

    console.log("soy k1",k1)

    // datos generales
    full.textContent = `${datos.nombre} ${datos.apellido} ${datos.apellido1}`
    conyu.value = `${datos.n_conyuge} ${datos.a_conyuge} ${datos.a1_conyuge}`
    document.getElementById("numeroTel").value = datos.numeroTel
    document.getElementById("numeroTel1").value = datos.numeroTel1
    document.getElementById("rfc").value = datos.rfc
    document.getElementById("nacionalidad").value = datos.nacionalidad
    document.getElementById("email").value = datos.email
    document.getElementById("estado_civil").value = datos.estado_civil
   
    if (conyu.value == "null null null"){
        conyu.value = "Sin Conyugue";
            }

    // datos Domiciliarios
    document.getElementById("full_dom").value = `${ datos.calle } ${ datos.num_ext } Int. ${ datos.num_int } Col. ${ datos.colonia } ${ datos.codigopostal } ${ datos.municipio_alcaldia }  ${datos.estado }` 
    document.getElementById("referencia").value = datos.referencias
    
    // datos Domiciliarios
    document.getElementById("full_dom_em").value =`${ datos.calle_empleo } ${ datos.num_ext_empleo } Int. ${ datos.num_int_empleo } Col. ${ datos.colonia_empleo } ${ datos.codigo_postal_empleo }, ${datos.ciudad_empleo }`  
    document.getElementById("full_dom_arrendador").value =`${ datos.calle_dia } ${ datos.num_ext_dia } Int. ${ datos.num_int_dia } Col. ${ datos.colonia_dia } ${ datos.codigo_postal_dia }, ${datos.ciudad_dia }`  
    // referencias
    document.getElementById("ref1").value =`Nombre: ${datos.n_ref1} Parentesco: ${datos.p_ref1} Telefono: ${datos.tel_ref1}`
    document.getElementById("ref2").value =`Nombre: ${datos.n_ref2} Parentesco: ${datos.p_ref2} Telefono: ${datos.tel_ref2}`
    document.getElementById("ref3").value =`Nombre: ${datos.n_ref3} Parentesco: ${datos.p_ref3} Telefono: ${datos.tel_ref3}`
    
    document.getElementById("poi1").value =`Nombre: ${datos.n_inquilino1} Parentesco: ${datos.p_inquilino1}`
    document.getElementById("poi2").value =`Nombre: ${datos.n_inquilino2} Parentesco: ${datos.p_inquilino2}`
    document.getElementById("poi3").value =`Nombre: ${datos.n_inquilino3} Parentesco: ${datos.p_inquilino3}`
    document.getElementById("poi4").value =`Nombre: ${datos.n_inquilino4} Parentesco: ${datos.p_inquilino4}`
    document.getElementById("poi5").value =`Nombre: ${datos.n_inquilino5} Parentesco: ${datos.p_inquilino5}`
    
    for(let i= 24; i< 44;i++)
    {
        let k2 = document.getElementsByName(k1[i]);
        console.log("yo soy k2",k2)
        k2[0].value =  datos[k1[i]];
        console.log("soy k2",k2[0]);
    }
// segundo for
    for(let i= 52; i< 58;i++)
    {
        let k2 = document.getElementsByName(k1[i]);
        console.log("yo soy k2 del for2",k2)
        k2[0].value =  datos[k1[i]];
        console.log("soy k2",k2[0]);
    }

 // Buro de credito
 // Tarjeta
    document.getElementById("tdc_vigente").value = datos.credito.tdc_vigente
    document.getElementById("tdc_num").value = datos.credito.tdc_num
    document.getElementById("tdc_limite").value =`$ ${datos.credito.tdc_limite}`
    document.getElementById("tdc_io").value = datos.credito.tdc_io
 // creditos
    document.getElementById("credito_vigente").value = datos.credito.credito_vigente
    document.getElementById("credi_ocupado").value = datos.credito.credi_ocupado

    document.getElementById("auto_num_cre").value = datos.credito.auto_num_cre
    document.getElementById("auto_io").value = datos.credito.auto_io

    document.getElementById("hipo_num_cre").value = datos.credito.hipo_num_cre
    document.getElementById("hipo_io").value = datos.credito.hipo_io

 // ocultador de inquilinos
       var poi2 = document.getElementById("poi2");
       var poi3 = document.getElementById("poi3");
       var poi4 = document.getElementById("poi4");
       var poi5 = document.getElementById("poi5");
  
       var inq2 = document.getElementById("inq2");
       var inq3 = document.getElementById("inq3");
       var inq4 = document.getElementById("inq4");
       var inq5 = document.getElementById("inq5");
       
  
        if(poi2.value=="Nombre: null Parentesco: null") {
             inq2.style.display='none';
         }
         else{
             inq2.style.display='';
              }
       if(poi3.value=="Nombre: null Parentesco: null") {
             inq3.style.display='none';
         }
         else{
             inq3.style.display='';
              }
       if(poi4.value=="Nombre: null Parentesco: null") {
             inq4.style.display='none';
         }
         else{
             inq4.style.display='';
              }
       if(poi5.value=="Nombre: null Parentesco: null") {
             inq5.style.display='none';
         }
         else{
             inq5.style.display='';
              }
              
    //localStorage.removeItem('data_inquilino')
    //console.log("limpio",localStorage)
            
}