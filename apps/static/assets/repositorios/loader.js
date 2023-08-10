async function auten(){   
    await fetch('https://arredify-docker.onrender.com/user_unico/',{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': `Token ${localStorage.getItem('token')}`
          },
    })
     .then(response => response.json())
     .then(data => {
       
        try{ 
            if (data.user){
                document.querySelector('.dropdown-fl').style.display = 'block';
            }
            else{
                window.location.href = `/login/`
                localStorage.clear();
            }
        }
       catch{
           //window.location.replace(`/login/`);
          // window.location.href = `/login/`
           
       }
   })
     .catch(error => console.error(error));

}
