import { createStore } from 'vuex'
import router from '../router/index'

export default createStore({
    state:
    {
        token: null
    },
    mutations:
    {
        async checkActive(state, jsonData){
            fetch('http://127.0.0.1:5000/api/user/authenticate/external', {
                method: 'POST',
                headers: {  'Accept': 'application/json',
                            'Content-Type': 'application/json' },
                body: JSON.stringify(jsonData)
              })
              .then(function(response) {
                if (response.ok) {
                  response.json().then(function(data) {
                    console.log('Datos enviados correctamente');
                    
                    if(!data.Error)
                    {
                        localStorage.setItem('jwt', data.Access_token)
                        state.token = jsonData['correo'];

                        var usuario = {
                            nombre: data.nombre,
                            apellidos: data.apellidos,
                            correo: data.correo
                        }

                        var cookieData = JSON.stringify({
                            usuario: usuario
                        });

                        $cookies.set('auth-test-sso-1', cookieData);
                        router.push("/perfil");
                    }
                    else
                    {
                        console.log(data.Message);
                        alert(data.Message);
                    }
                  });
                } else {
                  console.log('Error al enviar los datos', response.statusText);
                }
              })
              .catch(function(error) {
                console.log('Error al enviar la solicitud POST:', error);
              });
        },
        async logout(state){
            if($cookies.isKey('auth-test-sso-1')){
                if($cookies.get('auth-test-sso-1') != null){

                    const jwt = localStorage.getItem('jwt');
                    localStorage.removeItem('jwt');

                    fetch('http://127.0.0.1:5000/api/user/logout', {
                        method: 'GET',
                        headers: {  'Accept': 'application/json',
                                    'Content-Type': 'application/json',
                                    'Authorization': 'Bearer '+ jwt }
                    })
                    .then(function(response) {
                        if (response.ok) {
                            response.json().then(function(data) {
                            console.log('Datos enviados correctamente');
                            if(!data.Error)
                            {
                                console.log(data.Message);
                                $cookies.remove('auth-test-sso-1');
                    
                                router.push("/");
                            }
                            else
                            {
                                alert(data.Message);
                            }
                            });
                        } else {
                            console.log('Error al enviar los datos', response.statusText);
                        }
                    })
                    .catch(function(error) {
                        console.log('Error al enviar la solicitud POST:', error);
                    });
                }
            }
            else{
                console.log("No existe cookie de autenticacion");
            }
        },
    },
    actions:{
        doCheckActive({ commit }, jsonData) {
            commit("checkActive", jsonData);
        },
        doLogout({ commit }, correo) {
            commit("logout", correo);
        }
    }
})