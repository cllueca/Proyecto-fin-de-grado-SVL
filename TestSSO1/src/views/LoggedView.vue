<template>
    <header>
        <p>TEST-SSO-1</p>
        <hr>
    </header>
    <h1> Hola {{ username }}</h1>
    <div class="row-12">
        <button class="btn btn-secondary btn-lg" @click="logout">Cerrar sesion</button>
    </div>
</template>

<style>

h1{
    width: 40%;
    margin: auto;
    display: flex;
    margin-bottom: 2%;
    padding: 10px;
    justify-content: center;
    align-items: center;
    font-weight: bold;
}

.row-12 button{
  width: 40%;
  margin: auto;
  display: flex;
  margin-bottom: 2%;
  padding: 10px;
  justify-content: center; /* Centra horizontalmente el contenido */
  align-items: center; /* Centra verticalmente el contenido */
  font-weight: bold;
}

</style>

<script>
import store from '../store/index'
export default{
    computed:{
      username(){
          var cookieData = $cookies.get('auth-test-sso-1')
          return cookieData['usuario']['nombre'];
      }
    },
    methods:
    {
        async logout()
        {
            try{
                await store.dispatch("doLogout");
            }
            catch(error)
            {
                console.log(error);
            }
        }
    }
}
</script>