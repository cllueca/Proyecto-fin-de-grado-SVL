import { createStore } from 'vuex'
import router from '../router/index'
import { getRelativeTime, getFormattedDate } from './timeFunctions'

export default createStore({
    state:
    {
        urlComun: 'http://localhost:5000/api/user/',
        token: null,
        serviciosEnlazados: null,
        serviciosDisponibles: null,
        messageLogin: null,
        messageReg: null
    },
    mutations:
    {
        async login(state, jsonData){
            
            fetch(state.urlComun + 'authenticate', {
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
                        state.messageLogin = null;
                        localStorage.setItem('jwt', data.Access_token)
                        state.token = jsonData['correo'];

                        var usuario = {
                            nombre: data.nombre,
                            apellidos: data.apellidos,
                            correo: jsonData['correo'],
                            fecha_registro: getFormattedDate(data.fecha_registro)
                        }

                        var cookieData = JSON.stringify({
                            usuario: usuario
                        });

                        $cookies.set('auth', cookieData);
                        router.push("/");
                    }
                    else
                    {
                        if (data.pct != 0)
                        { 
                            state.messageLogin = "Lo sentimos, no se ha reconocido su voz, ¿otro intento?";
                        }
                        else
                        {
                            state.messageLogin = data.Message;
                        }
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
        async register(state, jsonData){
            fetch(state.urlComun + 'add', {
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
                        state.messageReg = null;
                        localStorage.setItem('jwt', data.Access_token)
                        state.token = jsonData['correo'];

                        var usuario = {
                            nombre: data.User['nombre'],
                            apellidos: data.User['apellidos'],
                            correo: jsonData['correo'],
                            fecha_registro: 'Ahora mismo'
                        }

                        var cookieData = JSON.stringify({
                            usuario: usuario
                        });

                        $cookies.set('auth', cookieData);
                        router.push("/perfil");
                    }
                    else
                    {
                        state.messageReg = data.Message;
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
            if($cookies.isKey('auth')){
                if($cookies.get('auth') != null){

                    const jwt = localStorage.getItem('jwt');
                    localStorage.removeItem('jwt');

                    fetch(state.urlComun + 'logout', {
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
                                $cookies.remove('auth');

                                if(state.serviciosDisponibles != null){
                                    state.serviciosDisponibles = null;
                                }
            
                                if(state.serviciosEnlazados != null){
                                    state.serviciosEnlazados = null;
                                }

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
        async updateProfile(state, jsonData){
            const jwt = localStorage.getItem('jwt');
            fetch(state.urlComun + 'update', {
                method: 'POST',
                headers: {  'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            'Authorization': 'Bearer '+ jwt },
                body: JSON.stringify(jsonData)
              })
              .then(function(response) {
                if (response.ok) {
                  response.json().then(function(data) {
                    console.log('Datos enviados correctamente');
                    
                    if(!data.Error)
                    {
                        var usuario = {
                            nombre: data.NewData['nombre'],
                            apellidos: data.NewData['apellidos'],
                            correo: $cookies.get('auth')['usuario']['correo'],
                            fecha_registro: $cookies.get('auth')['usuario']['fecha_registro']
                        }

                        var cookieData = JSON.stringify({
                            usuario: usuario
                        });

                        $cookies.set('auth', cookieData);
                        location.reload(true);
                        alert(data.Message);
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
        },
        async getAvailableServices(state){
            const jwt = localStorage.getItem('jwt');
            fetch(state.urlComun + 'availableServices', {
                method: 'GET',
                headers: {  'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            'Authorization': 'Bearer '+ jwt },
              })
              .then(function(response) {
                if (response.ok) {
                  response.json().then(function(data) {
                    console.log('Datos enviados correctamente');
                    
                    if(!data.Error)
                    {
                        console.log(data.Message);
                        
                        if(Object.keys(data.Sitios).length != 0)
                        {
                            var cookieData = {}
                            
                            for (var sitio in data.Sitios){
                                cookieData[data.Sitios[sitio]['nombre']] = data.Sitios[sitio]
                            }
                            state.serviciosDisponibles = cookieData;
                        }
                    }
                    else
                    {
                        console.log(data.Message);
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
        async getLinkedServices(state)
        {
            const jwt = localStorage.getItem('jwt');
            fetch(state.urlComun + 'linkedServices', {
                method: 'GET',
                headers: {  'Accept': 'application/json',
                            'Content-Type': 'application/json',
                            'Authorization': 'Bearer '+ jwt },
            })
            .then(function(response) {
            if (response.ok) {
                response.json().then(function(data) {
                console.log('Datos enviados correctamente');
                
                if(!data.Error)
                {
                    console.log(data.Message);

                    if(Object.keys(data.Sitios).length != 0)
                    {
                        var cookieData = {}
                        
                        for (var sitio in data.Sitios){
                            
                            data.Sitios[sitio]['ultimo_login'] = getRelativeTime(data.Sitios[sitio]['ultimo_login']);
                            data.Sitios[sitio]['fecha_enlace'] = getFormattedDate(data.Sitios[sitio]['fecha_enlace']);
                            cookieData[data.Sitios[sitio]['nombre']] = data.Sitios[sitio]
                        }

                        state.serviciosEnlazados = cookieData;
                    }
                }
                else
                {
                    console.log(data.Message);
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
    },
    actions:{
        doLogin({ commit }, jsonData) {
            commit("login", jsonData);
        },
        doRegister({ commit }, jsonData) {
            commit("register", jsonData);
        },
        doLogout({ commit }, correo) {
            commit("logout", correo);
        },
        doUpdate({ commit }, jsonData) {
            commit("updateProfile", jsonData);
        },
        doGetAvailableServices({ commit }, jsonData){
            commit("getAvailableServices", jsonData);
        },
        doGetLinkedServices({ commit }, jsonData){
            commit("getLinkedServices", jsonData);
        }
    }
})