<template>
  <header>
    <p>TEST-SSO-1</p>
    <hr>
  </header>
  <div class="container" id="botonesInicio">
    <div class="row-12">
      <button class="btn btn-primary" id="login" @click="mensajeLogin">Iniciar sesion</button>
    </div>
    <div class="row-12">
      <button class="btn  btn-primary" id="loginVL" @click="iniciarSesionVL(true)">Iniciar sesion con VL</button>
    </div>
    <div class="row-12">
      <button class="btn  btn-primary" id="register" @click="mensajeRegistro">Registrarse</button>
    </div>
  </div>

  <div class="container hide" id="formLogin">
    <div class="loginForm col-lg-5 col-md-8 col-sm-8 p-4">
        <div class="loginHeader pt-3 pb-4">
            <h4 id="tituloLogin">Voice Link</h4>
            <hr>
        </div>
        <div class="loginBody">
            
          <div class="form-group">
            <div class="input-group mb-3">
              <input type="text" class="form-control form-control-lg" name="email" placeholder="Correo..." v-model="correo">
            </div>
          </div>

          <div class="form-group row-12">
            <button type="submit" class="btn btn-block btn-lg btn-primary" @click.prevent="sendData">Entrar</button>
          </div>
          <div class="row-12">
            <button class="btn btn-secondary btn-block btn-lg" @click="iniciarSesionVL(false)">Volver</button>
          </div>
        </div>
    </div>
  </div>
</template>


<style>

header{
  text-align: center;
  padding: 20px;
  font-size: 30px;
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

.loginForm{
  width: 70%;
  height: 70%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform:translate(-50%,-50%);
  background: #f3f3f3;
  box-shadow: 1px 1px 4px #dcdcdc;
}

.hide {
  display: none;
}

#tituloLogin{
  text-align: center;
  font-size: 44px;
  text-decoration:underline;
  font-weight: bold;
}
</style>


<script>
import store from '../store/index'
export default {
  data() {
      return {
          correo: ''
      };
  },
  methods: {
    async sendData() {

      if(this.correo != '')
      {
        var jsonData = { correo: this.correo };

        try {
            await store.dispatch("doCheckActive", jsonData);
        } catch (error) {
            console.error(error);
        }
      }
      else
      {
        alert("Es necesario un coreo");
      }
      
    },
    mensajeRegistro()
    {
      alert("Registro propio no implementado en sitio de prueba, pulsa el segundo boton");
    },
    mensajeLogin(){
      alert("Login propio no implementado en sitio de prueba, pulsa el segundo boton");
    },
    iniciarSesionVL(esInicio)
    {
      var botones = document.getElementById('botonesInicio');
      var form = document.getElementById('formLogin');

      if(esInicio)
      {
        botones.classList.add('hide');
        form.classList.remove('hide');
      }
      else
      {
        botones.classList.remove('hide');
        form.classList.add('hide');
      }

    }
  }
}
</script>